-- Adjust translations of survey questions
UPDATE ag.survey_question SET japanese = '平日(学校あるいは仕事がある日)の「朝、起きる時間」は、だいたい何時ごろですか。' WHERE survey_question_id = 344;
UPDATE ag.survey_question SET japanese = '平日(学校あるいは仕事がある日)の「夜、寝る時間」は、だいたい何時ごろですか。' WHERE survey_question_id = 345;
UPDATE ag.survey_question SET japanese = '休日(学校あるいは仕事がない日)の「朝、起きる時間」は、だいたい何時ごろですか。' WHERE survey_question_id = 346;
UPDATE ag.survey_question SET japanese = '休日(学校あるいは仕事がない日)の「夜、寝る時間」は、だいたい何時ごろですか。' WHERE survey_question_id = 347;
UPDATE ag.survey_question SET japanese = 'ノンカロリーまたは低カロリーの甘味料を含む食品はどれくらい摂取していますか? （※ノンカロリーまたは低カロリーの甘味料とは、糖アルコール(ソルビトール、マンニトール、マルチトール、キシ リトール、還元パラチノース、エリスリトール)、合成甘味料(サッカリン、アスパル テーム、アセスルファムカリウム(アセスルファム K)、スクラロース)を指します。）' WHERE survey_question_id = 463;
UPDATE ag.survey_question SET japanese = 'ノンカロリーまたは低カロリーの甘味料を含む食品を食べたとき、おなかの調子が悪くなることはありますか?' WHERE survey_question_id = 465;
UPDATE ag.survey_question SET japanese = '人工甘味料入りのダイエット飲料を摂取していますか？（※人工甘味料とは、糖アルコール(ソルビトール、マンニトール、マルチトール、キシ リトール、還元パラチノース、エリスリトール)、合成甘味料(サッカリン、アスパル テーム、アセスルファムカリウム(アセスルファム K)、スクラロース)を指します。）' WHERE survey_question_id = 157;
