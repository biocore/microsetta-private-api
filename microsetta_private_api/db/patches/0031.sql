-- Dec 7, 2015
-- Add 2015 as a birth year

-- Remove the unique constraint to allow the incrementing, then increment and re-add the constraint
ALTER TABLE survey_question_response DROP CONSTRAINT idx_survey_question_response;
UPDATE survey_question_response SET display_index = display_index + 1 WHERE survey_question_id = 112 and response != 'Unspecified';
ALTER TABLE survey_question_response ADD CONSTRAINT idx_survey_question_response UNIQUE ( survey_question_id, display_index );


INSERT INTO survey_response (american, british) VALUES ('2015', '2015');
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (112, '2015', 1);