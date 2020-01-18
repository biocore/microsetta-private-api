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
        * Migrating all data from the
        * Migrating all data from the ag_consent table to source
        * Migrating all data from the consent_revoked table to source

        :param TRN: The active transaction
        :return:
        """

        # TODO: We need to throw away the legacy sql_connection code.
        TRN.add("SELECT "
                "ag_login_id, "
                "participant_name, "
                "ag_consent_backup.participant_email, "
                "is_juvenile, "
                "parent_1_name, "
                "parent_2_name, "
                # "parent_1_code, " # TODO: Can we drop these two?
                # "parent_2_code, "
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

            # TODO: !!CRITICAL!! @Daniel, Can you verify this is the
            #  correct logic for migrating source type, there doesn't
            #  appear to be any way to specify an environment source type,
            #  and there are existing primary surveys associated even when
            #  age_range is None!!
            new_age_range = r["age_range"]
            source_type = "human"
            if r["age_range"] == "ANIMAL_SURVEY":
                source_type = "animal"
                new_age_range = None

            TRN.add("INSERT INTO source("
                    "id, account_id, source_type, "
                    "participant_name, participant_email, "
                    "is_juvenile, "
                    "parent_1_name, parent_2_name, "
                    # "parent_1_code, parent_2_code " # Drop?
                    "deceased_parent, "
                    "date_signed, date_revoked, "
                    "assent_obtainer, age_range) "
                    "VALUES ("
                    "%s, %s, %s, "
                    "%s, %s, "
                    "%s, "
                    "%s, %s, "
                    # "%s, %s, " # Drop parent_1_code?
                    "%s, "
                    "%s, %s, "
                    "%s, %s)",
                    (source_id, r["ag_login_id"], source_type,
                     r["participant_name"], r["participant_email"],
                     r["is_juvenile"],
                     r["parent_1_name"], r["parent_2_name"],
                     # r["parent_1_code"], r["parent_2_code"],
                     r["deceased_parent"],
                     r["date_signed"], r["date_revoked"],
                     r["assent_obtainer"], new_age_range)
                    )

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
                    first_name = names[0]
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
