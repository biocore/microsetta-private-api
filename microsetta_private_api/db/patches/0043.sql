-- remove a duplicate survey_question_response_type entry created from patch 0033
-- which appears to be a copy/pasta event from patch 0023, and add a constraint
-- to ensure the entries of survey_question_response_type are unique.

-- https://stackoverflow.com/questions/6583916/delete-completely-duplicate-rows-in-postgresql-and-keep-only-1
DELETE FROM ag.survey_question_response_type a
    WHERE a.ctid <> (SELECT min(b.ctid)
    FROM   ag.survey_question_response_type b
    WHERE  a.survey_question_id = b.survey_question_id);

ALTER TABLE ag.survey_question_response_type 
    ADD CONSTRAINT uc_survey_question_response_type 
    UNIQUE (survey_question_id, survey_response_type);
