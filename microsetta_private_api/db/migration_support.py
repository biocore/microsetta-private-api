import uuid
import pycountry
from microsetta_private_api.config_manager import SERVER_CONFIG
import csv
import os.path
from collections import defaultdict


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
        country_map['U.S. Virgin Islands'] = 'US'

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

        email_counter = {}

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

            # Check for duplicate email addresses and munge the names
            email = r['email']
            if email in email_counter:
                email_counter[email] += 1
                email_pre = email.split("@")[0]
                email = email_pre + "+" + str(email_counter[email]) \
                    + "@" + email.split("@")[1]
            else:
                email_counter[email] = 1

            TRN.add("INSERT INTO account("
                    "id, email, account_type, auth_issuer, auth_sub, "
                    "first_name, last_name, "
                    "street, city, state, post_code, country_code, "
                    "latitude, longitude, "
                    "cannot_geocode, elevation) "
                    "VALUES("
                    "%s, %s, %s, %s, %s, "
                    "%s, %s, "
                    "%s, %s, %s, %s, %s, "
                    "%s, %s, "
                    "%s, %s) ",
                    (r['ag_login_id'], email, 'standard', None, None,
                     first_name, last_name,
                     r['address'], r['city'], r['state'], r['zip'], cc,
                     r['latitude'], r['longitude'],
                     r['cannot_geocode'], r['elevation']))

    @staticmethod
    def fork_primary_id(TRN, old_survey_id):
        # For each offending ID,
        # 2:    generate a new primary ID
        # 3:    insert a new row into ag_login_surveys
        # 4/5:  update/replicate entries in referencing tables.
        #       Note that updating primary keys in postgres appears to
        #       work in the referencing tables.  Also note that no cascade
        #       strategy could solve this more simply, as there are also
        #       vioscreen tables in our database that must continue to refer
        #       to the existing vioscreen survey id.
        #

        # 2: Generate a new primary ID
        # Newly returned survey responses at the moment are uuid v4,
        # legacy IDs are 16 random hex character strings
        # We will use the new survey ID format matching survey_answers_repo
        new_survey_id = str(uuid.uuid4())

        # 3: Insert a new row into ag_login_surveys
        TRN.add("SELECT ag_login_id, source_id, creation_time "
                "FROM ag_login_surveys "
                "WHERE survey_id=%s", (old_survey_id,))
        ag_login_id, source_id, creation_time = TRN.execute()[-1][-1]
        TRN.add("INSERT INTO ag_login_surveys "
                "(ag_login_id, survey_id, vioscreen_status, "
                "source_id, creation_time) "
                "VALUES (%s, %s, %s, %s, %s)",
                (ag_login_id, new_survey_id, None,
                 source_id, creation_time))

        # 4: Update referencing tables entries
        for table_name in [
                "survey_answers",
                "survey_answers_other",
                "external_survey_answers"]:
            TRN.add("UPDATE " + table_name + " SET survey_id=%s "
                                             "WHERE survey_id=%s",
                    (new_survey_id, old_survey_id))

        # 5: or Fork entries referencing tables
        for table_name in ["source_barcodes_surveys"]:
            TRN.add("SELECT barcode, survey_id FROM " + table_name + " "
                    "WHERE survey_id=%s",
                    (old_survey_id,))
            rows = TRN.execute()[-1]
            for row in rows:
                linked_barcode = row[0]
                TRN.add("INSERT INTO source_barcodes_surveys "
                        "(barcode, survey_id) "
                        "VALUES(%s, %s)", (linked_barcode, new_survey_id))

    @staticmethod
    def migrate_70(TRN):
        """
        At some point in the past, primary surveys and vioscreen surveys
        shared the same ID.  This means that there are entrees in
        ag_login_surveys which indicate both a vioscreen status and are tied
        to answers in survey_answers.  This does not match our desired model
        as it must always be possible to query which survey template a given
        survey id corresponds to.  This migration script splits the identifiers
        in ag_login_surveys.  The split will generate a new identifier for
        the primary survey, insert a new row into ag_login_surveys, and update
        the necessary rows in those tables that refer to survey_id:
            source_barcodes_surveys - Link samples to vioscreen AND primary.
            survey_answers - Link answers to primary
            survey_answers_other - Link answers_other to primary
            external_survey_answers - ??? Link to primary I guess.
        """
        # Plan:
        # 1: Find offending IDs
        #
        # For each offending ID,
        # 2:    generate a new primary ID
        # 3:    insert a new row into ag_login_surveys
        # 4/5:  update/replicate entries in referencing tables.
        #       Note that updating primary keys in postgres appears to
        #       work in the referencing tables.  Also note that no cascade
        #       strategy could solve this more simply, as there are also
        #       vioscreen tables in our database that must continue to refer
        #       to the existing vioscreen survey id.

        # 1: Find offending IDs:  Offending IDs are those that both have a
        # vioscreen status of 3 (meaning a completed vioscreen survey) and at
        # least one answer in the survey_answers table.
        TRN.add("SELECT DISTINCT survey_id FROM ag_login_surveys "
                "LEFT OUTER JOIN survey_answers USING (survey_id) "
                "WHERE vioscreen_status=3 AND response is not null")
        rows = TRN.execute()[-1]
        offending_ids = [r[0] for r in rows]

        for old_survey_id in offending_ids:
            MigrationSupport.fork_primary_id(TRN, old_survey_id)

        # Check that we were successful - no offending ids should remain
        TRN.add("SELECT DISTINCT survey_id FROM ag_login_surveys "
                "LEFT OUTER JOIN survey_answers USING (survey_id) "
                "WHERE vioscreen_status=3 AND response is not null")
        rows = TRN.execute()[-1]
        offending_ids = [r[0] for r in rows]
        if len(offending_ids) != 0:
            raise Exception("Couldn't resolve vioscreen/primary split :(")

    @staticmethod
    def migrate_74(TRN):
        TRN.add("SELECT DISTINCT "
                "ag_login_id, "
                "ag_login_surveys.source_id, "
                "ag_kit_barcode_id, "
                "ag_login_surveys.survey_id "
                "FROM "
                "ag_login_surveys LEFT JOIN "
                "source_barcodes_surveys USING (survey_id) LEFT JOIN "
                "ag_kit_barcodes USING (barcode) "
                "WHERE vioscreen_status is not null "
                )
        rows = TRN.execute()[-1]
        for r in rows:
            TRN.add("INSERT INTO vioscreen_registry("
                    "account_id, source_id, sample_id, vio_id) "
                    "VALUES(%s, %s, %s, %s)",
                    (r[0], r[1], r[2], r[3]))
        TRN.execute()

    @staticmethod
    def migrate_77(TRN):
        # a few studies were remarked as not-TMI when they actually are. A
        # retroactive update to these studies is necessary. In some cases
        # the studies have samples which are both present in the TMI structures
        # and some which are not, stemming from kits having been created
        # after remarking the project as non-TMI.
        project_ids = [69, 110, 72, 93, 97, 101, 102, 107, 75, 90, 92, 128]

        for project in project_ids:
            # gather all kits for the project which are not
            # in the ag.ag_kit table
            TRN.add("""SELECT kit_id, array_agg(barcode)
                       FROM barcodes.barcode
                           JOIN barcodes.project_barcode USING (barcode)
                       WHERE project_id=%s
                           AND kit_id NOT IN (
                               SELECT supplied_kit_id
                               FROM ag.ag_kit
                               )
                       GROUP BY kit_id""",
                    (project, ))
            kit_barcodes = TRN.execute()[-1]

            # some barcodes don't have kits!? gather them, make kits. our old
            # infrastructure allowed for creating sets of barcodes without
            # kits, which further complicates this migration.
            # gather unattached barcodes
            TRN.add("""SELECT barcode
                       FROM barcodes.barcode
                           JOIN barcodes.project_barcode USING (barcode)
                       WHERE project_id=%s
                           AND kit_id IS NULL""",
                    (project, ))
            unattached_barcodes = TRN.execute()[-1]
            unattached_barcodes = [r[0] for r in unattached_barcodes]

            # gather a prefix if one had already been used with the
            # project
            TRN.add("""SELECT supplied_kit_id
                       FROM ag.ag_kit
                           JOIN ag.ag_kit_barcodes USING (ag_kit_id)
                           JOIN barcodes.barcode
                               ON barcode.barcode=ag_kit_barcodes.barcode
                           JOIN barcodes.project_barcode
                               ON barcode.barcode=project_barcode.barcode
                       WHERE project_id=%s""",
                    (project, ))
            existing_kits = [r[0] for r in TRN.execute()[-1]]
            prefix = 'm77'  # default to m77 -> migration 77
            if len(existing_kits) > 0:
                prefixes = [k.split('_', 1)[0]
                            for k in existing_kits if '_' in k]
                if len(prefixes) > 0:
                    prefix = list(prefixes)[0]

            # Create and assign kits. e're going to use the existing logic
            # to create kits to be consistents, but it's a private
            # member method of AdminRepo. It is "safe" to use this method
            # as it does not have side effects.
            from microsetta_private_api.repo.admin_repo import AdminRepo
            careful_with_this = AdminRepo(None)

            unattached_kit_barcodes = []
            for barcode in unattached_barcodes:
                kit = careful_with_this._generate_random_kit_name(8, prefix)
                unattached_kit_barcodes.append((kit, (barcode, )))

                # establish kit associations within the database
                TRN.add("""INSERT INTO barcodes.kit
                           (kit_id)
                           VALUES (%s)""", (kit, ))
                TRN.add("""UPDATE barcodes.barcode
                           SET kit_id=%s
                           WHERE barcode=%s""", (kit, barcode))

            # recreate the steps taken at kit creation to place kit information
            # into the TMI structures
            # see https://github.com/biocore/microsetta-private-api/blob/2a6c5fd9a7c3aa925c45f9f6cc3a6626cee3ee8f/microsetta_private_api/repo/admin_repo.py#L746-L763  # noqa
            for kit, barcodes in kit_barcodes + unattached_kit_barcodes:
                # add these kits to ag_kit
                kit_uuid = str(uuid.uuid4())
                TRN.add("""INSERT INTO ag.ag_kit
                           (ag_kit_id, supplied_kit_id, swabs_per_kit)
                           VALUES (%s, %s, %s)""",
                        (kit_uuid, kit, len(barcodes)))

                # add the associated barcodes to ag_kit_barcodes
                for barcode in barcodes:
                    TRN.add("""INSERT INTO ag.ag_kit_barcodes
                               (ag_kit_id, barcode)
                               VALUES (%s, %s)""",
                            (kit_uuid, barcode))

            # remark the project as TMI
            TRN.add("""UPDATE barcodes.project
                       SET is_microsetta=true
                       WHERE project_id=%s""",
                    (project, ))
            TRN.execute()

    @staticmethod
    def migrate_82(TRN):
        def log(*args):
            print(*args)
            errors.append(' '.join([str(a) for a in args]))

        # flag for things that can go wrong
        # NOTHING_WRONG = 0
        MISSING_SURVEY_ID = 1
        SURVEY_IS_PRIMARY_ID = 2
        NO_SAMPLE_FOUND = 4
        MISMATCHED_VIO_STATUS = 8
        MISSING_SURVEY_ID_IN_REGISTRY = 16

        status_map = {
            "Finished": 3,
            "Review": 2,  # I have no idea what Review is supposed to map to.
            "Started": 1,
            "New": 0
        }
        vs_data_path = SERVER_CONFIG["vioscreen_patch_path"]
        if not os.path.exists(vs_data_path):
            print("No vioscreen patch found at: " + vs_data_path)
            return

        with open(vs_data_path) as csvfile:
            vio_reader = csv.reader(csvfile, delimiter='\t')
            header = True
            all_errors = {}
            all_wrong_flags = {}

            for patch_row in vio_reader:
                if header:
                    header = False
                    continue
                survey_id, status_string = patch_row
                status_num = status_map[status_string]

                errors = []
                wrong_flags = 0

                # Check state in ag_login_surveys
                TRN.add("SELECT ag_login_id, survey_id, vioscreen_status, "
                        "source_id, creation_time "
                        "FROM ag_login_surveys "
                        "WHERE survey_id = %s", (survey_id,))
                ag_rows = TRN.execute()[-1]

                # See if we have data at all.
                if len(ag_rows) == 0:
                    # No?  Error missing survey id.
                    log("No record in ag_login_surveys")
                    wrong_flags |= MISSING_SURVEY_ID
                elif len(ag_rows) == 1:
                    # We do have data.  Check if status matches.
                    if ag_rows[0][2] != status_num:
                        # No?  Error mismatched vio status
                        log("Mismatched status.  We say: " +
                            str(ag_rows[0][2]) + " they say: " +
                            str(status_num))
                        wrong_flags |= MISMATCHED_VIO_STATUS

                        # If our status is None, it means primary and vio
                        # shared survey IDs.  We need to fork the data.
                        if ag_rows[0][2] is None:
                            wrong_flags |= SURVEY_IS_PRIMARY_ID
                    else:
                        log("Status agrees.  Looks okay.")
                else:
                    # This can only be by programmer error.
                    log("Multiple ag_login_surveys rows!?!")
                    raise Exception("How can this happen!?")

                # Check state in vioscreen_registry as well
                TRN.add("SELECT vio_id, account_id, source_id, sample_id "
                        " FROM vioscreen_registry "
                        "WHERE vio_id = %s", (survey_id,))
                registry_rows = TRN.execute()[-1]
                if len(registry_rows) == 0:
                    # Nope.  missing from vioscreen registry.
                    log("We're missing this data from registry")
                    log("VIO:", patch_row)
                    wrong_flags |= MISSING_SURVEY_ID_IN_REGISTRY
                if len(registry_rows) >= 1:
                    # Ooh, found it.  Check if we can recover.
                    log("Found existing data:")
                    log("VIO:", survey_id, status_num)
                    log("US :", registry_rows)
                    if len(registry_rows) == 1:
                        if registry_rows[0][3] is None:
                            log("We don't know what sample to associate")
                            wrong_flags |= NO_SAMPLE_FOUND
                    else:
                        for r in registry_rows:
                            if r[3] is None:
                                # This can only by be programmer error.
                                log("Corrupted Registry.  Survey has samples "
                                    "But some samples are null!?")
                                log("Failing out.")
                                raise Exception("Null Samples!?")

                all_errors[survey_id] = errors
                all_wrong_flags[survey_id] = wrong_flags

                # Examine what all went wrong and determine resolution.
                if (wrong_flags & MISSING_SURVEY_ID) == MISSING_SURVEY_ID:
                    # Not here at all.  No idea what account to put it in
                    log("Manual Intervention Required: account unknown")
                if (wrong_flags & SURVEY_IS_PRIMARY_ID) \
                        == SURVEY_IS_PRIMARY_ID:
                    # It's here, but it's marked as a primary survey.
                    # We need to fork out the primary survey and mark this
                    # as a vioscreen survey in ag_login_surveys.
                    log("Resolution: Fork primary survey ID")
                    MigrationSupport.fork_primary_id(TRN, survey_id)
                    TRN.execute()
                    # It should already be marked as a mismatched status, which
                    # will then cause it to have status updated later on.
                    assert (wrong_flags & MISMATCHED_VIO_STATUS) == \
                        MISMATCHED_VIO_STATUS
                if (wrong_flags & NO_SAMPLE_FOUND) == NO_SAMPLE_FOUND:
                    # No idea what to associate this with.
                    # If there's only one sample, maybe we can do it?
                    # Even that is kind of guessing though...
                    log("Manual Intervention Required: Sample ID unknown")
                if (wrong_flags & MISMATCHED_VIO_STATUS) == \
                        MISMATCHED_VIO_STATUS:
                    log("Resolution: Updating "
                        "ag_login_surveys.vioscreen_status")
                    TRN.add("UPDATE ag_login_surveys SET "
                            "vioscreen_status = %s "
                            "WHERE survey_id = %s", (status_num, survey_id))
                    TRN.execute()
                if (wrong_flags & MISSING_SURVEY_ID_IN_REGISTRY) == \
                        MISSING_SURVEY_ID_IN_REGISTRY:
                    # There are a ton of ways this could happen.  Could be
                    # this survey wasn't in ag_login_surveys at all.  Could be
                    # it was there but was marked as a primary survey
                    # Could be it was there but had a vioscreen_status other
                    # than 3.  Regardless, if the data is there now, we can
                    # copy it over, otherwise, we're out of luck.
                    if len(ag_rows) == 0:
                        log("Manual Intervention Required: Missing data from "
                            "registry cannot be restored")
                    else:
                        log("Resolution: Copy into vioscreen_registry")
                        account_id = ag_rows[0][0]
                        source_id = ag_rows[0][3]

                        # we only want to update samples which are not already
                        # in the registry. participants who had taken part
                        # early in the project, and again more recently, may
                        # have a scenario where there are multiple vio_ids and
                        # multiple samples, where the the recent vio_id <->
                        # sample is in the registry and correct.
                        TRN.add("""SELECT DISTINCT ag_kit_barcode_id
                                   FROM source_barcodes_surveys
                                   LEFT JOIN ag_kit_barcodes USING (barcode)
                                   WHERE survey_id = %s
                                   AND ag_kit_barcode_id NOT IN
                                   (SELECT DISTINCT sample_id
                                    FROM vioscreen_registry
                                    WHERE deleted=false
                                        AND sample_id IS NOT NULL)""",
                                (survey_id,))
                        rows = TRN.execute()[-1]
                        if len(rows) == 0:
                            log("Barcodes already associated")
                        else:
                            for r in rows:
                                TRN.add("INSERT INTO vioscreen_registry("
                                        "account_id, source_id, "
                                        "sample_id, vio_id) "
                                        "VALUES(%s, %s, %s, %s)",
                                        (account_id, source_id, r[0],
                                         survey_id))
                            TRN.execute()

            status_map = defaultdict(int)
            for k in all_wrong_flags:
                status_map[all_wrong_flags[k]] += 1

            print("\n\n-------------------------------------------------\n\n")
            print("SUMMARY OF THINGS THAT ARE WRONG:")
            print(status_map)

            print("Examples")
            for status in status_map:
                print(status)
                for k in all_wrong_flags:
                    if all_wrong_flags[k] == status:
                        print("\n".join(all_errors[k]))
                        break

            print("\n\n-------------------------------------------------\n\n")
            print("SCROLL UP A BIT FOR SUMMARY!")
            print("ALL THE LOGS (-Uncomment me-)")
            # print(all_errors)

    @staticmethod
    def migrate_96(TRN):
        from microsetta_private_api.repo.source_repo import SourceRepo as sr

        TRN.add("SELECT id, source_name FROM source")
        rows = TRN.execute()[-1]

        for r in rows:
            hsi = sr.construct_host_subject_id(r[0], r[1])

            TRN.add("""INSERT INTO source_host_subject_id
                       (source_id, host_subject_id)
                       VALUES (%s, %s)""",
                    (r[0], hsi))
        TRN.execute()

    MIGRATION_LOOKUP = {
        "0048.sql": migrate_48.__func__,
        "0050.sql": migrate_50.__func__,
        "0070.sql": migrate_70.__func__,
        "0074.sql": migrate_74.__func__,
        "0077.sql": migrate_77.__func__,
        # patch 0082 migration is executed through hotfix_vioscreen.py
        # as it depends on external state
        # "0082.sql": migrate_82.__func__
        # ...
        "0096.sql": migrate_96.__func__,
    }

    @classmethod
    def run_migration(cls, TRN, patch_name):
        if patch_name in cls.MIGRATION_LOOKUP:
            try:
                cls.MIGRATION_LOOKUP[patch_name](TRN)
            except Exception as e:
                # TODO: We need to throw away the legacy sql_connection code!
                TRN._raise_execution_error('', '', e)
