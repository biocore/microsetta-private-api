-- Feb 4, 2016
-- Create consent revoked table
CREATE TABLE ag.consent_revoked ( 
    ag_login_id          uuid  NOT NULL,
    participant_name     varchar  NOT NULL,
    participant_email    varchar  NOT NULL,
    date_revoked         date DEFAULT current_date NOT NULL,
    CONSTRAINT idx_consent_revoked UNIQUE ( ag_login_id, participant_name ) 
 );

CREATE INDEX idx_consent_revoked_0 ON ag.consent_revoked ( ag_login_id );

ALTER TABLE ag.consent_revoked ADD CONSTRAINT fk_consent_revoked FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id );

-- Add IBD diagnosis type as retired question
INSERT INTO survey_question (survey_question_id, question_shortname, american, british, retired) VALUES
(161, 'IBD_DIAGNOSIS', 'Which type of IBD?', 'Which type of IBD?', TRUE);

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (146, 'SINGLE');

INSERT INTO survey_response (american, british) VALUES ('Ulcerative colitis', 'Ulcerative colitis');
INSERT INTO survey_response (american, british) VALUES ('Crohn''s disease', 'Crohn''s disease');

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (161, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (161, 'Ulcerative colitis', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (161, 'Crohn''s disease', 2);

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-1, 161, 50);

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
        IF survey IS NULL
        THEN
            CONTINUE;
        END IF;
        -- Assign uninterpretable answers to 'Unspecified'
        SELECT CASE(ibd)
           WHEN 'Ulcerative colitis' THEN 'Ulcerative colitis'
           WHEN 'Crohn''s disease' THEN 'Crohn''s disease'
           ELSE 'Unspecified'
        END
        FROM ag.ag_human_survey WHERE participant_name = pid AND ag_login_id::varchar = login INTO ans;

        INSERT INTO ag.survey_answers (survey_id, survey_question_id, response) VALUES (survey, 161, ans);
    END LOOP;
END $do$;

-- Make the rest of the answers Unspecified
INSERT INTO ag.survey_answers (survey_id, survey_question_id, response)
    SELECT survey_id, 161, 'Unspecified'
    FROM ag.ag_login_surveys
    WHERE survey_id NOT IN (
        SELECT survey_id
        FROM ag.survey_answers
        WHERE survey_question_id = 161);
