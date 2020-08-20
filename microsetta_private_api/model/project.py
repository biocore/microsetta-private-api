import datetime

PROJ_ID_KEY = "project_id"
# This is a pain: in the db, the field that holds the project name is called
# "project", but that is the idiom that code/yaml uses for the whole object.
# Too risky to change the db, too likely to cause bugs to change the code
# idiom just for this one object, so handling both keys
PROJ_NAME_KEY = 'project_name'
DB_PROJ_NAME_KEY = 'project'
IS_MICROSETTA_KEY = 'is_microsetta'
BANK_SAMPLES_KEY = 'bank_samples'
PLATING_START_DATE_KEY = 'plating_start_date'
CONTACT_NAME_KEY = 'contact_name'
ADDTL_CONTACT_NAME_KEY = 'additional_contact_name'
CONTACT_EMAIL_KEY = 'contact_email'
DEADLINES_KEY = 'deadlines'
NUM_SUBJECTS_KEY = 'num_subjects'
NUM_TIMEPOINTS_KEY = 'num_timepoints'
START_DATE_KEY = 'start_date'
DISPOSITION_COMMENTS_KEY = 'disposition_comments'
COLLECTION_KEY = 'collection'
IS_FECAL_KEY = 'is_fecal'
IS_SALIVA_KEY = 'is_saliva'
IS_SKIN_KEY = 'is_skin'
IS_BLOOD_KEY = 'is_blood'
IS_OTHER_KEY = 'is_other'
DO_16S_KEY = 'do_16s'
DO_SHALLOW_SHOTGUN_KEY = 'do_shallow_shotgun'
DO_SHOTGUN_KEY = 'do_shotgun'
DO_RT_QPCR_KEY = 'do_rt_qpcr'
DO_SEROLOGY_KEY = 'do_serology'
DO_METATRANSCRIPTOMICS_KEY = 'do_metatranscriptomics'
DO_MASS_SPEC_KEY = 'do_mass_spec'
MASS_SPEC_COMMENTS_KEY = 'mass_spec_comments'
MASS_SPEC_CONTACT_NAME_KEY = 'mass_spec_contact_name'
MASS_SPEC_CONTACT_EMAIL_KEY = 'mass_spec_contact_email'
DO_OTHER_KEY = 'do_other'
BRANDING_ASSOC_INSTRUCTIONS_KEY = 'branding_associated_instructions'
BRANDING_STATUS_KEY = 'branding_status'
SUBPROJECT_NAME_KEY = 'subproject_name'
ALIAS_KEY = 'alias'
SPONSOR_KEY = 'sponsor'
COORDINATION_KEY = 'coordination'
COMPUTED_STATS_KEY = 'computed_stats'

# Clearly the set of computed statistics for projects is going to grow and
# mutate. Any new ones need their keys defined here and then added in
# get_computed_stats_keys() below.
NUM_KITS_KEY = 'num_kits'
NUM_SAMPLES_KEY = 'num_samples'
NUM_SAMPLES_RECEIVED_KEY = 'num_samples_received'
NUM_UNIQUE_SOURCES_KEY = 'num_unique_sources'
NUM_PARTIALLY_RETURNED_KITS_KEY = 'num_partially_returned_kits'
NUM_FULLY_RETURNED_KITS_KEY = 'num_fully_returned_kits'
NUM_KITS_W_PROBLEMS_KEY = "num_kits_w_problems"

# I hate these status strings. They are independently (re)defined
# in the sql patches, in the microsetta-private-api yaml, AND in at least one
# of the microsetta-admin templates, and they MUST be the same in all places.
# Adding yet one more redefinition here because it is preferable to hard-coding
# them into the AdminRepo ...
VALID_SAMPLES_STATUS = 'sample-is-valid'
UNKNOWN_VALIDITY_STATUS = 'received-unknown-validity'
NO_ACCOUNT_STATUS = 'no-registered-account'
NO_SOURCE_STATUS = 'no-associated-source'
NO_COLLECTION_INFO_STATUS = 'no-collection-info'
SAMPLE_STATUSES = [VALID_SAMPLES_STATUS, UNKNOWN_VALIDITY_STATUS,
                   NO_ACCOUNT_STATUS, NO_SOURCE_STATUS,
                   NO_COLLECTION_INFO_STATUS]


def get_computed_stats_keys():
    """Return list of all keys for computed statistics about a project."""

    # order not important
    result = [NUM_KITS_KEY, NUM_SAMPLES_KEY,
              NUM_SAMPLES_RECEIVED_KEY, NUM_UNIQUE_SOURCES_KEY,
              NUM_PARTIALLY_RETURNED_KITS_KEY,
              NUM_FULLY_RETURNED_KITS_KEY, NUM_KITS_W_PROBLEMS_KEY]

    num_status_keys = get_num_status_keys()
    result.extend(num_status_keys)
    return result


def get_num_status_keys():
    """Return list of the stats keys for number of samples with each status."""

    result = []
    for curr_status in SAMPLE_STATUSES:
        status_w_underscores = curr_status.replace("-", "_")
        result.append("num_{0}".format(status_w_underscores))

    return result


class Project:
    def __init__(self, **kwargs):
        # when project is created with input from front api, id
        # won't yet exist
        self.project_id = kwargs.get(PROJ_ID_KEY)

        # these and project_name (handled later) are the only required fields
        self.is_microsetta = kwargs[IS_MICROSETTA_KEY]
        self.bank_samples = kwargs[BANK_SAMPLES_KEY]

        # all the remaining fields are optional and default to None
        self.plating_start_date = kwargs.get(PLATING_START_DATE_KEY)
        self.contact_name = kwargs.get(CONTACT_NAME_KEY)
        self.additional_contact_name = kwargs.get(ADDTL_CONTACT_NAME_KEY)
        self.contact_email = kwargs.get(CONTACT_EMAIL_KEY)
        self.deadlines = kwargs.get(DEADLINES_KEY)
        self.num_subjects = kwargs.get(NUM_SUBJECTS_KEY)
        self.num_timepoints = kwargs.get(NUM_TIMEPOINTS_KEY)
        self.start_date = kwargs.get(START_DATE_KEY)
        self.disposition_comments = kwargs.get(DISPOSITION_COMMENTS_KEY)
        self.collection = kwargs.get(COLLECTION_KEY)
        self.is_fecal = kwargs.get(IS_FECAL_KEY)
        self.is_saliva = kwargs.get(IS_SALIVA_KEY)
        self.is_skin = kwargs.get(IS_SKIN_KEY)
        self.is_blood = kwargs.get(IS_BLOOD_KEY)
        self.is_other = kwargs.get(IS_OTHER_KEY)
        self.do_16s = kwargs.get(DO_16S_KEY)
        self.do_shallow_shotgun = kwargs.get(DO_SHALLOW_SHOTGUN_KEY)
        self.do_shotgun = kwargs.get(DO_SHOTGUN_KEY)
        self.do_rt_qpcr = kwargs.get(DO_RT_QPCR_KEY)
        self.do_serology = kwargs.get(DO_SEROLOGY_KEY)
        self.do_metatranscriptomics = kwargs.get(DO_METATRANSCRIPTOMICS_KEY)
        self.do_mass_spec = kwargs.get(DO_MASS_SPEC_KEY)
        self.mass_spec_comments = kwargs.get(MASS_SPEC_COMMENTS_KEY)
        self.mass_spec_contact_name = kwargs.get(MASS_SPEC_CONTACT_NAME_KEY)
        self.mass_spec_contact_email = kwargs.get(MASS_SPEC_CONTACT_EMAIL_KEY)
        self.do_other = kwargs.get(DO_OTHER_KEY)
        self.branding_associated_instructions = kwargs.get(
            BRANDING_ASSOC_INSTRUCTIONS_KEY)
        self.branding_status = kwargs.get(BRANDING_STATUS_KEY)
        self.subproject_name = kwargs.get(SUBPROJECT_NAME_KEY)
        self.alias = kwargs.get(ALIAS_KEY)
        self.sponsor = kwargs.get(SPONSOR_KEY)
        self.coordination = kwargs.get(COORDINATION_KEY)

        self.computed_stats = kwargs.get(COMPUTED_STATS_KEY, {})

        project_name = kwargs.get(PROJ_NAME_KEY)
        db_project_name = kwargs.get(DB_PROJ_NAME_KEY)

        if project_name is None:
            if db_project_name is None:
                raise ValueError("No project name provided")
            self.project_name = db_project_name
        elif project_name is not None:
            if db_project_name is not None:
                if project_name != db_project_name:
                    raise ValueError("Conflicting project names provided")
            self.project_name = project_name

        if self.plating_start_date is not None:
            if isinstance(self.plating_start_date, str):
                try:
                    self.plating_start_date = datetime.datetime.strptime(
                        self.plating_start_date, "%Y-%m-%d")
                except ValueError:
                    raise ValueError(
                        "plating start date '{0}' is not a valid date in "
                        "YYYY-MM-DD format".format(self.plating_start_date))

        if not self.bank_samples and self.plating_start_date is not None:
            raise ValueError("Plating start date cannot be set for"
                             " unbanked projects")

    @classmethod
    def from_db(cls, row):
        row_dict = dict(row)
        return Project(**row_dict)

    @staticmethod
    def from_dict(values_dict):
        return Project(**values_dict)

    def to_api(self):
        return vars(self)
