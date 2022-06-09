INSERT INTO ag.survey_group (group_order, american, british, spanish) VALUES (6, 'cooking oils and oxalate-rich foods', 'cooking oils and oxalate-rich foods', 'aceites de cocina y alimentos ricos en oxalatos');

INSERT INTO ag.surveys (survey_id, survey_group) VALUES (7, 6);

INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (239, 
'In a given week, how often do you use or cook with vegetable oils (excluding coconut and palm oil) such as corn, soy, canola (rapeseed), olive, peanut, avocado, safflower or sunflower?',
'In a given week, how often do you use or cook with vegetable oils (excluding coconut and palm oil) such as corn, soy, canola (rapeseed), olive, peanut, avocado, safflower or sunflower?',
'OILS_FREQUENCY_VEGETABLE',
'false',
'En una semana determinada, ¿con qué frecuencia usa o cocina con aceites vegetales (excluyendo aceite de coco y palma) como maíz, soya, canola (colza), oliva, maní, aguacate, cártamo o girasol?',
'Au cours d''une semaine donnée, à quelle fréquence utilisez-vous ou cuisinez-vous avec des huiles végétales (à l''exclusion de l''huile de coco et de palme) telles que le maïs, le soja, le canola (colza), l''olive, l''arachide, l''avocat, le carthame ou le tournesol ?',
'在给定的一周内，您使用植物油（不包括椰子油和棕榈油）如玉米、大豆、油菜（油菜籽）、橄榄、花生、鳄梨、红花或向日葵的频率如何？');


INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (240,
'In a given week, how often do you use or cook with lard, butter or ghee?',
'In a given week, how often do you use or cook with lard, butter or ghee?',
'OILS_FREQUENCY_BUTTER',
'false',
'En una semana determinada, ¿con qué frecuencia usa o cocina con manteca de cerdo, mantequilla o manteca?',
'Au cours d''une semaine donnée, à quelle fréquence utilisez-vous ou cuisinez-vous avec du saindoux, du beurre ou du ghee ?',
'在给定的一周内，您使用猪油、黄油或酥油烹饪或烹饪的频率如何');


INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (241,
'In a given week, how often do you use or cook with coconut, palm or palm kernel oil?',
'In a given week, how often do you use or cook with coconut, palm or palm kernel oil?',
'OILS_FREQUENCY_OTHEROILS',
'false',
'En una semana determinada, ¿con qué frecuencia usa o cocina con aceite de coco, palma o palmiste?',
'Au cours d''une semaine donnée, à quelle fréquence utilisez-vous ou cuisinez-vous avec de l''huile de noix de coco, de palme ou de palmiste ?',
'在给定的一周内，您使用椰子油、棕榈油或棕榈仁油的频率如何');


INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (242,
'In a given week, how often do you use or cook with margarine or (vegetable) shortening?',
'In a given week, how often do you use or cook with margarine or (vegetable) shortening?',
'OILS_FREQUENCY_MARGARIN',
'false',
'En una semana determinada, ¿con qué frecuencia usa o cocina con margarina o manteca (vegetal)?',
'Au cours d''une semaine donnée, à quelle fréquence utilisez-vous ou cuisinez-vous avec de la margarine ou du shortening (végétal) ?',
'在给定的一周内，您使用或烹饪人造黄油或（植物）起酥油的频率如何');


INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (243,
'On average, how often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?',
'On average, how often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?',
'OILS_FREQUENCY_OXALATE',
'false',
'En promedio, ¿con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha o hojas de remolacha, okra, quinua, amaranto, trigo sarraceno, salvado o germen de trigo, cereales de salvado, semillas de chía, ruibarbo, chocolate negro o cacao? polvo (>70%) y frutos secos como almendras, cacahuetes, pecanas, anacardos y avellanas?',
'En moyenne, à quelle fréquence consommez-vous des aliments riches en oxalate, tels que les épinards, la bette à carde, la betterave ou les feuilles de betterave, le gombo, le quinoa, l''amarante, le sarrasin, le son ou le germe de blé, les céréales de son, les graines de chia, la rhubarbe, le chocolat noir ou le cacao poudre (>70 %) et des noix comme les amandes, les cacahuètes, les noix de pécan, les noix de cajou et les noisettes ?',
'平均而言，您多久食用一次富含草酸盐的食物，例如菠菜、瑞士甜菜、甜菜根或甜菜、秋葵、藜麦、苋菜、荞麦、麦麸或胚芽、麸麦片、奇亚籽、大黄、黑巧克力或可可粉末 (>70%) 和坚果，如杏仁、花生、山核桃、腰果和榛子？');


INSERT INTO ag.survey_question (survey_question_id, american, british, question_shortname, retired, spanish, french, chinese) 
VALUES (244,
'In a given week, how often do you consume soy products such as textured vegetable protein, tofu, tempeh, soybean flour, soy nuts, soy butter, soybeans, and miso (i.e. fermented soy)?',
'In a given week, how often do you consume soy products such as textured vegetable protein, tofu, tempeh, soybean flour, soy nuts, soy butter, soybeans, and miso (i.e. fermented soy)?',
'OILS_FREQUENCY_SOY',
'false',
'En una semana determinada, ¿con qué frecuencia consume productos de soja como proteína vegetal texturizada, tofu, tempeh, harina de soja, nueces de soja, mantequilla de soja, soja y miso (es decir, soja fermentada)?',
'Au cours d''une semaine donnée, à quelle fréquence consommez-vous des produits à base de soja tels que des protéines végétales texturées, du tofu, du tempeh, de la farine de soja, des noix de soja, du beurre de soja, des graines de soja et du miso (c''est-à-dire du soja fermenté) ?',
'在给定的一周内，您多久食用一次豆制品，例如质地植物蛋白、豆腐、豆豉、大豆粉、大豆坚果、大豆黄油、大豆和味噌（即发酵大豆）？');


INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 239, 1000);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 240, 1001);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 241, 1002);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 242, 1003);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 243, 1004);
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (6, 244, 1005);


INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (239, 'SINGLE');
INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (240, 'SINGLE');
INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (241, 'SINGLE');
INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (242, 'SINGLE');
INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (243, 'SINGLE');
INSERT INTO ag.survey_question_response_type(survey_question_id, survey_response_type) VALUES (244, 'SINGLE');

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (239, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (239, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (239, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (239, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (239, 'Daily', 4);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (240, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (240, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (240, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (240, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (240, 'Daily', 4);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (241, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (241, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (241, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (241, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (241, 'Daily', 4);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (242, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (242, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (242, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (242, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (242, 'Daily', 4);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (243, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (243, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (243, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (243, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (243, 'Daily', 4);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (244, 'Never', 0);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (244, 'Rarely (less than once/week)', 1);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (244, 'Occasionally (1-2 times/week)', 2);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (244, 'Regularly (3-5 times/week)', 3);
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (244, 'Daily', 4);

