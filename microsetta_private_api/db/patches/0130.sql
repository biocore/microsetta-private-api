-- Update campaign association for Fundrazr transactions to point to internal TMI campaign rather than AGP
UPDATE campaign.transaction_source_to_campaign
SET internal_campaign_id = (
    SELECT campaign_id FROM campaign.campaigns WHERE title = 'The Microsetta Initiative'
)
WHERE remote_campaign_id = '4Tqx5';

-- Update Rob's phone number in consent documents. We're not creating a new version of the consent docs as it's not a material change of terms
UPDATE ag.consent_documents SET consent_content = REPLACE(consent_content, '858-246-1184', '858-822-2379');

-- Add comma to oxalate-rich foods question
UPDATE ag.survey_question SET american = 'How often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, watermelon, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?' WHERE survey_question_id = 243;

-- Add "More than 10 years ago" response to fermented foods question
INSERT INTO ag.survey_response (american, spanish, spain_spanish) VALUES ('More than 10 years ago', 'Hace más de 10 años', 'Hace más de 10 años');
UPDATE ag.survey_question_response SET display_index = 6 WHERE survey_question_id = 478 AND response = 'I do not eat fermented foods';
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (478, 'More than 10 years ago', 5);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (478, 'More than 10 years ago', 165);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (478, 'More than 10 years ago', 166);

-- Trigger question 37c off of 37 rather than 37b
DELETE FROM ag.survey_question_triggers WHERE survey_question_id = 165 AND triggered_question = 167;
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
    VALUES (478, 'Since infancy/childhood', 167),
           (478, 'Within the last year', 167),
           (478, 'Within the last 5 years', 167),
           (478, 'Within the last 10 years', 167),
           (478, 'More than 10 years ago', 167);

-- Fix height/weight unit questions on mobile
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text col-12 col-md-2' WHERE survey_question_id IN (108, 113);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-switch col-12 col-md-4' WHERE survey_question_id IN (109, 114);

-- Adjust Spanish translations of various questions/responses
UPDATE ag.survey_question SET spanish = '¿Se muerde las uñas?', spain_spanish = '¿Se muerde las uñas?' WHERE survey_question_id = 26;
UPDATE ag.survey_question SET spanish = 'Me han puesto la vacuna de la influenza en los últimos ____________.', spain_spanish = 'Me han puesto la vacuna de la influenza en los últimos ____________.' WHERE survey_question_id = 40;
UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana cocina y come comidas caseras? (Excluya las comidas listas para consumir, como los macarrones con queso en caja, las sopas instantáneas o los alimentos de Lean Cuisine)', spain_spanish = 'Por lo general, ¿cuántas veces a la semana cocina y come comidas caseras? (Excluya las comidas listas para consumir, como los macarrones con queso en caja, las sopas instantáneas o los alimentos de Lean Cuisine)' WHERE survey_question_id = 57;
UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana come alimentos listos para consumir (p. ej., macarrones con queso, sopas instantáneas o alimentos de Lean Cuisine)?', spain_spanish = 'Por lo general, ¿cuántas veces a la semana come alimentos listos para consumir (p. ej., macarrones con queso, sopas instantáneas o alimentos de Lean Cuisine)?' WHERE survey_question_id = 58;
UPDATE ag.survey_question SET spanish = 'En una semana promedio, ¿cuántos alimentos derivados de plantas consume? Por ejemplo, si consume una sopa que contiene zanahorias, papas y cebolla, puede contar esto como 3 alimentos derivados de plantas. Si consume pan multigrano, cada grano cuenta como un alimento derivado de plantas. Cada fruta también cuenta como un alimento derivado de plantas.', spain_spanish = 'En una semana promedio, ¿cuántos alimentos derivados de plantas consume? Por ejemplo, si consume una sopa que contiene zanahorias, papas y cebolla, puede contar esto como 3 alimentos derivados de plantas. Si consume pan multigrano, cada grano cuenta como un alimento derivado de plantas. Cada fruta también cuenta como un alimento derivado de plantas.' WHERE survey_question_id = 146;
UPDATE ag.survey_response SET spanish = 'Estreñimiento', spain_spanish = 'Estreñimiento' WHERE american = 'Constipation';
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha u hojas de remolacha, okra, quinoa, amaranto, trigo sarraceno, salvado o germen de trigo, cereal de salvado, semillas de chía, ruibarbo, sandía, chocolate negro o cacao en polvo? (>70 %) y frutos secos como almendras, cacahuetes, nueces, anacardos y avellanas?', spain_spanish = '¿Con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha u hojas de remolacha, okra, quinoa, amaranto, trigo sarraceno, salvado o germen de trigo, cereal de salvado, semillas de chía, ruibarbo, sandía, chocolate negro o cacao en polvo? (>70 %) y frutos secos como almendras, cacahuetes, nueces, anacardos y avellanas?' WHERE survey_question_id = 243;
UPDATE ag.survey_question SET spanish = '¿Cuántas veces se ha contagiado de Coronavirus/COVID-19?', spain_spanish = '¿Cuántas veces se ha contagiado de Coronavirus/COVID-19?' WHERE survey_question_id = 521;

