-- Retire the fabric softener question
UPDATE ag.survey_question SET retired = TRUE WHERE survey_question_id = 36;

-- Add an "I use both" option for the deodorant question
INSERT INTO ag.survey_response (american, spanish, spain_spanish) VALUES ('I use both', 'Yo uso ambos', 'Yo uso ambos');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (34, 'I use both', 5);

-- Re-word the question about surfing
UPDATE ag.survey_question
    SET american = 'Do you swim, surf, snorkel, or do other activities where you are in the ocean on a regular basis?',
        spanish = '¿Usted nada, surfea, practica esnórquel o realiza otras actividades en el mar con regularidad?',
        spain_spanish = '¿Usted nada, surfea, practica esnórquel o realiza otras actividades en el mar con regularidad?'
    WHERE survey_question_id = 354;

-- Add "Other" option to types of exercise
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (331, 'Other', 5);

-- Add "None of the above" option to COVID symptoms question
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (214, 'None of the above', 17);

-- Add missing note to question about non-nutritive sweeteners
UPDATE ag.survey_question
    SET american = 'How often do you consume beverages with non-nutritive or low-calorie sweeteners? This includes sugar alcohols (sorbitol, mannitol, maltitol, xylitol, reduced palatinose, erythritol), synthetic sweeteners (saccharin, aspartame, acesulfame potassium, sucralose), and sugar substitutes (stevia, monk fruit).',
        spanish = '¿Con qué frecuencia consume bebidas con edulcorantes no nutritivos o bajos en calorías? Esto incluye los alcoholes de azúcar (sorbitol, manitol, maltitol, xilitol, palatinosa reducida, eritritol), edulcorantes sintéticos (sacarina, aspartamo, acesulfamo de potasio, sucralosa) y sustitutos del azúcar (stevia, fruta del monje).',
        spain_spanish = '¿Con qué frecuencia consume bebidas con edulcorantes no nutritivos o bajos en calorías? Esto incluye los alcoholes de azúcar (sorbitol, manitol, maltitol, xilitol, palatinosa reducida, eritritol), edulcorantes sintéticos (sacarina, aspartamo, acesulfamo de potasio, sucralosa) y sustitutos del azúcar (stevia, fruta del monje).'
    WHERE survey_question_id = 157;

-- Stop "Rarely" response from triggering fermented foods sub-questions
DELETE FROM ag.survey_question_triggers WHERE survey_question_id = 165 AND triggering_response = 'Rarely (a few times/month)';

-- Move questions about producing fermented foods out of triggers
DELETE FROM ag.survey_question_triggers WHERE triggered_question IN (169, 171);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox' WHERE survey_question_id IN (169, 171);

-- Add "I don't produce fermented foods" option to both production questions
INSERT INTO ag.survey_response (american, spanish, spain_spanish) VALUES ('I do not produce fermented foods', 'No produzco alimentos fermentados', 'No produzco alimentos fermentados');
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (169, 'I do not produce fermented foods', 22);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (171, 'I do not produce fermented foods', 22);

-- Trigger fermented foods increase/frequency questions based on whether user consumes fermented foods
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
    VALUES (478, 'Since infancy/childhood', 166),
            (478, 'Within the last year', 166),
            (478, 'Within the last 5 years', 166),
            (478, 'Within the last 10 years', 166),
            (478, 'Since infancy/childhood', 165),
            (478, 'Within the last year', 165),
            (478, 'Within the last 5 years', 165),
            (478, 'Within the last 10 years', 165);

-- Update fermented foods increase/frequency questions' css classes to include "tmi-survey-triggered-question"
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis tmi-survey-triggered-question' WHERE survey_question_id = 165;
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id = 166;

-- Fix triggering sequence for non-nutritive food/beverage question sequence
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
    VALUES (157, 'Rarely (a few times/month)', 465),
            (157, 'Occasionally (1-2 times/week)', 465),
            (157, 'Regularly (3-5 times/week)', 465),
            (157, 'Daily', 465),
            (463, 'Rarely (a few times/month)', 465),
            (463, 'Occasionally (1-2 times/week)', 465),
            (463, 'Regularly (3-5 times/week)', 465),
            (463, 'Daily', 465),
            (465, 'Yes', 466);

-- Un-retire the "other" questions for fermented foods consumed and produced, then reorganize sequencing to fit them in to the Detailed Diet survey (survey_group -18)
UPDATE ag.survey_question SET retired = FALSE, css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (168, 170, 172);
DELETE FROM ag.group_questions WHERE survey_group = -10 AND survey_question_id IN (168, 170, 172);
UPDATE ag.group_questions SET display_index = 50 WHERE survey_group = -18 AND survey_question_id = 171;
UPDATE ag.group_questions SET display_index = 48 WHERE survey_group = -18 AND survey_question_id = 169;
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
    VALUES (-18, 168, 47),
            (-18, 170, 49),
            (-18, 172, 51);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
    VALUES (167, 'Other', 168),
            (169, 'Other', 170),
            (171, 'Other', 172);

-- Fix formatting for cancer diagnosis question
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id = 507;

-- As part of the Daklapack API specs, the TMI account that orders a kit will appear on the label in the companyName field.
-- We're going to set our fulfillment account's name to Microsetta Initiative to be as descriptive and professional as possible.
-- In the long term, it would be good to see if we can discontinue use of this field.
UPDATE ag.account SET first_name = 'Microsetta', last_name = 'Initiative' WHERE id = '000fc4cd-8fa4-db8b-e050-8a800c5d81b7';
