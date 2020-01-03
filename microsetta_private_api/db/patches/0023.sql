-- Sept 16, 2015
-- Add way to retire questions
--promote unmappable questions from old survey

ALTER TABLE ag.survey_question ADD COLUMN retired boolean DEFAULT FALSE;
-- Add plants question back as a retired question
INSERT INTO survey_question (survey_question_id, question_shortname, american, british, retired) VALUES
(146, 'TYPES_OF_PLANTS', 'How many different species of plants did you consume during the last 7-day period?', 'How many different species of plants did you consume during the last 7-day period?', TRUE);

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (146, 'SINGLE');

INSERT INTO survey_response (american, british) VALUES ('Less than 5', 'Less than 5');
INSERT INTO survey_response (american, british) VALUES ('6 to 10', '6 to 10');
INSERT INTO survey_response (american, british) VALUES ('11 to 20', '11 to 20');
INSERT INTO survey_response (american, british) VALUES ('21 to 30', '21 to 30');
INSERT INTO survey_response (american, british) VALUES ('More than 30', 'More than 30');

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, 'Less than 5', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, '6 to 10', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, '11 to 20', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, '21 to 30', 4);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (146, 'More than 30', 5);

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-1, 146, 50);

-- Promote answers
DO $do$
DECLARE
    ans varchar;
    survey varchar;
    pid varchar;
    login varchar;
BEGIN
    -- Make sure not in test database so there's actually something to promote
    IF NOT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema = 'ag' AND table_name = 'ag_human_survey')
    THEN
        RETURN;
    END IF;

    FOR pid, login IN
        SELECT participant_name, ag_login_id FROM ag.ag_human_survey
    LOOP
        SELECT survey_id FROM ag.ag_login_surveys WHERE participant_name = pid AND ag_login_id::varchar = login INTO survey;
        -- If unpromoted survey, don't convert answers
        IF survey = NULL
        THEN
            CONTINUE;
        END IF;
        -- Assign uninterpretable answers to 'Unspecified'
        SELECT CASE(types_of_plants)
           WHEN '28' THEN '21 to 30'
           WHEN 'Less than 5' THEN 'Less than 5'
           WHEN '6 to 10' THEN '6 to 10'
           WHEN '11 to 20' THEN '11 to 20'
           WHEN '21 to 30' THEN '21 to 30'
           WHEN 'More than 30' THEN 'More than 30'
           ELSE 'Unspecified'
        END
        FROM ag.ag_human_survey WHERE participant_name = pid AND ag_login_id::varchar = login INTO ans;

        INSERT INTO ag.survey_answers (survey_id, survey_question_id, response) VALUES (survey, 146, ans);
    END LOOP;
END $do$;

-- Make the rest of the answers Unspecified
INSERT INTO ag.survey_answers (survey_id, survey_question_id, response)
    SELECT survey_id, 146, 'Unspecified'
    FROM ag.ag_login_surveys
    WHERE survey_id NOT IN (
        SELECT survey_id
        FROM ag.survey_answers
        WHERE survey_question_id = 146);
