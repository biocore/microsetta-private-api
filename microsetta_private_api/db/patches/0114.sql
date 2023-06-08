-- Retire the COVID-19 survey
UPDATE ag.surveys SET retired = true WHERE survey_id = 21;

-- Retire the questions we won't be moving to other surveys
UPDATE ag.survey_question SET retired = true WHERE survey_question_id IN (209, 210, 213, 216, 217, 238, 218, 220, 226, 227, 228);

-- Clean up triggers for retired questions
DELETE FROM ag.survey_question_triggers WHERE triggered_question = 213;

-- Move two questions into the Lifestyle group
UPDATE ag.group_questions SET survey_group = -12, display_index = 29 WHERE survey_question_id = 219 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -12, display_index = 30 WHERE survey_question_id = 225 AND survey_group = -21;

-- Move the other questions into the General Health group
UPDATE ag.group_questions SET survey_group = -14, display_index = 23 WHERE survey_question_id = 211 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 24 WHERE survey_question_id = 212 AND survey_group = -21;
-- We're leaving an open spot for a new question (created below) at display_index = 25
UPDATE ag.group_questions SET survey_group = -14, display_index = 26 WHERE survey_question_id = 214 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 27 WHERE survey_question_id = 221 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 28 WHERE survey_question_id = 222 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 29 WHERE survey_question_id = 223 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 30 WHERE survey_question_id = 224 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 31 WHERE survey_question_id = 229 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 32 WHERE survey_question_id = 230 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 33 WHERE survey_question_id = 231 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 34 WHERE survey_question_id = 232 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 35 WHERE survey_question_id = 233 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 36 WHERE survey_question_id = 234 AND survey_group = -21;
UPDATE ag.group_questions SET survey_group = -14, display_index = 37 WHERE survey_question_id = 235 AND survey_group = -21;

-- Adjust the wording of a few existing questions
UPDATE ag.survey_question SET american = 'In the past month, have you been exposed to someone likely to have Coronavirus/COVID-19? (check all that apply)' WHERE survey_question_id = 211;
UPDATE ag.survey_question SET american = 'In the past month, have you been suspected of having Coronavirus/COVID-19 infection?' WHERE survey_question_id = 212;
UPDATE ag.survey_question SET american = 'In the past 6 weeks, have you had any of the following symptoms? (check all that apply)' WHERE survey_question_id = 214;
INSERT INTO ag.survey_response (american, spanish, spain_spanish) VALUES ('Lack of appetite', 'Falta de apetito', 'Falta de apetito');
UPDATE ag.survey_question_response SET response = 'Lack of appetite' WHERE response = 'Lack of appetitie';
-- Now let's add new options. First, we'll add the options to the database
INSERT INTO ag.survey_response (american) VALUES
    ('Shortness of breath or difficulty breathing'),
    ('Headaches'),
    ('Muscle aches'),
    ('Runny or stuffy nose'),
    ('Wheezing');
-- Then, we'll update display_index values for existing options and drop in new ones
UPDATE ag.survey_question_response SET display_index = 16 WHERE survey_question_id = 214 AND display_index = 11;
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'Wheezing', 15);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'Runny or stuffy nose', 14);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'Muscle aches', 13);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'Headaches', 12);
UPDATE ag.survey_question_response SET display_index = 11 WHERE survey_question_id = 214 AND display_index = 10;
UPDATE ag.survey_question_response SET display_index = 10 WHERE survey_question_id = 214 AND display_index = 9;
UPDATE ag.survey_question_response SET display_index = 9 WHERE survey_question_id = 214 AND display_index = 8;
UPDATE ag.survey_question_response SET display_index = 8 WHERE survey_question_id = 214 AND display_index = 7;
UPDATE ag.survey_question_response SET display_index = 7 WHERE survey_question_id = 214 AND display_index = 6;
UPDATE ag.survey_question_response SET display_index = 6 WHERE survey_question_id = 214 AND display_index = 5;
UPDATE ag.survey_question_response SET display_index = 5 WHERE survey_question_id = 214 AND display_index = 4;
UPDATE ag.survey_question_response SET display_index = 4 WHERE survey_question_id = 214 AND display_index = 3;
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'Shortness of breath or difficulty breathing', 3);

-- Add new question to General Health group
INSERT INTO ag.survey_question (survey_question_id, american, question_shortname, retired, css_classes) VALUES (521, 'How many times have you been infected with Coronavirus/COVID-19?', 'COVID_TIMES_INFECTED', false, 'tmi-survey-radio-horizontal');
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type) VALUES (521, 'SINGLE');
INSERT INTO ag.survey_response (american) VALUES ('3 or more');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
    (521, '0', 1),
    (521, '1', 2),
    (521, '2', 3),
    (521, '3 or more', 4);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (-14, 521, 25);
