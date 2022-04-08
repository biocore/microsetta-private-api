# Dumping a survey

To dump a survey, refer to the survey ID (see `select survey_id, american from ag.surveys join ag.survey_group on survey_group=group_order;`).

```bash
python dump-survey.py <survey_id_number>
```

# Constructing the bulk of a language patch

The majority of the patch for the survey in a new language can be constructed with:

```bash
python format_language_patches.py --input <your_xls_file> --output <the_patch> --lang <language_name>
```

This will not automatically create the survey name and group entries. Please see `microsetta_private_api/db/patches/0081.sql` for an example
