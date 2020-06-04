-- users requested that height and weight units come before entering the values

DO
$do$
DECLARE
    q108 integer;
    q109 integer;
    q113 integer;
    q114 integer;
BEGIN
    -- store the current display indices
    SELECT display_index INTO q108 FROM ag.group_questions WHERE survey_question_id=108;
    SELECT display_index INTO q109 FROM ag.group_questions WHERE survey_question_id=109;
    SELECT display_index INTO q113 FROM ag.group_questions WHERE survey_question_id=113;
    SELECT display_index INTO q114 FROM ag.group_questions WHERE survey_question_id=114;

    -- set 108 to a temp value, put index from 109 as 108, put index from 108 as 109
    UPDATE ag.group_questions SET display_index=123456 WHERE survey_question_id=108;
    UPDATE ag.group_questions SET display_index=q108 WHERE survey_question_id=109;
    UPDATE ag.group_questions SET display_index=q109 WHERE survey_question_id=108;

    -- set 108 to a temp value, put index from 114 as 113, put index from 113 as 114
    UPDATE ag.group_questions SET display_index=123456 WHERE survey_question_id=113;
    UPDATE ag.group_questions SET display_index=q113 WHERE survey_question_id=114;
    UPDATE ag.group_questions SET display_index=q114 WHERE survey_question_id=113;
END $do$;

-- and add missing birth years... (derived from 0040.sql). This is painful.
ALTER TABLE ag.survey_question_response DROP CONSTRAINT idx_survey_question_response;
UPDATE ag.survey_question_response 
    SET display_index = display_index + 2 
    WHERE survey_question_id = 112 AND response != 'Unspecified';
ALTER TABLE ag.survey_question_response ADD CONSTRAINT idx_survey_question_response UNIQUE ( survey_question_id, display_index );

INSERT INTO ag.survey_response (american, british) VALUES ('2019', '2019');
INSERT INTO ag.survey_response (american, british) VALUES ('2020', '2020');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index, spanish, french, chinese) 
    VALUES (112, '2020', 1, '2020', '2020', '2020');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index, spanish, french, chinese) 
    VALUES (112, '2019', 2, '2019', '2019', '2019');
