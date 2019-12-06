-- May 5th, 2017
-- Stefan Janssen

-- remove tables identified as no longer used in our code base. Most likely, they are left overs from the transition from Oracle to Postgres

-- tables whose names do not show up in codebases of american-gut-web and labadmin (grep name *.py -i)
DROP TABLE ag.ag_animal_survey;
DROP TABLE ag.ag_human_survey;
DROP TABLE ag.ag_import_stats_tmp;
DROP TABLE ag.ag_map_markers;
DROP TABLE ag.ag_participant_exceptions;
DROP TABLE ag.ag_survey_answer;
DROP TABLE ag.ag_survey_multiples;
DROP TABLE ag.ag_survey_multiples_backup;
DROP TABLE barcodes.barcode_exceptions;
DROP TABLE ag.controlled_vocab_values;
DROP TABLE ag.controlled_vocabs;

-- we only delete information from this table, but never read or write. Can't we simply delete the full table then?
DROP TABLE ag.promoted_survey_ids;
