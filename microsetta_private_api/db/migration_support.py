import uuid
import pycountry


class MigrationSupport:
    """
    Contains methods for data migrations that are difficult to express as
    pure SQL.  Methods are registered with script names in MIGRATION_LOOKUP.
    These methods will be run immediately after the script with the associated
    name, and as part of the same transaction.

    Note that you must have a sql script in the patch folder to run a
    migration method, even if no sql is required for the change
    """

    @staticmethod
    def migrate_48(TRN):
        """
        In order to support the REST api, we need participants to have unique
        ids.  This is a change from the previous keying in ag_consent
        which worked off of a compound key (ag_login_id, participant_name).

        As part of schema change 48, we are generating new unique IDs for all
        sources, and migrating the consent information from ag_consent and
        consent_revoked

        This requires:

        * Adding a new source table (Done in the 0048.sql)
        * Mapping each ag_login_id, participant_name pair to a new unique id
        * Migrating all data from the ag_consent table to source
        * Migrating all data from the consent_revoked table to source
        * Migrating ag_kit_barcodes.environment_sampled to source

        :param TRN: The active transaction
        :return:
        """

        # Migrate all human and animal sources from ag_consent
        # TODO: We need to throw away the legacy sql_connection code.
        TRN.add("SELECT "
                "ag_login_id, "
                "participant_name, "
                "ag_consent_backup.participant_email, "
                "is_juvenile, "
                "parent_1_name, "
                "parent_2_name, "
                "deceased_parent, "
                "date_signed, "
                "assent_obtainer, "
                "age_range, "
                "date_revoked "
                "FROM "
                "ag.ag_consent_backup "
                "LEFT JOIN "
                "ag.consent_revoked_backup "
                "USING (ag_login_id, participant_name)")

        rows = TRN.execute()[-1]
        # For each distinct ag_login_id, participant_name pair:
        for r in rows:
            # Generate a new id
            source_id = str(uuid.uuid4())

            # Add that id to the correct rows of ag_login_surveys
            TRN.add("UPDATE "
                    "ag_login_surveys "
                    "SET "
                    "source_id = %s "
                    "WHERE "
                    "ag_login_id = %s AND "
                    "participant_name = %s",
                    (source_id,
                     r["ag_login_id"],
                     r["participant_name"]))

            # Convert data formats:
            # Fix age range to not store type information

            new_age_range = r["age_range"]
            source_type = "human"
            if r["age_range"] == "ANIMAL_SURVEY":
                source_type = "animal"
                new_age_range = None

            new_deceased_parent = None
            if r['deceased_parent'] is not None:
                existing = r['deceased_parent'].lower()
                if existing in ['yes', 'true']:
                    new_deceased_parent = True
                elif existing in ['no', 'false']:
                    new_deceased_parent = False
                else:
                    raise RuntimeError(
                        "ERROR: Cannot migrate source.deceased_parent: "
                        "Unknown input: " + str(existing))

            TRN.add("INSERT INTO source("
                    "id, account_id, source_type, "
                    "source_name, participant_email, "
                    "is_juvenile, "
                    "parent_1_name, parent_2_name, "
                    "deceased_parent, "
                    "date_signed, date_revoked, "
                    "assent_obtainer, age_range) "
                    "VALUES ("
                    "%s, %s, %s, "
                    "%s, %s, "
                    "%s, "
                    "%s, %s, "
                    "%s, "
                    "%s, %s, "
                    "%s, %s)",
                    (source_id, r["ag_login_id"], source_type,
                     r["participant_name"], r["participant_email"],
                     r["is_juvenile"],
                     r["parent_1_name"], r["parent_2_name"],
                     new_deceased_parent,
                     r["date_signed"], r["date_revoked"],
                     r["assent_obtainer"], new_age_range)
                    )

            # Mark all samples associated with this source directly into the
            # ag_kit_barcodes table
            TRN.add("SELECT barcode "
                    "FROM ag_kit_barcodes "
                    "LEFT JOIN source_barcodes_surveys USING (barcode) "
                    "LEFT JOIN ag_login_surveys USING (survey_id) "
                    "LEFT JOIN ag_kit USING (ag_kit_id) "
                    "WHERE "
                    "ag_kit.ag_login_id=%s AND "
                    "participant_name=%s "
                    "GROUP BY "
                    "barcode",
                    (r["ag_login_id"], r["participant_name"]))

            # All these n+1 queries are bad for performance, but only
            # ~30000 rows at the time we're migrating, so no big deal.
            associated_barcodes = TRN.execute()[-1]
            for barcode_row in associated_barcodes:
                TRN.add("UPDATE ag_kit_barcodes "
                        "SET source_id=%s "
                        "WHERE barcode=%s",
                        (source_id, barcode_row['barcode']))

        # Migrate all environmental sources from ag_kit_barcodes
        # NOTE: Looking through the existing data, we found several samples
        # which have both an environment_sampled field and a human participant
        # name and associated survey.  We are therefore going to treat any
        # environment sample which has an associated participant name as
        # human sourced, rather than associated with the environment
        # We also found a number of environment_sampled='' rows.  (As opposed
        # to environment_sampled is null) As part of this migration, we are
        # either associating these samples with human sources (if that link
        # already exists), or we are discarding the ideas that these are env
        # samples and leaving them completely unassociated.

        # Thus the only samples we are going to migrate as environmental srcs
        # are those with an environment_sampled that is neither null nor empty
        # and with no association with any participant_name via surveys
        TRN.add("SELECT ag_kit.ag_login_id, barcode, environment_sampled "
                "FROM ag_kit_barcodes "
                "LEFT JOIN source_barcodes_surveys "
                "USING (barcode) "
                "LEFT JOIN ag_login_surveys "
                "USING (survey_id) "
                "LEFT JOIN ag_consent_backup "
                "USING (ag_login_id, participant_name) "
                "LEFT JOIN ag_kit "
                "USING (ag_kit_id) "
                "WHERE "
                "environment_sampled is not null AND "
                "environment_sampled != '' AND "
                "participant_name is null "
                "ORDER BY (ag_kit.ag_login_id, environment_sampled, barcode)")

        last_account_id = None
        name_suffix = 1
        env_rows = TRN.execute()[-1]
        for r in env_rows:
            if r['ag_login_id'] == last_account_id:
                name_suffix = name_suffix + 1
            else:
                name_suffix = 1
                last_account_id = r['ag_login_id']

            # Generate a new id
            source_id = str(uuid.uuid4())
            source_type = "environmental"
            # Add a new source
            TRN.add("INSERT INTO source("
                    "id, account_id, source_type, "
                    "source_name, participant_email, "
                    "is_juvenile, "
                    "parent_1_name, parent_2_name, "
                    "deceased_parent, "
                    "date_signed, date_revoked, "
                    "assent_obtainer, age_range, description) "
                    "VALUES ("
                    "%s, %s, %s, "
                    "%s, %s, "
                    "%s, "
                    "%s, %s, "
                    "%s, "
                    "%s, %s, "
                    "%s, %s, %s)",
                    (source_id, r["ag_login_id"], source_type,
                     "Environmental Sample-" + str(name_suffix).zfill(3), None,
                     None,
                     None, None,
                     None,
                     None, None,
                     None, None, r['environment_sampled'])
                    )
            # Write that source into the sample to keep it linked up
            TRN.add("UPDATE ag_kit_barcodes "
                    "SET source_id=%s "
                    "WHERE barcode=%s",
                    (source_id, r['barcode']))

    @staticmethod
    def migrate_50(TRN):
        country_map = {x.name: x.alpha_2 for x in pycountry.countries}

        # Apparently we have a few country strings pycountry can't map well,
        # add any others we need to migrate right here to complete migration:
        country_map[None] = ''
        country_map[''] = ''
        country_map['South Korea'] = 'KR'
        country_map['US'] = 'US'
        country_map['Czech Republic'] = 'CZ'

        TRN.add("SELECT DISTINCT country FROM ag_login_backup")
        rows = TRN.execute()[-1]
        db_countries = [r['country'] for r in rows]

        need_to_map_manually = []
        for country in db_countries:
            if country not in country_map:
                need_to_map_manually.append(country)

        if len(need_to_map_manually) > 0:
            raise RuntimeError(
                "ERROR: Cannot migrate ag_login: Require "
                "country codes for: " + str(need_to_map_manually))

        TRN.add("SELECT "
                "ag_login_id, email, name, "
                "address, city, state, zip, country, "
                "latitude, longitude, cannot_geocode, elevation "
                "FROM "
                "ag_login_backup")

        rows = TRN.execute()[-1]
        for r in rows:
            # Split name into first name last name with simple heuristic
            first_name = None
            last_name = None
            if r['name'] is not None:
                names = r['name'].split()
                if len(names) == 1:
                    first_name = names[0]
                elif len(names) >= 2:
                    first_name = " ".join(names[0:-1])
                    last_name = names[-1]

            # Look up country code
            cc = country_map[r['country']]

            TRN.add("INSERT INTO account("
                    "id, email, account_type, auth_provider, "
                    "first_name, last_name, "
                    "street, city, state, post_code, country_code, "
                    "latitude, longitude, "
                    "cannot_geocode, elevation) "
                    "VALUES("
                    "%s, %s, %s, %s, "
                    "%s, %s, "
                    "%s, %s, %s, %s, %s, "
                    "%s, %s, "
                    "%s, %s)",
                    (r['ag_login_id'], r['email'], 'standard', 'GLOBUS',
                     first_name, last_name,
                     r['address'], r['city'], r['state'], r['zip'], cc,
                     r['latitude'], r['longitude'],
                     r['cannot_geocode'], r['elevation']))

    MIGRATION_LOOKUP = {
        "0048.sql": migrate_48.__func__,
        "0050.sql": migrate_50.__func__
        # ...
    }

    @classmethod
    def run_migration(cls, TRN, patch_name):
        if patch_name in cls.MIGRATION_LOOKUP:
            try:
                cls.MIGRATION_LOOKUP[patch_name](TRN)
            except Exception as e:
                # TODO: We need to throw away the legacy sql_connection code!
                TRN._raise_execution_error('', '', e)
