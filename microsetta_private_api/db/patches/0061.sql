-- add in a few approved questions to the primary survey, and one to covid
-- in addition, apply some tweaks / cleanup to the covid survey

-- Update the name of the survey. This was previously called "Primary Information"
-- But it's what gets presented to the user. We don't really have a concept of the
-- name of a survey, but we potentially should add that.
UPDATE ag.survey_group 
    SET american='Microsetta Initiative/American Gut Project' 
    WHERE group_order = -1;

UPDATE ag.survey_group 
    SET british='Microsetta Initiative/American Gut Project' 
    WHERE group_order = -1;

-- update the phrasing of an existing question
UPDATE ag.survey_question
    SET american='In an average week, how often do you consume at least 2-3 servings of starchy and non-starchy vegetables. Examples of starchy vegetables include white potatoes, corn, peas and cabbage.  Examples of non-starchy vegetables include raw leafy greens, cucumbers, tomatoes, peppers, broccoli, and kale. (1 serving = ½ cup vegetables/potatoes; 1 cup leafy raw vegetables)',
        british='In an average week, how often do you consume at least 2-3 servings of starchy and non-starchy vegetables. Examples of starchy vegetables include white potatoes, corn, peas and cabbage.  Examples of non-starchy vegetables include raw leafy greens, cucumbers, tomatoes, peppers, broccoli, and kale. (1 serving = ½ cup vegetables/potatoes; 1 cup leafy raw vegetables)'
    WHERE survey_question_id=62;

-- add new responses to a few questions
UPDATE ag.survey_question_response 
    SET display_index=5 
    WHERE survey_question_id=212 AND response='No symptoms or signs';
INSERT INTO ag.survey_response (american, british) VALUES ('Yes, have had some possible symptoms but tested negative', 
                                                           'Yes, have had some possible symptoms but tested negative');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
    VALUES (212, 'Yes, have had some possible symptoms but tested negative', 4);

-- add a response as the last option to two questions
INSERT INTO ag.survey_response (american, british) VALUES ('Not applicable', 'Not applicable');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
    VALUES (226, 'Not applicable', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
    VALUES (227, 'Not applicable', 3);

-- add more responses to a few questions. the response structure is consistent 
-- so lets do it in a loop
INSERT INTO ag.survey_response (american, british) VALUES ('One or two days', 'One or two days');
DO
$do$
DECLARE
    qid integer;
BEGIN
    -- this response is specific at the time of this patch to the questions that need updating
    FOR qid IN SELECT survey_question_id FROM ag.survey_question_response WHERE response='More than half the days'
    LOOP
        -- shift all responses down in display order
        UPDATE ag.survey_question_response 
            SET display_index=5 
            WHERE survey_question_id=qid AND response='Nearly every day';
        UPDATE ag.survey_question_response 
            SET display_index=4
            WHERE survey_question_id=qid AND response='More than half the days';
        UPDATE ag.survey_question_response 
            SET display_index=3 
            WHERE survey_question_id=qid AND response='Several days per week';
        
        -- ...and insert our response
        INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
            VALUES (qid, 'One or two days', 2);
    END LOOP;
END $do$;

-- typos and response replacements

-- create a means to replace a response as this pattern will be used a few times
-- note: postgres9 does not have procedures... 
CREATE OR REPLACE FUNCTION replace_response(qid INTEGER, old_resp VARCHAR, new_resp VARCHAR) RETURNS INTEGER AS
$$
DECLARE
    didx INTEGER;
BEGIN
    SELECT display_index
        INTO didx
        FROM ag.survey_question_response
        WHERE survey_question_id=qid
            AND response=old_resp;

    INSERT INTO ag.survey_response (american, british) VALUES (new_resp, new_resp);

    INSERT INTO ag.survey_question_response
        (survey_question_id, response, display_index)
        VALUES (qid, new_resp, 999);

    UPDATE ag.survey_answers
        SET response=new_resp
        WHERE survey_question_id=qid
            AND response=old_resp;

    DELETE FROM ag.survey_question_response
        WHERE survey_question_id=qid
            AND response=old_resp;

    UPDATE ag.survey_question_response
        SET display_index=didx
        WHERE survey_question_id=qid
            AND response=new_resp; 
    
    RETURN 1;
END;
$$ LANGUAGE plpgsql;

SELECT replace_response(162, 
                'Westen-Price, or other low-grain, low processed food diet', 
                'Weston-Price, or other low-grain, low processed food diet');

SELECT replace_response(217,
                        'Put into self-quarantine without symptoms (e.g., due to possible exposure)',
                        'Put into self-quarantine without symptoms (e.g. due to possible exposure)');

SELECT replace_response(232, 'Very Satisfied', 'Very satisfied');
SELECT replace_response(232, 'Moderately Satisfied', 'Moderately satisfied');
SELECT replace_response(232, 'Very Dissatisfied', 'Very dissatisfied');

SELECT replace_response(233, 'Noticable', 'Barely noticeable');
SELECT replace_response(233, 'A Little Somewhat', 'Somewhat noticeable');
SELECT replace_response(233, 'Much', 'Quite Noticeable');
SELECT replace_response(233, 'Very Much Noticable', 'Very noticeable');

SELECT replace_response(234, 'Worried', 'A little worried');
SELECT replace_response(234, 'A Little Somewhat', 'Somewhat worried');
SELECT replace_response(234, 'Much', 'Quite worried');
SELECT replace_response(234, 'Very Much Worried', 'Very worried');

SELECT replace_response(235, 'A Little Somewhat', 'Somewhat interfering');
SELECT replace_response(235, 'Much', 'Quite interfering');
SELECT replace_response(235, 'Very Much Interfering', 'Very interfering');

-- now lets get rid of our helper function
DROP FUNCTION replace_response(qid INTEGER, old_resp VARCHAR, new_resp VARCHAR);

-- finally, create two new primary questions and one covid question
INSERT INTO ag.survey_question (survey_question_id, american, british,  question_shortname, retired) 
    VALUES (236, 
           'In an average week, how often do you consume beets (including raw, canned, pickled, or roasted)? (1 serving = 1 cup raw or cooked)',
           'In an average week, how often do you consume beets (including raw, canned, pickled, or roasted)? (1 serving = 1 cup raw or cooked)',
           'BEET_FREQUENCY', 'f');
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
    VALUES (4, 236, 24);
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type)
    VALUES (236, 'SINGLE');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Unspecified', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Never', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Rarely (less than once/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Occasionally (1-2 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Regularly (3-5 times/week)', 4);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (236, 'Daily', 5);

INSERT INTO ag.survey_question (survey_question_id, american, british,  question_shortname, retired) 
    VALUES (237, 
           'In an average week, how often do you eat various plant sources of protein including tofu, tempeh, edamame, lentils, chickpeas, peanuts, almonds, walnuts, or quinoa?',
           'In an average week, how often do you eat various plant sources of protein including tofu, tempeh, edamame, lentils, chickpeas, peanuts, almonds, walnuts, or quinoa?',
           'PLANT_PROTEIN_FREQUENCY', 'f');
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
    VALUES (4, 237, 25);
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type)
    VALUES (237, 'SINGLE');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Unspecified', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Never', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Rarely (less than once/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Occasionally (1-2 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Regularly (3-5 times/week)', 4);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (237, 'Daily', 5);

INSERT INTO ag.survey_question (survey_question_id, american, british,  question_shortname, retired) 
    VALUES (238, 
           'Have any of the following happened to you because of Coronavirus/COVID-19? (check all that apply)',
           'Have any of the following happened to you because of Coronavirus/COVID-19? (check all that apply)',
           'COVID_HAPPENED_TO_YOU', 'f');
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
    VALUES (-6, 238, 9.5);
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type)
    VALUES (238, 'MULTIPLE');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Unspecified', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Fallen ill physically', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Hospitalized', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Put into self-quarantine with symptoms', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Put into self-quarantine without symptoms (e.g. due to possible exposure)', 4);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Lost job', 5);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'Reduced ability to earn money', 6);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) 
    VALUES (238, 'None of the above', 7);
