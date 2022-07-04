INSERT INTO ag.survey_group (group_order, american, british, spanish) VALUES (-7, 'Cooking Oils and Oxalate-rich Foods', 'Cooking Oils and Oxalate-rich Foods', 'Aceites de cocina y alimentos ricos en oxalatos');

INSERT INTO ag.surveys (survey_id, survey_group) VALUES (7, -7);

-- Ignoring the french and chinese columns as those languages are unused right now
INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, spanish) VALUES
(239, 'In a given week, how often do you use or cook with vegetable oils (excluding coconut and palm oil) such as corn, soy, canola (rapeseed), olive, peanut, avocado, safflower or sunflower?', 'In a given week, how often do you use or cook with vegetable oils (excluding coconut and palm oil) such as corn, soy, canola (rapeseed), olive, peanut, avocado, safflower or sunflower?', 'OILS_FREQUENCY_VEGETABLE', 'En una semana determinada, ¿con qué frecuencia usa o cocina con aceites vegetales (excluyendo aceite de coco y palma) como maíz, soya, canola (colza), oliva, maní, aguacate, cártamo o girasol?'),
(240, 'In a given week, how often do you use or cook with lard, butter or ghee?', 'In a given week, how often do you use or cook with lard, butter or ghee?', 'OILS_FREQUENCY_ANIMAL', 'En una semana determinada, ¿con qué frecuencia usa o cocina con manteca de cerdo, mantequilla o ghee (mantequilla clarificada)?'),
(241, 'In a given week, how often do you use or cook with coconut, palm or palm kernel oil?', 'In a given week, how often do you use or cook with coconut, palm or palm kernel oil?', 'OILS_FREQUENCY_OTHER', 'En una semana determinada, ¿con qué frecuencia usa o cocina con aceite de coco, palma o palmiste?'),
(242, 'In a given week, how often do you use or cook with margarine or (vegetable) shortening?', 'In a given week, how often do you use or cook with margarine or (vegetable) shortening?', 'OILS_FREQUENCY_MARGARINE', 'En una semana determinada, ¿con qué frecuencia usa o cocina con margarina o manteca (vegetal)?'),
(243, 'On average, how often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?', 'On average, how often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?', 'OILS_FREQUENCY_OXALATE', 'En promedio, ¿con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha o hojas de remolacha, okra, quinoa, amaranto, trigo sarraceno, salvado o germen de trigo, cereales de salvado, semillas de chía, ruibarbo, chocolate negro o cacao en polvo (>70 %) y frutos secos como almendras, cacahuates, pecanas, anacardos y avellanas?'),
(244, 'In a given week, how often do you consume soy products such as textured vegetable protein, tofu, tempeh, soybean flour, soy nuts, soy butter, soybeans, and miso (i.e. fermented soy)?', 'In a given week, how often do you consume soy products such as textured vegetable protein, tofu, tempeh, soybean flour, soy nuts, soy butter, soybeans, and miso (i.e. fermented soy)?', 'OILS_FREQUENCY_SOY', 'En una semana determinada, ¿con qué frecuencia consume productos de soya como proteína vegetal texturizada, tofu, tempeh, harina de soya, nueces de soya, mantequilla de soya, granos de soya y miso (soya fermentada)?');

INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES
(-7, 239, 0),
(-7, 240, 1),
(-7, 241, 2),
(-7, 242, 3),
(-7, 243, 4),
(-7, 244, 5);

INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type) VALUES
(239, 'SINGLE'),
(240, 'SINGLE'),
(241, 'SINGLE'),
(242, 'SINGLE'),
(243, 'SINGLE'),
(244, 'SINGLE');

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(239, 'Unspecified', 0),
(239, 'Never', 1),
(239, 'Rarely (a few times/month)', 2),
(239, 'Occasionally (1-2 times/week)', 3),
(239, 'Regularly (3-5 times/week)', 4),
(239, 'Daily', 5);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(240, 'Unspecified', 0),
(240, 'Never', 1),
(240, 'Rarely (a few times/month)', 2),
(240, 'Occasionally (1-2 times/week)', 3),
(240, 'Regularly (3-5 times/week)', 4),
(240, 'Daily', 5);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(241, 'Unspecified', 0),
(241, 'Never', 1),
(241, 'Rarely (a few times/month)', 2),
(241, 'Occasionally (1-2 times/week)', 3),
(241, 'Regularly (3-5 times/week)', 4),
(241, 'Daily', 5);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(242, 'Unspecified', 0),
(242, 'Never', 1),
(242, 'Rarely (a few times/month)', 2),
(242, 'Occasionally (1-2 times/week)', 3),
(242, 'Regularly (3-5 times/week)', 4),
(242, 'Daily', 5);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(243, 'Unspecified', 0),
(243, 'Never', 1),
(243, 'Rarely (a few times/month)', 2),
(243, 'Occasionally (1-2 times/week)', 3),
(243, 'Regularly (3-5 times/week)', 4),
(243, 'Daily', 5);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
(244, 'Unspecified', 0),
(244, 'Never', 1),
(244, 'Rarely (a few times/month)', 2),
(244, 'Occasionally (1-2 times/week)', 3),
(244, 'Regularly (3-5 times/week)', 4),
(244, 'Daily', 5);
