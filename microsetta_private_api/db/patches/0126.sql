-- We need to un-retire the COVID_LEVEL_OF_WELLBEING question and add it to the General Health group
UPDATE ag.survey_question SET retired = false WHERE survey_question_id = 210;
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (-14, 210, 38);
