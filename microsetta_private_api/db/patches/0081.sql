-- spanish responses were not reflected in this table
ALTER TABLE ag.survey_response ADD COLUMN spanish VARCHAR;
UPDATE ag.survey_response
    SET spanish=survey_question_response.spanish
    FROM ag.survey_question_response
    WHERE survey_response.american=survey_question_response.response;
