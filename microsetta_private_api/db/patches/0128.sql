-- The "Yes, I use a copper IUD" response needs to read as "No, I use a copper IUD" as copper IUD is not hormonal.
-- Since adding that option was part of the overhaul and no one has had the opportunity to actually select it,
-- we can safely change this without breaking foreign keys on existing survey responses.
DELETE FROM ag.survey_question_response WHERE survey_question_id = 497 AND response = 'Yes, I use a copper IUD';
UPDATE ag.survey_response SET american = 'No, I use a copper IUD', spanish = 'No, uso un DIU de cobre', spain_spanish = 'No, uso un DIU de cobre' WHERE american = 'Yes, I use a copper IUD';
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (497, 'No, I use a copper IUD', 6);

-- Change questions about sleep problems to trigger off of sleep quality question
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis tmi-survey-triggered-question' WHERE survey_question_id IN (233, 234, 235);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
    VALUES (232, 'Moderately satisfied', 233),
            (232, 'Dissatisfied', 233),
            (232, 'Very dissatisfied', 233),
            (232, 'Moderately satisfied', 234),
            (232, 'Dissatisfied', 234),
            (232, 'Very dissatisfied', 234),
            (232, 'Moderately satisfied', 235),
            (232, 'Dissatisfied', 235),
            (232, 'Very dissatisfied', 235);
