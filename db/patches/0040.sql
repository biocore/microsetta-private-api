-- Mar 1, 2017
-- Add 2016 and 2017 as a birth year

-- This patch is entirely based off of 0031.sql

-- Remove the unique constraint to allow the incrementing, then increment and re-add the constraint
ALTER TABLE survey_question_response DROP CONSTRAINT idx_survey_question_response;
UPDATE survey_question_response SET display_index = display_index + 2 WHERE survey_question_id = 112 and response != 'Unspecified';
ALTER TABLE survey_question_response ADD CONSTRAINT idx_survey_question_response UNIQUE ( survey_question_id, display_index );


INSERT INTO survey_response (american, british) VALUES ('2016', '2016');
INSERT INTO survey_response (american, british) VALUES ('2017', '2017');
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (112, '2017', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (112, '2016', 2);
