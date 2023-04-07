-- Add sleep-related questions to the end of the General Lifestyle and Hygiene Information section
-- Create the questions
INSERT INTO ag.survey_question (survey_question_id, american, question_shortname, retired, spanish, spain_spanish, japanese)
VALUES
    (344, 'On days you have school or work, what time do you get up in the morning?', 'WEEKDAY_WAKE_TIME', FALSE, 'En los días que tiene escuela o trabajo, ¿a qué hora se levanta por la mañana?', 'En los días que tiene escuela o trabajo, ¿a qué hora se levanta por la mañana?', '学校や仕事がある日は、朝何時に起きますか？'),
    (345, 'On nights before you have school or work, what time do you go to bed?', 'WEEKDAY_SLEEP_TIME', FALSE, 'En las noches antes de ir a la escuela o al trabajo, ¿a qué hora se acuesta?', 'En las noches antes de ir a la escuela o al trabajo, ¿a qué hora se acuesta?', '学校や仕事がある前の夜は、何時に寝ますか？'),
    (346, 'On your off days (days when you do not have school or work), what time do you get up in the morning?', 'WEEKEND_WAKE_TIME', FALSE, 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se levanta por la mañana?', 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se levanta por la mañana?', '休みの日（学校や仕事がない日）は、朝何時に起きますか？'),
    (347, 'On nights before your off days (days when you do not have school or work), what time do you go to bed?', 'WEEKEND_SLEEP_TIME', FALSE, 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se acuesta?', 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se acuesta?', '休みの日（学校や仕事がない日）の前の夜は、何時に寝ますか？'),
    (348, 'Do you have a job or some other situation that requires you to work and sleep during atypical hours (e.g. work between 10pm-6am and sleep between 9am-5pm)?', 'ATYPICAL_SLEEP_TIME', FALSE, '¿Tiene un trabajo o alguna otra situación que requiera que trabaje y duerma en horarios atípicos (por ejemplo, trabaje entre las 10 pm y las 6 am y duerma entre las 9 am y las 5 pm)?', '¿Tiene un trabajo o alguna otra situación que requiera que trabaje y duerma en horarios atípicos (por ejemplo, trabaje entre las 10 pm y las 6 am y duerma entre las 9 am y las 5 pm)?', '不規則な時間帯に仕事や睡眠を必要とする仕事やその他の状況がありますか（午後10時～午前6時に仕事して、午前9時～午後5時に睡眠をとるなど）？'),
    (349, 'If you use light emitting electronic devices such as a phone or laptop right before bed, do you use it in night or dark mode?', 'DARK_MODE_ON', FALSE, 'Si usa dispositivos electrónicos que emiten luz, como un teléfono o una computadora portátil, justo antes de acostarse, ¿los usa en modo nocturno u oscuro?', 'Si usa dispositivos electrónicos que emiten luz, como un teléfono o una computadora portátil, justo antes de acostarse, ¿los usa en modo nocturno u oscuro?', '電話やノートパソコンなどの発光電子機器を寝る直前に使用する場合、ナイトモードまたはダークモードで使用していますか？'),
    (350, 'Over the past week, how would you rate your sleep quality?', 'SLEEP_QUALITY', FALSE, 'Durante la última semana, ¿cómo calificaría la calidad de su sueño?', 'Durante la última semana, ¿cómo calificaría la calidad de su sueño?', '過去1週間の睡眠の質はどんなでしたか？');

-- Set the question types
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type)
VALUES
    (344, 'SINGLE'),
    (345, 'SINGLE'),
    (346, 'SINGLE'),
    (347, 'SINGLE'),
    (348, 'SINGLE'),
    (349, 'SINGLE'),
    (350, 'SINGLE');

-- Associate them with the group
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
VALUES
    (2, 344, 13),
    (2, 345, 14),
    (2, 346, 15),
    (2, 347, 16),
    (2, 348, 17),
    (2, 349, 18),
    (2, 350, 19);

-- Create the responses we'll need for the questions
INSERT INTO ag.survey_response (american, spanish, spain_spanish, japanese)
VALUES
    ('10:00AM', '10:00AM', '10:00AM', '10:00午前'),
    ('10:00PM', '10:00PM', '10:00PM', '10:00午後'),
    ('10:30AM', '10:30AM', '10:30AM', '10:30午前'),
    ('10:30PM', '10:30PM', '10:30PM', '10:30午後'),
    ('11:00AM', '11:00AM', '11:00AM', '11:00午前'),
    ('11:00PM', '11:00PM', '11:00PM', '11:00午後'),
    ('11:30AM', '11:30AM', '11:30AM', '11:30午前'),
    ('11:30PM', '11:30PM', '11:30PM', '11:30午後'),
    ('12:00AM', '12:00AM', '12:00AM', '12:00午前'),
    ('12:00PM', '12:00PM', '12:00PM', '12:00午後'),
    ('12:30AM', '12:30AM', '12:30AM', '12:30午前'),
    ('12:30PM', '12:30PM', '12:30PM', '12:30午後'),
    ('1:00AM', '1:00AM', '1:00AM', '1:00午前'),
    ('1:00PM', '1:00PM', '1:00PM', '1:00午後'),
    ('1:30AM', '1:30AM', '1:30AM', '1:30午前'),
    ('1:30PM', '1:30PM', '1:30PM', '1:30午後'),
    ('2:00AM', '2:00AM', '2:00AM', '2:00午前'),
    ('2:00PM', '2:00PM', '2:00PM', '2:00午後'),
    ('2:30AM', '2:30AM', '2:30AM', '2:30午前'),
    ('2:30PM', '2:30PM', '2:30PM', '2:30午後'),
    ('3:00AM', '3:00AM', '3:00AM', '3:00午前'),
    ('3:00PM', '3:00PM', '3:00PM', '3:00午後'),
    ('3:30AM', '3:30AM', '3:30AM', '3:30午前'),
    ('3:30PM', '3:30PM', '3:30PM', '3:30午後'),
    ('4:00AM', '4:00AM', '4:00AM', '4:00午前'),
    ('4:00PM', '4:00PM', '4:00PM', '4:00午後'),
    ('4:30AM', '4:30AM', '4:30AM', '4:30午前'),
    ('4:30PM', '4:30PM', '4:30PM', '4:30午後'),
    ('5:00AM', '5:00AM', '5:00AM', '5:00午前'),
    ('5:00PM', '5:00PM', '5:00PM', '5:00午後'),
    ('5:30AM', '5:30AM', '5:30AM', '5:30午前'),
    ('5:30PM', '5:30PM', '5:30PM', '5:30午後'),
    ('6:00AM', '6:00AM', '6:00AM', '6:00午前'),
    ('6:00PM', '6:00PM', '6:00PM', '6:00午後'),
    ('6:30AM', '6:30AM', '6:30AM', '6:30午前'),
    ('6:30PM', '6:30PM', '6:30PM', '6:30午後'),
    ('7:00AM', '7:00AM', '7:00AM', '7:00午前'),
    ('7:00PM', '7:00PM', '7:00PM', '7:00午後'),
    ('7:30AM', '7:30AM', '7:30AM', '7:30午前'),
    ('7:30PM', '7:30PM', '7:30PM', '7:30午後'),
    ('8:00AM', '8:00AM', '8:00AM', '8:00午前'),
    ('8:00PM', '8:00PM', '8:00PM', '8:00午後'),
    ('8:30AM', '8:30AM', '8:30AM', '8:30午前'),
    ('8:30PM', '8:30PM', '8:30PM', '8:30午後'),
    ('9:00AM', '9:00AM', '9:00AM', '9:00午前'),
    ('9:00PM', '9:00PM', '9:00PM', '9:00午後'),
    ('9:30AM', '9:30AM', '9:30AM', '9:30午前'),
    ('9:30PM', '9:30PM', '9:30PM', '9:30午後'),
    ('I do not use these devices before bed', 'No uso estos dispositivos antes de acostarme.', 'No uso estos dispositivos antes de acostarme.', '寝る直前にこれらの機器は使用していません。');

-- Associate responses with questions
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
VALUES
    (344, 'Unspecified', 0),
    (344, '12:00AM', 1),
    (344, '12:30AM', 2),
    (344, '1:00AM', 3),
    (344, '1:30AM', 4),
    (344, '2:00AM', 5),
    (344, '2:30AM', 6),
    (344, '3:00AM', 7),
    (344, '3:30AM', 8),
    (344, '4:00AM', 9),
    (344, '4:30AM', 10),
    (344, '5:00AM', 11),
    (344, '5:30AM', 12),
    (344, '6:00AM', 13),
    (344, '6:30AM', 14),
    (344, '7:00AM', 15),
    (344, '7:30AM', 16),
    (344, '8:00AM', 17),
    (344, '8:30AM', 18),
    (344, '9:00AM', 19),
    (344, '9:30AM', 20),
    (344, '10:00AM', 21),
    (344, '10:30AM', 22),
    (344, '11:00AM', 23),
    (344, '11:30AM', 24),
    (344, '12:00PM', 25),
    (344, '12:30PM', 26),
    (344, '1:00PM', 27),
    (344, '1:30PM', 28),
    (344, '2:00PM', 29),
    (344, '2:30PM', 30),
    (344, '3:00PM', 31),
    (344, '3:30PM', 32),
    (344, '4:00PM', 33),
    (344, '4:30PM', 34),
    (344, '5:00PM', 35),
    (344, '5:30PM', 36),
    (344, '6:00PM', 37),
    (344, '6:30PM', 38),
    (344, '7:00PM', 39),
    (344, '7:30PM', 40),
    (344, '8:00PM', 41),
    (344, '8:30PM', 42),
    (344, '9:00PM', 43),
    (344, '9:30PM', 44),
    (344, '10:00PM', 45),
    (344, '10:30PM', 46),
    (344, '11:00PM', 47),
    (344, '11:30PM', 48),
    (345, 'Unspecified', 0),
    (345, '12:00AM', 1),
    (345, '12:30AM', 2),
    (345, '1:00AM', 3),
    (345, '1:30AM', 4),
    (345, '2:00AM', 5),
    (345, '2:30AM', 6),
    (345, '3:00AM', 7),
    (345, '3:30AM', 8),
    (345, '4:00AM', 9),
    (345, '4:30AM', 10),
    (345, '5:00AM', 11),
    (345, '5:30AM', 12),
    (345, '6:00AM', 13),
    (345, '6:30AM', 14),
    (345, '7:00AM', 15),
    (345, '7:30AM', 16),
    (345, '8:00AM', 17),
    (345, '8:30AM', 18),
    (345, '9:00AM', 19),
    (345, '9:30AM', 20),
    (345, '10:00AM', 21),
    (345, '10:30AM', 22),
    (345, '11:00AM', 23),
    (345, '11:30AM', 24),
    (345, '12:00PM', 25),
    (345, '12:30PM', 26),
    (345, '1:00PM', 27),
    (345, '1:30PM', 28),
    (345, '2:00PM', 29),
    (345, '2:30PM', 30),
    (345, '3:00PM', 31),
    (345, '3:30PM', 32),
    (345, '4:00PM', 33),
    (345, '4:30PM', 34),
    (345, '5:00PM', 35),
    (345, '5:30PM', 36),
    (345, '6:00PM', 37),
    (345, '6:30PM', 38),
    (345, '7:00PM', 39),
    (345, '7:30PM', 40),
    (345, '8:00PM', 41),
    (345, '8:30PM', 42),
    (345, '9:00PM', 43),
    (345, '9:30PM', 44),
    (345, '10:00PM', 45),
    (345, '10:30PM', 46),
    (345, '11:00PM', 47),
    (345, '11:30PM', 48),
    (346, 'Unspecified', 0),
    (346, '12:00AM', 1),
    (346, '12:30AM', 2),
    (346, '1:00AM', 3),
    (346, '1:30AM', 4),
    (346, '2:00AM', 5),
    (346, '2:30AM', 6),
    (346, '3:00AM', 7),
    (346, '3:30AM', 8),
    (346, '4:00AM', 9),
    (346, '4:30AM', 10),
    (346, '5:00AM', 11),
    (346, '5:30AM', 12),
    (346, '6:00AM', 13),
    (346, '6:30AM', 14),
    (346, '7:00AM', 15),
    (346, '7:30AM', 16),
    (346, '8:00AM', 17),
    (346, '8:30AM', 18),
    (346, '9:00AM', 19),
    (346, '9:30AM', 20),
    (346, '10:00AM', 21),
    (346, '10:30AM', 22),
    (346, '11:00AM', 23),
    (346, '11:30AM', 24),
    (346, '12:00PM', 25),
    (346, '12:30PM', 26),
    (346, '1:00PM', 27),
    (346, '1:30PM', 28),
    (346, '2:00PM', 29),
    (346, '2:30PM', 30),
    (346, '3:00PM', 31),
    (346, '3:30PM', 32),
    (346, '4:00PM', 33),
    (346, '4:30PM', 34),
    (346, '5:00PM', 35),
    (346, '5:30PM', 36),
    (346, '6:00PM', 37),
    (346, '6:30PM', 38),
    (346, '7:00PM', 39),
    (346, '7:30PM', 40),
    (346, '8:00PM', 41),
    (346, '8:30PM', 42),
    (346, '9:00PM', 43),
    (346, '9:30PM', 44),
    (346, '10:00PM', 45),
    (346, '10:30PM', 46),
    (346, '11:00PM', 47),
    (346, '11:30PM', 48),
    (347, 'Unspecified', 0),
    (347, '12:00AM', 1),
    (347, '12:30AM', 2),
    (347, '1:00AM', 3),
    (347, '1:30AM', 4),
    (347, '2:00AM', 5),
    (347, '2:30AM', 6),
    (347, '3:00AM', 7),
    (347, '3:30AM', 8),
    (347, '4:00AM', 9),
    (347, '4:30AM', 10),
    (347, '5:00AM', 11),
    (347, '5:30AM', 12),
    (347, '6:00AM', 13),
    (347, '6:30AM', 14),
    (347, '7:00AM', 15),
    (347, '7:30AM', 16),
    (347, '8:00AM', 17),
    (347, '8:30AM', 18),
    (347, '9:00AM', 19),
    (347, '9:30AM', 20),
    (347, '10:00AM', 21),
    (347, '10:30AM', 22),
    (347, '11:00AM', 23),
    (347, '11:30AM', 24),
    (347, '12:00PM', 25),
    (347, '12:30PM', 26),
    (347, '1:00PM', 27),
    (347, '1:30PM', 28),
    (347, '2:00PM', 29),
    (347, '2:30PM', 30),
    (347, '3:00PM', 31),
    (347, '3:30PM', 32),
    (347, '4:00PM', 33),
    (347, '4:30PM', 34),
    (347, '5:00PM', 35),
    (347, '5:30PM', 36),
    (347, '6:00PM', 37),
    (347, '6:30PM', 38),
    (347, '7:00PM', 39),
    (347, '7:30PM', 40),
    (347, '8:00PM', 41),
    (347, '8:30PM', 42),
    (347, '9:00PM', 43),
    (347, '9:30PM', 44),
    (347, '10:00PM', 45),
    (347, '10:30PM', 46),
    (347, '11:00PM', 47),
    (347, '11:30PM', 48),
    (348, 'Unspecified', 0),
    (348, 'Yes', 1),
    (348, 'No', 2),
    (349, 'Unspecified', 0),
    (349, 'Yes', 1),
    (349, 'No', 2),
    (349, 'I do not use these devices before bed', 3),
    (350, 'Unspecified', 0),
    (350, 'Very poor', 1),
    (350, 'Poor', 2),
    (350, 'Fair', 3),
    (350, 'Good', 4),
    (350, 'Very good', 5);

-- Add artificial sweetener questions to Detailed Dietary Information section
-- Create the questions
INSERT INTO ag.survey_question (survey_question_id, american, question_shortname, retired, spanish, spain_spanish, japanese)
VALUES
    (463, 'How often do you consume foods containing non-nutritive or low-calorie sweeteners?', 'ARTIFICIAL_SWEETENERS_FOOD', FALSE, '¿Con qué frecuencia consume alimentos que contienen edulcorantes no nutritivos o bajos en calorías?', '¿Con qué frecuencia consume alimentos que contienen edulcorantes no nutritivos o bajos en calorías?', 'ノンカロリーまたは低カロリーの甘味料を含む食品はどれくらい摂取していますか？'),
    (465, 'When you consume foods or beverages containing non-nutritive or low-calorie sweeteners, do you tend to experience gastrointestinal disorders afterwards, such as gas, bloating, and/or diarrhea?', 'ARTIFICIAL_GI_DISORDERS', FALSE, 'Cuando consume alimentos o bebidas que contienen edulcorantes no nutritivos o bajos en calorías, ¿tiende a experimentar sintomas gastrointestinales posteriores, como gases, inflamación y/o diarrea?', 'Cuando consume alimentos o bebidas que contienen edulcorantes no nutritivos o bajos en calorías, ¿tiende a experimentar sintomas gastrointestinales posteriores, como gases, inflamación y/o diarrea?', 'ノンカロリーまたは低カロリーの甘味料を含む食品や飲料を摂取した場合、その後、ガス、膨張、下痢などの消化器の不具合が起きることがよくありますか？'),
    (466, 'If you answered "yes", to the previous question, what are the symptoms? Select all that apply.', 'ARTIFICIAL_GI_DISORDER_TYPES', FALSE, 'Si respondió "sí" a la pregunta anterior, ¿cuáles son los síntomas? Seleccione todas las que correspondan.', 'Si respondió "sí" a la pregunta anterior, ¿cuáles son los síntomas? Seleccione todas las que correspondan.', '前の質問への回答が「はい」の場合、症状は何ですか？該当するものをすべて選択してください。');

-- Set the question types
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type)
VALUES
    (463, 'SINGLE'),
    (465, 'SINGLE'),
    (466, 'MULTIPLE');

-- Associate them with the group. We need to make space for them, so we'll re-index a few existing questions first.
UPDATE ag.group_questions SET display_index = 28 WHERE survey_group = 4 AND display_index = 25;
UPDATE ag.group_questions SET display_index = 27 WHERE survey_group = 4 AND display_index = 24;
UPDATE ag.group_questions SET display_index = 26 WHERE survey_group = 4 AND display_index = 23;
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index)
VALUES
    (4, 463, 23),
    (4, 465, 24),
    (4, 466, 25);

-- Create the responses we'll need for the questions
INSERT INTO ag.survey_response (american, spanish, spain_spanish, japanese)
VALUES
    ('Stomachache', 'Dolor de estómago', 'Dolor de estómago', '腹痛'),
    ('Soft stools', 'Heces blandas', 'Heces blandas', '軟便'),
    ('Constipation', 'Estriñimiento', 'Estriñimiento', '便秘');

-- Associate responses with questions
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index)
VALUES
    (463, 'Unspecified', 0),
    (463, 'Never', 1),
    (463, 'Rarely (a few times/month)', 2),
    (463, 'Occasionally (1-2 times/week)', 3),
    (463, 'Regularly (3-5 times/week)', 4),
    (463, 'Daily', 5),
    (465, 'Unspecified', 0),
    (465, 'Yes', 1),
    (465, 'No', 2),
    (466, 'Unspecified', 0),
    (466, 'Stomachache', 1),
    (466, 'Diarrhea', 2),
    (466, 'Soft stools', 3),
    (466, 'Constipation', 4),
    (466, 'Other', 5);

-- Set up the triggers
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question)
VALUES
    (157, 'Rarely (a few times/month)', 465),
    (157, 'Occasionally (1-2 times/week)', 465),
    (157, 'Regularly (3-5 times/week)', 465),
    (157, 'Daily', 465),
    (463, 'Rarely (a few times/month)', 465),
    (463, 'Occasionally (1-2 times/week)', 465),
    (463, 'Regularly (3-5 times/week)', 465),
    (463, 'Daily', 465),
    (465, 'Yes', 466);


-- Update translations for survey questions
UPDATE ag.survey_question SET japanese = 'どれくらいの頻度でプロバイオティクスや乳酸菌を服用していますか？' WHERE american = 'How frequently do you take a probiotic?';
UPDATE ag.survey_question SET japanese = 'どれくらいの頻度でビタミンB複合体、葉酸塩または葉酸を服用していますか？' WHERE american = 'How frequently do you take Vitamin B complex, folate or folic acid?';
UPDATE ag.survey_question SET japanese = '抗生物質を投与された動物の肉／乳製品を食べますか？' WHERE american = 'Do you eat meat/dairy products from animals treated with antibiotics?';
UPDATE ag.survey_question SET japanese = '私は過去____の間に居住国以外に旅行したことがある。' WHERE american = 'I have traveled outside of my country of residence in the past _________.';
UPDATE ag.survey_question SET japanese = 'あなたの同居人でこの研究に参加している人はいますか？' WHERE american = 'Are any of your roommates participating in this study?';
UPDATE ag.survey_question SET japanese = '水泳用プール／お風呂の使用頻度を教えてください。' WHERE american = 'How often do you use a swimming pool/hot tub?';
UPDATE ag.survey_question SET japanese = '私は過去___の間に抗生物質を服用しました。' WHERE american = 'I have taken antibiotics in the last ____________.';
UPDATE ag.survey_question SET japanese = '私は過去___の間にインフルエンザのワクチンを接種しました。' WHERE american = 'I have received a flu vaccine in the last ____________.';
UPDATE ag.survey_question SET japanese = '怖い夢や悪夢を見ることがありますか？' WHERE american = 'Do you have vivid and/or frightening dreams?';
UPDATE ag.survey_question SET japanese = '1週間のうち、1日に全粒粉を2食分以上を摂取する頻度はどのくらいですか？ （1食分＝100％全粒粉パン1枚、高繊維シリアル、オートミールなどの全粒シリアル1カップ、全粒クラッカー3～4枚、玄米や全粒パスタ1/2カップ）' WHERE american = 'In an average week, how often do you eat at least 2 servings of whole grains in a day?';
UPDATE ag.survey_question SET japanese = '1日に2～3食分以上の果物を摂取する頻度はどのくらいですか？ (1食分 =　果物1/2カップ、中くらいの大きさの果物1個、4 オンスの100%フルーツジュース)。' WHERE american = 'In an average week, how often to you consume at least 2-3 servings of fruit in a day?  (1 serving = 1/2 cup fruit; 1 medium sized fruit; 4 oz. 100% fruit juice.)';
UPDATE ag.survey_question SET japanese = '1週間のうち、1日に2-3食分以上のでんぷん質野菜と非でんぷん質野菜を摂取する頻度はどのくらいですか？でんぷん質野菜の例としては、白イモ、トウモロコシ、エンドウ豆、キャベツなどが挙げられます。非でんぷん質野菜の例としては、生の葉野菜、キュウリ、トマト、ピーマン、ブロッコリー、ケールなどがあります。（ 1食分＝野菜/じゃがいも1/2カップ、生の葉野菜1カップ）' WHERE american = 'In an average week, how often do you consume at least 2-3 servings of starchy and non-starchy vegetables. Examples of starchy vegetables include white potatoes, corn, peas and cabbage.  Examples of non-starchy vegetables include raw leafy greens, cucumbers, tomatoes, peppers, broccoli, and kale. (1 serving = ½ cup vegetables/potatoes; 1 cup leafy raw vegetables)';
UPDATE ag.survey_question SET japanese = '1 週間に何種類の植物（野菜、果物、穀物）を食べますか?例えばにんじん、じゃがいも、玉ねぎが入ったスープを消費した場合、 3 種類の野菜とみなします。多穀物パンを消費した場合、それぞれの穀物を数えてください。' WHERE american = 'In an average week, how many different plant species do you eat? e.g. If you consume a can of soup that contains carrots, potatoes, and onion, you can count this as 3 different plants; If you consume multi-grain bread, each different grain counts as a plant.';
UPDATE ag.survey_question SET japanese = '１週間のうち、1日に2食分以上の牛乳やチーズを摂取する頻度はどのくらいですか？（ 1食分＝牛乳またはヨーグルト1カップ、チーズ1.5～2オンス）' WHERE american = 'In an average week, how often do you consume at least 2 servings of milk or cheese a day?  (1 serving = 1 cup milk or yogurt; 1 1/2 - 2 ounces cheese)';
UPDATE ag.survey_question SET japanese = 'あなたの微生物に関連する食習慣や生活習慣があれば記入してください。' WHERE american = 'Please write anything else about yourself that you think could affect your personal microorganisms.';
UPDATE ag.survey_question SET japanese = '過去____の間にビール、ワイン、アルコールを除いた発酵食品を摂取する頻度や量が大幅に（2倍以上）増加しました。' WHERE american = 'Excluding beer, wine, and alcohol, I have significantly increased (i.e. more than doubled) my intake of fermented foods in frequency or quantity within the last ____.';
UPDATE ag.survey_question SET japanese = '以下の発酵食品/飲料のいずれかを自宅で製造して摂取していますか？該当するものをすべて選択し、記載されていないものは「その他」にすべて記入してください。' WHERE american = 'Do you produce any of the following fermented foods/beverages at home for personal consumption? Check all that apply.';
UPDATE ag.survey_question SET japanese = 'その他、発酵食品について記載することがあればご記入ください。' WHERE american = 'Volunteer more information about this activity.';
UPDATE ag.survey_question SET japanese = '1週間のうち、ラード、バター、ギーはどれくらいの頻度で使用・調理していますか？' WHERE american = 'In a given week, how often do you use or cook with lard, butter or ghee?';
UPDATE ag.survey_question SET japanese = '1週間のうち、ココナッツオイル、パームオイル、パームカーネルオイルをどれくらいの頻度で使用していますか？' WHERE american = 'In a given week, how often do you use or cook with coconut, palm or palm kernel oil?';
UPDATE ag.survey_question SET japanese = '1週間のうち、マーガリンや植物性ショートニングをどれくらいの頻度で使用していますか？' WHERE american = 'In a given week, how often do you use or cook with margarine or (vegetable) shortening?';
UPDATE ag.survey_question SET japanese = 'ほうれん草、ふだん草、ビーツまたはビーツの葉、オクラ、キノア、アマランス、蕎麦、小麦ふすままたは胚芽、ふすまシリアル、チアシード、ルバーブ、ダークチョコレートやココア粉末（> 70％）、又はナッツ（アーモンド、ピーナッツ、ピーカン、カシュー、ヘーゼルナッツ）などのシュウ酸塩が豊富な食品を平均してどれくらいの頻度で摂取していますか? ' WHERE american = 'On average, how often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts, pecans, cashews, and hazelnuts?';

-- Update translations for survey responses
UPDATE ag.survey_response SET japanese = '不明' WHERE american = 'Unspecified';
UPDATE ag.survey_response SET japanese = '肉と野菜両方食べる' WHERE american = 'Omnivore';
UPDATE ag.survey_response SET japanese = '肉と野菜両方食べるが、赤身肉は食べない' WHERE american = 'Omnivore but do not eat red meat';
UPDATE ag.survey_response SET japanese = 'ベジタリアン（菜食主義）' WHERE american = 'Vegetarian';
UPDATE ag.survey_response SET japanese = 'ビーガン（完全菜食主義）' WHERE american = 'Vegan';
UPDATE ag.survey_response SET japanese = 'ペットボトル・ミネラルウォーター' WHERE american = 'Bottled';
UPDATE ag.survey_response SET japanese = 'ろ過水' WHERE american = 'Filtered';
UPDATE ag.survey_response SET japanese = '分からない' WHERE american = 'Not sure';
UPDATE ag.survey_response SET japanese = '私は1年以上現在地で暮らしている' WHERE american = 'I have lived in my current state of residence for more than a year.';
UPDATE ag.survey_response SET japanese = '1回未満' WHERE american = 'Less than one';
UPDATE ag.survey_response SET japanese = '1回' WHERE american = 'One';
UPDATE ag.survey_response SET japanese = '2回' WHERE american = 'Two';
UPDATE ag.survey_response SET japanese = '3回' WHERE american = 'Three';
UPDATE ag.survey_response SET japanese = '4回' WHERE american = 'Four';
UPDATE ag.survey_response SET japanese = '5回以上' WHERE american = 'Five or more';
UPDATE ag.survey_response SET japanese = '分からない' WHERE american = 'I don''t know, I do not have a point of reference';
UPDATE ag.survey_response SET japanese = '医療従事者（医師、医師助手）に診断されたことがある' WHERE american = 'Diagnosed by a medical professional (doctor, physician assistant)';
UPDATE ag.survey_response SET japanese = '代替医療の医師に診断されたことがある' WHERE american = 'Diagnosed by an alternative medicine practitioner';
UPDATE ag.survey_response SET japanese = '自己診断したことがある' WHERE american = 'Self-diagnosed';
UPDATE ag.survey_response SET japanese = '固形食と粉ミルク/母乳の両方を食べている' WHERE american = 'I eat both solid food and formula/breast milk';
