-- September 24, 2015
-- Rename a few columns so they make more sense on pulldown

UPDATE ag.survey_question set question_shortname = 'ANTIBIOTIC_HISTORY' WHERE survey_question_id = 39;
UPDATE ag.survey_question set question_shortname = 'DOMINANT_HAND' WHERE survey_question_id = 22;
UPDATE ag.survey_question set question_shortname = 'NAIL_BITER' WHERE survey_question_id = 26;
