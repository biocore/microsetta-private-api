--November 7, 2015
--Fix typos in column shortnames
UPDATE ag.survey_question SET question_shortname = 'FROZEN_DESSERT_FREQUENCY' WHERE survey_question_id = 66;
UPDATE ag.survey_question SET question_shortname = 'OTHER_CONDITIONS_LIST' WHERE survey_question_id = 106;
