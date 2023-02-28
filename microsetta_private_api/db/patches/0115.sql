-- Add columns to survey-related tables to support Japanese
ALTER TABLE ag.survey_group ADD COLUMN japanese VARCHAR;
ALTER TABLE ag.survey_question ADD COLUMN japanese VARCHAR;
ALTER TABLE ag.survey_response ADD COLUMN japanese VARCHAR;

-- For debugging testing, set all of the Japanese values to English so that missing translations are obvious.
-- TODO: Remove these three queries before merging PR
UPDATE ag.survey_group SET japanese = american;
UPDATE ag.survey_question SET japanese = american;
UPDATE ag.survey_response SET japanese = american;

-- Add the Japanese text for survey names
UPDATE ag.survey_group SET japanese = '基本情報' WHERE group_order = -10; -- Basic Information
UPDATE ag.survey_group SET japanese = '自宅において' WHERE group_order = -11; -- At Home
UPDATE ag.survey_group SET japanese = '生活様式' WHERE group_order = -12; -- Lifestyle
UPDATE ag.survey_group SET japanese = '消化器' WHERE group_order = -13; -- Gut
UPDATE ag.survey_group SET japanese = '健康全般' WHERE group_order = -14; -- General Health
UPDATE ag.survey_group SET japanese = '健康診断' WHERE group_order = -15; -- Health Diagnosis
UPDATE ag.survey_group SET japanese = 'アレルギー' WHERE group_order = -16; -- Allergies
UPDATE ag.survey_group SET japanese = '飲食物' WHERE group_order = -17; -- Diet
UPDATE ag.survey_group SET japanese = '食事の詳細' WHERE group_order = -18; -- Detailed Diet
UPDATE ag.survey_group SET japanese = '他の' WHERE group_order = -22; -- Other

-- Add the Japanese text for survey questions
UPDATE ag.survey_question SET japanese = '普通は夜およそ何時間くらい寝ますか？' WHERE american = 'Approximately how many hours of sleep do you get in an average night?';
UPDATE ag.survey_question SET japanese = '診断されたのはいつ頃ですか？' WHERE american = 'Approximately when were you diagnosed?';
UPDATE ag.survey_question SET japanese = 'あなたの同居人のうち、誰かこの研究に参加している人はいますか？' WHERE american = 'Are any of your roommates participating in this study?';
UPDATE ag.survey_question SET japanese = 'あなたは母乳や調整粉乳から栄養のほとんどを受け取っている乳児ですか、それとも成人用栄養シェイクから栄養のほとんど（1日のカロリーの75%以上）を受け取っている成人ですか？' WHERE american = 'Are you an infant who receives most of your nutrition from breast milk or formula, or an adult who receives most (more than 75% of daily calories) of your nutrition from adult nutritional shakes (i.e. Ensure)?';
UPDATE ag.survey_question SET japanese = '現在妊娠中ですか？' WHERE american = 'Are you currently pregnant?';
UPDATE ag.survey_question SET japanese = '現在、何らかのホルモン避妊法を使用していますか？' WHERE american = 'Are you currently using some form of hormonal birth control?';
UPDATE ag.survey_question SET japanese = 'この人とあなたは血のつながりがありますか？' WHERE american = 'Are you genetically related?';
UPDATE ag.survey_question SET japanese = 'あなたはグルテン不耐症ですか？' WHERE american = 'Are you gluten intolerant?';
UPDATE ag.survey_question SET japanese = '患者介護に関与していますか、または病院／クリニックで働いていますか？' WHERE american = 'Are you involved in patient care or work in a hospital / clinic setting?';
UPDATE ag.survey_question SET japanese = 'あなたは乳糖不耐症ですか？' WHERE american = 'Are you lactose intolerant?';
UPDATE ag.survey_question SET japanese = 'あなたはこの研究の他の参加者と関係がありますか？' WHERE american = 'Are you related to any of the other participants in this study?';
UPDATE ag.survey_question SET japanese = 'あなたは毎日マルチビタミンを服用していますか？' WHERE american = 'Are you taking a daily multivitamin?';
UPDATE ag.survey_question SET japanese = '他の栄養／ハーブサプリメントを服用していますか？' WHERE american = 'Are you taking any other nutritional/herbal supplements?';
UPDATE ag.survey_question SET japanese = '自宅で水を飲む前に、追加の処理（ろ過を除く）を施していますか（例：沸騰、浄化タブレット、塩素／漂白剤） ？' WHERE american = 'At home, do you apply additional treatment (not including filtering) to your drinking water prior to consumption (e.g., boiling, purification tablet, chlorine/bleach)?';
UPDATE ag.survey_question SET japanese = '自宅で飲む、味のついていない普通の飲料水は主にどういうものですか？これには静水または発泡水／炭酸水も含められます。' WHERE american = 'At home, what is the main source of your plain, unflavored drinking water? This can include still or sparkling/carbonated water.';
UPDATE ag.survey_question SET japanese = '通常、寝る前の最後の食事や軽食を何時に食べますか？' WHERE american = 'At what time do you typically eat your last meal or snack before going to sleep?';
UPDATE ag.survey_question SET japanese = '出生時の生物学的性別' WHERE american = 'Biological sex assigned at birth';
UPDATE ag.survey_question SET japanese = '誕生月' WHERE american = 'Birth month';
UPDATE ag.survey_question SET japanese = '誕生年' WHERE american = 'Birth year';
UPDATE ag.survey_question SET japanese = '出生国' WHERE american = 'Country of birth';
UPDATE ag.survey_question SET japanese = '居住国' WHERE american = 'Country of residence';
UPDATE ag.survey_question SET japanese = '現在の郵便番号：' WHERE american = 'Current ZIP code';
UPDATE ag.survey_question SET japanese = '便の硬さについて教えてください。' WHERE american = 'Describe the consistency of your bowel movements';
UPDATE ag.survey_question SET japanese = 'あなたの一番血のつながりが近い親族（一親等）で、片頭痛に悩まされている人はいますか？' WHERE american = 'Do any of your first-degree relatives suffer from migraines?';
UPDATE ag.survey_question SET japanese = 'あなたは爪を噛みますか？' WHERE american = 'Do you bite your fingernails?';
UPDATE ag.survey_question SET japanese = '現在、がんを患っていますか？' WHERE american = 'Do you currently have cancer?';
UPDATE ag.survey_question SET japanese = '現在、他の疾患に対して市販薬または処方薬を服用していますか？' WHERE american = 'Do you currently take non-prescription or prescription medication for other conditions?';
UPDATE ag.survey_question SET japanese = '現在、顔のニキビに処方薬を服用していますか？' WHERE american = 'Do you currently take prescription medication for facial acne?';
UPDATE ag.survey_question SET japanese = '抗生物質で治療した動物の肉／乳製品を食べますか？' WHERE american = 'Do you eat meat/dairy products from animals treated with antibiotics?';
UPDATE ag.survey_question SET japanese = '運動は一般的に屋内それとも屋外でしますか？' WHERE american = 'Do you generally exercise indoors or outdoors?';
UPDATE ag.survey_question SET japanese = '猫を飼っていますか？' WHERE american = 'Do you have a cat(s)?';
UPDATE ag.survey_question SET japanese = '犬を飼っていますか？' WHERE american = 'Do you have a dog(s)?';
UPDATE ag.survey_question SET japanese = '不規則な時間帯に仕事や睡眠を必要とする仕事やその他の状況がありますか（午後10時～午前6時に仕事して、午前9時～午後5時に睡眠をとるなど）？' WHERE american = 'Do you have a job or some other situation that requires you to work and sleep during atypical hours (e.g. work between 10pm-6am and sleep between 9am-5pm)?';
UPDATE ag.survey_question SET japanese = '次の慢性疾患のいずれかがありますか（該当するもの全てにチェックを入れてください） ：' WHERE american = 'Do you have any of the following chronic conditions (check all that apply)';
UPDATE ag.survey_question SET japanese = '食べ物以外で、以下に記載のものに対するアレルギーはありますか？該当するものをすべて選択してください。' WHERE american = 'Do you have any of the following non-food allergies? Select all that apply.';
UPDATE ag.survey_question SET japanese = '家畜をよく触ったり定期的に触ったりすることはありますか？' WHERE american = 'Do you have frequent and regular contact with farm animals?';
UPDATE ag.survey_question SET japanese = '家に他の（犬や猫以外の）ペットはいますか？' WHERE american = 'Do you have other (non-dog or cat) pets at home?';
UPDATE ag.survey_question SET japanese = '季節性アレルギーはありますか？' WHERE american = 'Do you have seasonal allergies?';
UPDATE ag.survey_question SET japanese = '生々しいおよび／または恐ろしい夢を見ることがありますか？' WHERE american = 'Do you have vivid and/or frightening dreams?';
UPDATE ag.survey_question SET japanese = '次の発酵食品／飲料のいずれかを自宅で個人用に製造していますか？該当するものをすべて選択し、記載されていないものを「その他」に記入してください。' WHERE american = 'Do you produce any of the following fermented foods/beverages at home for personal consumption? Select all that apply and write in any that are not listed under ‘Other’.';
UPDATE ag.survey_question SET japanese = '次の発酵食品／飲料のいずれかを商業目的で製造していますか？該当するものをすべて選択し、記載されていないものを「その他」に記入してください。' WHERE american = 'Do you produce any of the following fermented foods/beverages for commercial purposes? Select all that apply and write in any that are not listed under ‘Other’.';
UPDATE ag.survey_question SET japanese = '片頭痛が起きることがありますか？' WHERE american = 'Do you suffer from migraines?';
UPDATE ag.survey_question SET japanese = '定期的に海でサーフィンをしていますか？' WHERE american = 'Do you surf in the ocean on a regular basis?';
UPDATE ag.survey_question SET japanese = 'あなたは片頭痛用の薬を飲んでいますか。' WHERE american = 'Do you take any migraine medication?';
UPDATE ag.survey_question SET japanese = '症状を和らげるために薬を服用していますか？' WHERE american = 'Do you take medication to relieve your symptoms?';
UPDATE ag.survey_question SET japanese = 'アプリを使用して次のいずれかを追跡していますか？該当するものをすべて選択してください。' WHERE american = 'Do you track any of the following using an app(s)? Select all that apply.';
UPDATE ag.survey_question SET japanese = 'デオドラントまたは制汗剤（制汗剤には一般的にアルミニウムが含まれています）は使用していますか？' WHERE american = 'Do you use deodorant or antiperspirant (antiperspirants generally contain aluminum)?';
UPDATE ag.survey_question SET japanese = '衣類を乾かすときに柔軟剤を使っていますか？' WHERE american = 'Do you use fabric softener when drying your clothes?';
UPDATE ag.survey_question SET japanese = '市販薬を使用して顔のニキビを治していますか？' WHERE american = 'Do you use non-prescription products to control facial acne?';
UPDATE ag.survey_question SET japanese = 'この人はあなたと一緒に住んでいますか？' WHERE american = 'Does this person live with you?';
UPDATE ag.survey_question SET japanese = 'ビール、ワイン、アルコールを除き、私が発酵食品を摂取する頻度または量は、過去____以内に大幅に（2倍以上）増加しました。' WHERE american = 'Excluding beer, wine, and alcohol, I have significantly increased (i.e. more than doubled) my intake of fermented foods in frequency or quantity within the last ____.';
UPDATE ag.survey_question SET japanese = '新型コロナウイルス／COVID -19のため、あなたに次のようなことがありましたか？（該当するもの全てにチェックを入れてください）' WHERE american = 'Have any of the following happened to you because of Coronavirus/COVID-19? (check all that apply)';
UPDATE ag.survey_question SET japanese = '新型コロナウイルス／COVID -19のため、ご家族に次のようなことがありましたか？（該当するもの全てにチェックを入れてください）' WHERE american = 'Have any of the following happened to your family members because of Coronavirus/COVID-19? (check all that apply)';
UPDATE ag.survey_question SET japanese = '注意欠如障害（Attention Deficit Disorder、ADD）／注意欠如多動性障害（Attention Deficit Hyperactivity Disorder、ADHD）と診断されたことはありますか？' WHERE american = 'Have you been diagnosed with ADD/ADHD?';
UPDATE ag.survey_question SET japanese = 'アルツハイマー病／認知症と診断されたことはありますか？' WHERE american = 'Have you been diagnosed with Alzheimer’s Disease/Dementia?';
UPDATE ag.survey_question SET japanese = '喘息、嚢胞性線維症、慢性閉塞性肺疾患（chronic obstructive pulmonary disease、COPD）またはその他の肺疾患と診断されたことはありますか？' WHERE american = 'Have you been diagnosed with Asthma, Cystic fibrosis, COPD or other lung Disease?';
UPDATE ag.survey_question SET japanese = '自閉症スペクトラム障害または状態（ASD／ASC）と診断されたことはありますか？' WHERE american = 'Have you been diagnosed with Autism Spectrum Disorder or Condition (ASD/ASC)?';
UPDATE ag.survey_question SET japanese = 'ループス（全身性エリテマトーデス）、R.A.（関節リウマチ）、MS （多発性硬化症）、橋本甲状腺炎などの自己免疫疾患、またはその他の自己免疫疾患と診断されたことはありますか？' WHERE american = 'Have you been diagnosed with autoimmune disease such as Lupus (systemic lupus erythematosus), R.A. (rheumatoid arthritis), MS (multiple sclerosis), Hashimoto’s thyroiditis , or any other auto-immune disease?';
UPDATE ag.survey_question SET japanese = '新型コロナウイルス/COVID -19に感染している可能性が高い人と接触したことはありますか？（該当するもの全てにチェックを入れてください）' WHERE american = 'Have you been exposed to someone likely to have Coronavirus/COVID-19? (check all that apply)';
UPDATE ag.survey_question SET japanese = '新型コロナウイルス／COVID -19にかかったと疑ったことがありますか？' WHERE american = 'Have you been suspected of having Coronavirus/COVID-19 infection?';
UPDATE ag.survey_question SET japanese = '今までに皮膚疾患の診断を受けたことはありますか？' WHERE american = 'Have you ever been diagnosed with a skin condition?';
UPDATE ag.survey_question SET japanese = '今までに他に何かの病気の症状で診断を受けたことはありますか？ ' WHERE american = 'Have you ever been diagnosed with any other relevant clinical condition? ';
UPDATE ag.survey_question SET japanese = '今までにがんと診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with cancer?';
UPDATE ag.survey_question SET japanese = '今までにカンジダや真菌の腸内増殖過多と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with Candida or fungal overgrowth in the gut?';
UPDATE ag.survey_question SET japanese = '今までにクロストリジウム・ディフィシル（ C. difficile ）感染症と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with Clostridium difficile (C. diff) infection?';
UPDATE ag.survey_question SET japanese = '今までに冠動脈疾患、心臓疾患、心臓発作、または脳卒中と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with coronary artery disease, heart disease, heart attack, or stroke?';
UPDATE ag.survey_question SET japanese = '今までに糖尿病と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with diabetes?';
UPDATE ag.survey_question SET japanese = '今までにてんかんまたは発作性障害と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with epilepsy or seizure disorder?';
UPDATE ag.survey_question SET japanese = '今までに炎症性腸疾患（inflammatory bowel disease、IBD）と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with inflammatory bowel disease (IBD)?';
UPDATE ag.survey_question SET japanese = '今までに過敏性腸症候群（irritable bowel syndrome、IBS）*と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with irritable bowel syndrome (IBS)*?';
UPDATE ag.survey_question SET japanese = '今までに腎臓病と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with kidney disease?';
UPDATE ag.survey_question SET japanese = '今までに肝臓病と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with liver disease?';
UPDATE ag.survey_question SET japanese = '今までに精神疾患と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with mental health illness?';
UPDATE ag.survey_question SET japanese = '今までに片頭痛の診断を受けたことはありますか？' WHERE american = 'Have you ever been diagnosed with migraines?';
UPDATE ag.survey_question SET japanese = '今までにフェニルケトン尿症と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with phenylketonuria?';
UPDATE ag.survey_question SET japanese = '今までに小腸細菌過剰増殖症（small intestinal bacterial overgrowth、SIBO）と診断されたことはありますか？' WHERE american = 'Have you ever been diagnosed with small intestinal bacterial overgrowth (SIBO)?';
UPDATE ag.survey_question SET japanese = '今までに甲状腺疾患と診断されたことはありますか。' WHERE american = 'Have you ever been diagnosed with thyroid disease?';
UPDATE ag.survey_question SET japanese = '水ぼうそうにかかったこと（水ぼうそうワクチンのことではありません）はありますか？' WHERE american = 'Have you had a chickenpox infection (not the varicella vaccine)?';
UPDATE ag.survey_question SET japanese = '次のいずれかの症状がありましたか？（該当するもの全てにチェックを入れてください）' WHERE american = 'Have you had any of the following symptoms? (check all that apply)';
UPDATE ag.survey_question SET japanese = '虫垂（盲腸）を取って（摘出して）いますか？' WHERE american = 'Have you had your appendix removed?';
UPDATE ag.survey_question SET japanese = '扁桃を取って（摘出して）いますか？' WHERE american = 'Have you had your tonsils removed?';
UPDATE ag.survey_question SET japanese = 'Lyft、Uberを含むライドシェアサービス、またはタクシーの代替を使用したことがありますか?' WHERE american = 'Have you used shared ride services including Lyft, Uber or alternative forms of taxi?';
UPDATE ag.survey_question SET japanese = '身長' WHERE american = 'Height';
UPDATE ag.survey_question SET japanese = '繊維サプリメントをどれくらいの回数服用していますか？' WHERE american = 'How frequently do you take a fiber supplement?';
UPDATE ag.survey_question SET japanese = 'プロバイオティクをどれくらいの回数服用していますか？' WHERE american = 'How frequently do you take a probiotic?';
UPDATE ag.survey_question SET japanese = 'ビタミンDサプリメントをどれくらいの回数服用していますか？' WHERE american = 'How frequently do you take a Vitamin D supplement?';
UPDATE ag.survey_question SET japanese = 'ビタミンB複合体、葉酸塩または葉酸をどれくらいの回数服用していますか？' WHERE american = 'How frequently do you take Vitamin B complex, folate or folic acid?';
UPDATE ag.survey_question SET japanese = '通常、アルコール飲料は一度に何杯飲みますか？' WHERE american = 'How many alcoholic beverages do you usually have per sitting?';
UPDATE ag.survey_question SET japanese = '通常、1日に何回食事をしますか？' WHERE american = 'How many meals do you typically eat per day?';
UPDATE ag.survey_question SET japanese = 'あなたが同居している人のうち、あなたの家族の一員ではない人は何人いますか？' WHERE american = 'How many of the people you live with are not a part of your family?';
UPDATE ag.survey_question SET japanese = '通常、1日に何回軽食（おやつ）を食べますか？' WHERE american = 'How many snacks do you typically eat per day?';
UPDATE ag.survey_question SET japanese = '便通は普通1日に何回ありますか？' WHERE american = 'How many times do you have a bowel movement in an average day?';
UPDATE ag.survey_question SET japanese = '仕事を含め、何らかの理由で自宅の外に出た（例えば、店舗や公園などに行くために家から離れた）回数は何回でしたか？' WHERE american = 'How many times have you gone outside of your home for any reason including work (e.g., left your property to go to stores, parks, etc.)?';
UPDATE ag.survey_question SET japanese = '通常、一度にどのくらい飲みますか？' WHERE american = 'How much do you typically consume in a sitting?';
UPDATE ag.survey_question SET japanese = 'あなたの生活の質を損なうという意味で、あなたの睡眠の問題は、どの程度他の人々が見てわかると思いますか？' WHERE american = 'How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life?';
UPDATE ag.survey_question SET japanese = 'トウモロコシ、大豆、キャノーラ（菜種）、オリーブ、ピーナッツ、アボカド、サフラワー、ヒマワリなどの植物油（ココナッツ油とパーム油は除かれます）で調理することはどれくらいありますか？ ' WHERE american = 'How often do you  cook with vegetable oils (excluding coconut and palm oil) such as corn, soy, canola (rapeseed), olive, peanut, avocado, safflower or sunflower? ';
UPDATE ag.survey_question SET japanese = '歯磨きは1日何回していますか？' WHERE american = 'How often do you brush your teeth?';
UPDATE ag.survey_question SET japanese = '水を1日1 L （約32オンス）以上飲むことはどれくらいありますか？' WHERE american = 'How often do you consume at least 1L (~32 ounces) of water in a day?';
UPDATE ag.survey_question SET japanese = '牛乳またはチーズを1日2サービング以上食べることはどれくらいありますか？（ 1サービング＝1カップ分の牛乳またはヨーグルト；1.5～ 2オンス分のチーズ）' WHERE american = 'How often do you consume at least 2 servings of milk or cheese a day? (1 serving = 1 cup milk or yogurt; 1½ - 2 ounces cheese)';
UPDATE ag.survey_question SET japanese = '果物を1日に2 ～ 3サービング以上食べることはどれくらいありますか？（ 1サービング＝半カップ分の果物；ミディアムサイズの果物1個、4液量オンス分の果汁100％のジュース。）' WHERE american = 'How often do you consume at least 2-3 servings of fruit in a day? (1 serving = ½ cup fruit; 1 medium sized fruit; 4 fl.oz. 100% fruit juice.)';
UPDATE ag.survey_question SET japanese = 'デンプン質と非デンプン質の野菜を2 ～ 3サービング以上食べることはどれくらいありますか？デンプン質の野菜とは、ジャガイモ、トウモロコシ、エンドウ豆、キャベツなどです。非デンプン質の野菜とは、生の葉物野菜、キュウリ、トマト、ピーマン、ブロッコリー、ケールなどです。（ 1サービング＝半カップ分の野菜／ジャガイモ；1カップ分の生の葉物野菜）' WHERE american = 'How often do you consume at least 2-3 servings of starchy and non-starchy vegetables. Examples of starchy vegetables include white potatoes, corn, peas and cabbage. Examples of non-starchy vegetables include raw leafy greens, cucumbers, tomatoes, peppers, broccoli, and kale. (1 serving = ½ cup vegetables/potatoes; 1 cup leafy raw vegetables)';
UPDATE ag.survey_question SET japanese = 'ビーツ（サトウダイコンのこと。生、缶入り、漬物にした、または焼いたものを含む）はどれくらい食べていますか？（ 1サービング＝1カップ分の生または調理済みのもの）' WHERE american = 'How often do you consume beets (including raw, canned, pickled, or roasted)? (1 serving = 1 cup raw or cooked)';
UPDATE ag.survey_question SET japanese = 'ノンカロリーまたは低カロリーの甘味料を含む飲料を飲むことはどれくらいありますか*？' WHERE american = 'How often do you consume beverages with non-nutritive or low-calorie sweeteners*?';
UPDATE ag.survey_question SET japanese = '鶏肉または七面鳥肉はどれくらい食べますか？' WHERE american = 'How often do you consume chicken or turkey?';
UPDATE ag.survey_question SET japanese = 'ノンカロリーまたは低カロリーの甘味料を含む食品はどれくらい摂取していますか？' WHERE american = 'How often do you consume foods containing non-nutritive or low-calorie sweeteners?';
UPDATE ag.survey_question SET japanese = 'プライムリブ、Tボーンステーキ、ハンバーガー、リブ肉、ベーコンなど、脂肪分の高い赤肉はどれくらい食べていますか？' WHERE american = 'How often do you consume higher fat red meats like prime rib, T-bone steak, hamburger, ribs, bacon, etc.?';
UPDATE ag.survey_question SET japanese = '肉／卵はどれくらい食べていますか？' WHERE american = 'How often do you consume meat/eggs?';
UPDATE ag.survey_question SET japanese = '代用乳（豆乳、無乳糖ミルク、アーモンドミルクなど）はどれくらい摂取していますか？' WHERE american = 'How often do you consume milk substitutes (soy milk, lactose free milk, almond milk, etc.)?';
UPDATE ag.survey_question SET japanese = '発酵野菜または植物製品を1サービング以上摂取することはどれくらいありますか？（ 1サービング＝半カップ分のザウアークラウト、キムチまたは発酵野菜、あるいは1カップ分の紅茶キノコ）' WHERE american = 'How often do you consume one or more servings of fermented vegetables or plant products? (1 serving = ½ cup sauerkraut, kimchi or fermented vegetable or 1 cup of kombucha)';
UPDATE ag.survey_question SET japanese = 'ほうれん草、スイスチャード、ビートの根または若葉、オクラ、キヌア、アマランサス、そば、小麦ふすまたは胚芽、ブランシリアル、チアシード、ダイオウ、スイカ、ダークチョコレートまたはココアパウダー（＞70％）などのシュウ酸塩を多く含む食物、およびアーモンド、ピーナッツ、ペカン、カシュー、ヘーゼルナッツなどのナッツ類はどれくらい食べていますか？' WHERE american = 'How often do you consume oxalate-rich foods, such as spinach, Swiss chard, beetroot or beet greens, okra, quinoa, amaranth, buckwheat, wheat bran or germ, Bran cereal, chia seeds, rhubarb, watermelon, dark chocolate or cocoa powder (>70%), and nuts such as almonds, peanuts pecans, cashews, and hazelnuts?';
UPDATE ag.survey_question SET japanese = 'あなたはインスタント料理（マカロニ・アンド・チーズ、ラーメン、Lean Cuisineなど）をどれくらい食べていますか？' WHERE american = 'How often do you consume ready-to-eat meals (e.g. macaroni and cheese, ramen noodles, lean cuisine)?';
UPDATE ag.survey_question SET japanese = '塩味のスナック（ポテトチップス、ナチョチップス、コーンチップス、バター付きのポップコーン、フライドポテトなど）はどれくらい食べますか？' WHERE american = 'How often do you consume salted snacks (potato chips, nacho chips, corn chips, popcorn with butter, French fries etc.)?';
UPDATE ag.survey_question SET japanese = '魚介類（魚、エビ、ロブスター、カニなど）はどれくらい食べますか？' WHERE american = 'How often do you consume seafood (fish, shrimp, lobster, crab, etc.)?';
UPDATE ag.survey_question SET japanese = '植物性加工タンパク質、豆腐、テンペ、大豆粉、大豆ナッツ、大豆バター、大豆、味噌（発酵大豆）などの大豆製品はどれくらい食べていますか？ ' WHERE american = 'How often do you consume soy products such as textured vegetable protein, tofu, tempeh, soybean flour, soy nuts, soy but butter, soybeans, and miso (i.e. fermented soy)? ';
UPDATE ag.survey_question SET japanese = '甘いお菓子（ケーキ、クッキー、ペイストリー、ドーナツ、マフィン、チョコレートなど）はどれくらい食べますか？ ' WHERE american = 'How often do you consume sugary sweets (cake, cookies, pastries, donuts, muffins, chocolate etc.) ';
UPDATE ag.survey_question SET japanese = '卵を丸ごと食べることはどれくらいありますか（卵泡立て器の使用や卵白のみのものは含まれません）？' WHERE american = 'How often do you consume whole eggs (does not include egg beaters or just egg whites).';
UPDATE ag.survey_question SET japanese = 'あなたはどれくらい家で料理を作って食べていますか？（箱入りのマカロニ・アンド・チーズ、ラーメン、Lean Cuisineなど、インスタント料理は除く）' WHERE american = 'How often do you cook and consume home cooked meals? (Exclude ready-to-eat meals like boxed macaroni and cheese, ramen noodles, lean cuisine)';
UPDATE ag.survey_question SET japanese = 'ラード、バター、またはギーで調理することはどれくらいありますか？' WHERE american = 'How often do you cook with lard, butter or ghee?';
UPDATE ag.survey_question SET japanese = 'オリーブオイルを使って調理することはどれくらいありますか。' WHERE american = 'How often do you cook with olive oil?';
UPDATE ag.survey_question SET japanese = '非ダイエットソーダやフルーツドリンク／パンチ（100 ％果汁のジュースは含まれません）などの砂糖入り飲料 を1日16オンス以上飲むことはどれくらいありますか？ （ソーダ1缶＝ 12オンス）' WHERE american = 'How often do you drink 16 ounces or more of sugar sweetened beverages such as non-diet soda or fruit drink/punch (not including 100 % fruit juice) in a day? (1 can of soda = 12 ounces)';
UPDATE ag.survey_question SET japanese = 'アルコールはどれくらい飲んでいますか？' WHERE american = 'How often do you drink alcohol?';
UPDATE ag.survey_question SET japanese = 'あなたが少なくとも1日2サービングの全粒穀物を食べることはどれくらいありますか？（ 1サービング＝スライス1枚分の全粒粉100 ％のパン；1カップ分のシレッデッド・フィート、ウィーティーズ、グレープ・ナッツ、高繊維シリアル、またはオートミールなどの全粒粉シリアル；全粒粉クラッカー3 ～ 4個；半カップ分の玄米または全粒粉パスタ）' WHERE american = 'How often do you eat at least 2 servings of whole grains in a day? (1 serving = 1 slice of 100% whole grain bread; 1 cup whole grain cereal like Shredded Wheat, Wheaties, Grape Nuts, high fiber cereals, or oatmeal; 3-4 whole grain crackers; ½ cup brown rice or whole wheat pasta)';
UPDATE ag.survey_question SET japanese = '持ち帰り／テイクアウト用のものも含め、店で調理された食べものをどれくらい食べていますか？' WHERE american = 'How often do you eat food prepared at a restaurant, including carry-out/take-out?';
UPDATE ag.survey_question SET japanese = '冷凍のデザート（アイスクリーム／ジェラート／ミルクシェイク、シャーベット／ソルベ、フローズンヨーグルトなど）はどれくらい食べていますか？' WHERE american = 'How often do you eat frozen desserts (ice cream/gelato/milkshakes, sherbet/sorbet, frozen yogurt, etc.)?';
UPDATE ag.survey_question SET japanese = '豆腐、テンペ、枝豆、レンズ豆、ひよこ豆、ピーナッツ、アーモンド、クルミ、キヌアなどの植物由来のタンパク質源はどれくらい食べていますか？' WHERE american = 'How often do you eat plant-based sources of protein including tofu, tempeh, edamame, lentils, chickpeas, peanuts, almonds, walnuts, or quinoa?';
UPDATE ag.survey_question SET japanese = '赤肉はどれくらい食べていますか。' WHERE american = 'How often do you eat red meat?';
UPDATE ag.survey_question SET japanese = 'どれくらい定期的に運動していますか？' WHERE american = 'How often do you exercise?';
UPDATE ag.survey_question SET japanese = 'どのような頻度で片頭痛がしますか？' WHERE american = 'How often do you experience migraines?';
UPDATE ag.survey_question SET japanese = '糸ようじ（デンタルフロス）はどれくらい使っていますか？' WHERE american = 'How often do you floss your teeth?';
UPDATE ag.survey_question SET japanese = 'タバコはどれくらい吸っていますか？' WHERE american = 'How often do you smoke cigarettes?';
UPDATE ag.survey_question SET japanese = 'どれくらい定期的にチームスポーツに参加していますか？' WHERE american = 'How often do you take part in team sports?';
UPDATE ag.survey_question SET japanese = '水泳用プール／ホットタブは、どのような頻度で使用していますか？' WHERE american = 'How often do you use a swimming pool/hot tub?';
UPDATE ag.survey_question SET japanese = 'ココナッツ油、パーム油、またはパーム核油を使用したり調理に使うことはどれくらいありますか？ ' WHERE american = 'How often do you use or cook with coconut, palm or palm kernel oil? ';
UPDATE ag.survey_question SET japanese = 'マーガリンや（野菜の）ショートニングを使用したり調理に使うことはどれくらいありますか？ ' WHERE american = 'How often do you use or cook with margarine or (vegetable) shortening? ';
UPDATE ag.survey_question SET japanese = '顔用の化粧品（日焼け止めやモイスチャライザーなどのスキンケア製品の使用も含める）はどれくらい使っていますか？' WHERE american = 'How often do you wear facial cosmetics (includes the use of skin care products like sunscreen or moisturizer)?';
UPDATE ag.survey_question SET japanese = '現在の睡眠パターンに関してどのように満足／不満足ですか？' WHERE american = 'How SATISFIED/DISSATISFIED are you with your CURRENT sleep pattern?';
UPDATE ag.survey_question SET japanese = 'それはどのように診断されましたか？' WHERE american = 'How was this diagnosed?';
UPDATE ag.survey_question SET japanese = 'その皮膚疾患はどのように診断されましたか？' WHERE american = 'How was your skin condition diagnosed?';
UPDATE ag.survey_question SET japanese = '母乳と粉ミルクのどちらで育ちましたか？' WHERE american = 'How were you fed as an infant?';
UPDATE ag.survey_question SET japanese = 'あなたが現在持っている睡眠の問題について、どの程度の心配／不安がありますか？' WHERE american = 'How WORRIED/DISTRESSED are you about your current sleep problem?';
UPDATE ag.survey_question SET japanese = 'あなたは自分の食習慣をどのように分類しますか？' WHERE american = 'How would you classify your diet?';
UPDATE ag.survey_question SET japanese = '私は過去____________の期間にインフルエンザワクチンを接種しました。' WHERE american = 'I have received a flu vaccine in the last ____________.';
UPDATE ag.survey_question SET japanese = '私は過去____________の期間に抗生物質を服用しました。' WHERE american = 'I have taken antibiotics in the last ____________.';
UPDATE ag.survey_question SET japanese = '私は過去＿＿＿の期間に、アメリカ合衆国外に旅行したことがあります。' WHERE american = 'I have traveled outside of the United States in the past _________.';
UPDATE ag.survey_question SET japanese = '上記のいずれかの症状があった場合、症状があった間は仕事を休んで自宅で過ごしていましたか？' WHERE american = 'If yes to any symptoms above, did you stay home from work while symptomatic?';
UPDATE ag.survey_question SET japanese = '質問24および／または25の回答が「はい」の場合、定期的に摂取するノンカロリーまたは低カロリーの甘味料はどのような種類のものですか？該当するものをすべて選択してください。' WHERE american = 'If you answered yes to Question 24 and/or 25, what type of non-nutritive or low-calorie sweetener(s) do you consume on a regular basis? Select all that apply.';
UPDATE ag.survey_question SET japanese = '前の質問への回答が「はい」の場合、症状は何ですか？該当するものをすべて選択してください。' WHERE american = 'If you answered yes to the previous question, what are the symptoms? Select all that apply.';
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どのタイプのIBDですか？' WHERE american = 'If you answered yes, which type of IBD do you have?';
UPDATE ag.survey_question SET japanese = '特殊な食習慣をとっている場合、それはどのような種類のものですか？該当するものをすべて選択してください。' WHERE american = 'If you eat a specialized diet, what type do you follow? Select all that apply.';
UPDATE ag.survey_question SET japanese = '断続的な断食をする場合、どのよう種類の断食をしますか？' WHERE american = 'If you practice intermittent fasting, what type do you follow?';
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どのタイプの糖尿病かを選択してください：' WHERE american = 'If you responded “Yes”, select which type of diabetes';
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どの障害かを次のリストから選択してください：' WHERE american = 'If you responded “yes”, please select which disorder(s) from the following list';
UPDATE ag.survey_question SET japanese = '繊維サプリメントを服用する場合、どのような種類のものを服用していますか？該当するものをすべて選択してください。' WHERE american = 'If you take a fiber supplement, what kind do you take? Select all that apply.';
UPDATE ag.survey_question SET japanese = '電話やノートパソコンなどの発光電子機器を寝る直前に使用する場合、ナイトモードまたはダークモードで使用していますか？' WHERE american = 'If you use light emitting electronic devices such as a phone or laptop right before bed, do you use it in night or dark mode?';
UPDATE ag.survey_question SET japanese = '普通の1週間に何種類の植物を食べていますか？たとえば、ニンジン、ジャガイモ、タマネギを含む缶詰スープを食べた場合、3種類別々の植物として数えることができます。マルチグレインのパンを摂取した場合、それぞれの穀物を別々の植物として数えます。すべての果物を合計に含めてください。' WHERE american = 'In an average week, how many different plants do you eat? For example - if you consume a can of soup that contains carrots, potatoes and onion, you can count this as 3 different plants; If you consume multi-grain bread, each different grain counts as a plant. Include all fruits in the total.';
UPDATE ag.survey_question SET japanese = '普通の1週間に、繊維含有量の多い強化食品（例： Fiber One ）はどれくらい食べていますか？' WHERE american = 'In an average week, how often do you eat foods that are fortified with high fiber content (e.g. Fiber One)?';
UPDATE ag.survey_question SET japanese = '過去6ヶ月以内に私の体重は_________しました。' WHERE american = 'My weight has _________ within the last 6 months.';
UPDATE ag.survey_question SET japanese = '氏名' WHERE american = 'Name';
UPDATE ag.survey_question SET japanese = '次のうち、片頭痛に伴う全ての症状にチェックを入れてください。' WHERE american = 'Of the following check all the symptoms you experience with a migraine';
UPDATE ag.survey_question SET japanese = '過去1ヶ月間におけるあなたの平均的なストレスレベルを、1を「ストレスがほとんどまたは全くない」、10を「かなりのストレス」とした10段階で評価してください。' WHERE american = 'On a scale of 1 to 10, where 1 means you have "little or no stress" and 10 means you have "a great deal of stress," how would you rate your average level of stress during the past month?';
UPDATE ag.survey_question SET japanese = '学校や仕事がある日は、朝何時に起きますか？' WHERE american = 'On days you have school or work, what time do you get up in the morning?';
UPDATE ag.survey_question SET japanese = '学校や仕事がある前の夜は、何時に寝ますか？' WHERE american = 'On nights before you have school or work, what time do you go to bed?';
UPDATE ag.survey_question SET japanese = '休みの日（学校や仕事がない日）の前の夜は、何時に寝ますか？' WHERE american = 'On nights before your off days (days when you do not have school or work), what time do you go to bed?';
UPDATE ag.survey_question SET japanese = '休みの日（学校や仕事がない日）は、朝何時に起きますか？ ' WHERE american = 'On your off days (days when you do not have school or work), what time do you get up in the morning? ';
UPDATE ag.survey_question SET japanese = '過去2週間の間、落ち込んだり、憂うつになったり、絶望したりすることがどれくらいありましたか？' WHERE american = 'Over the last 2 weeks, how often have you been bothered by feeling down, depressed or hopeless?';
UPDATE ag.survey_question SET japanese = '過去2週間の間に、緊張したり、不安を感じたり、いらいらしたりすることがどれくらいありましたか？' WHERE american = 'Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?';
UPDATE ag.survey_question SET japanese = '過去2週間の間、何かをする興味や楽しみがほとんどなくてつらいと思ったことがどれくらいありましたか？' WHERE american = 'Over the last 2 weeks, how often have you been bothered by little interest or pleasure in doing things?';
UPDATE ag.survey_question SET japanese = '過去2週間の間に、心配するのを止めたりコントロールできなかったりしたことがどれくらいありましたか？' WHERE american = 'Over the last 2 weeks, how often have you been bothered by not being able to stop or control worrying?';
UPDATE ag.survey_question SET japanese = '過去1週間に、腹部膨満感が起こったことはどれくらいありましたか？' WHERE american = 'Over the last week, how frequently have you had abdominal bloating?';
UPDATE ag.survey_question SET japanese = '過去1週間に、腹痛や腹部不快感を感じたことはどれくらいありましたか？' WHERE american = 'Over the last week, how frequently have you had abdominal pain or abdominal discomfort?';
UPDATE ag.survey_question SET japanese = '過去1週間で、お腹が鳴る／胃が鳴ることはどれくらいありましたか？' WHERE american = 'Over the last week, how frequently have you had borborygmi / rumbling stomach?';
UPDATE ag.survey_question SET japanese = '過去1週間に、膨満感（おならが出る）を感じたことはどれくらいありましたか？' WHERE american = 'Over the last week, how frequently have you had flatulence (passage of gas)?';
UPDATE ag.survey_question SET japanese = '過去1週間の睡眠の質はどんなでしたか？' WHERE american = 'Over the past week, how would you rate your sleep quality?';
UPDATE ag.survey_question SET japanese = '参加者名' WHERE american = 'Participant name';
UPDATE ag.survey_question SET japanese = '上記に記載されていないその他の特殊な食事制限があったら列挙／説明してください。' WHERE american = 'Please list/describe any other special diet restrictions you follow that are not indicated above.';
UPDATE ag.survey_question SET japanese = '片頭痛を起こす主な原因を、「1」が最も可能性が高い、「2」が2番目に可能性が高いとして、ランク付けしてください。片頭痛を引き起こす原因でないものは、空白のままにしておいてください。' WHERE american = 'Please rank the main factors that lead to your migraines, where “1” is most likely, “2” is second most likely, etc.  If the factor does not cause migraines leave blank';
UPDATE ag.survey_question SET japanese = '眠りにつけないことについて現在（過去2週間）どれくらい重症かを評価してください。' WHERE american = 'Please rate the CURRENT (i.e. LAST 2 WEEKS) SEVERITY of any difficulty falling asleep.';
UPDATE ag.survey_question SET japanese = '眠りが浅いことについて現在（過去2週間）どれくらい重症かを評価してください。' WHERE american = 'Please rate the CURRENT (i.e. LAST 2 WEEKS) SEVERITY of any difficulty staying asleep.';
UPDATE ag.survey_question SET japanese = '目覚めが早すぎることについて現在（過去2週間）どれくらい重症かを評価してください。' WHERE american = 'Please rate the CURRENT (i.e. LAST 2 WEEKS) SEVERITY of any problems waking up too early.';
UPDATE ag.survey_question SET japanese = 'あなたの現在の幸福状態について考えてください。幸福について考えるときは、あなたの身体的健康、感情的健康、あなたが経験しているあらゆる課題、あなたの人生の人々、あなたが利用できる機会や資源について考えてください。現在の幸福状態をどんなふうに言い表しますか？' WHERE american = 'Please think about your current level of well-being. When you think about well-being, think about your physical health, your emotional health, any challenges you are experiencing, the people in your life, and the opportunities or resources you have available to you. How would you describe your current level of well-being?';
UPDATE ag.survey_question SET japanese = '出産予定日：' WHERE american = 'Pregnancy due date';
UPDATE ag.survey_question SET japanese = 'この人は私の：' WHERE american = 'This person is my';
UPDATE ag.survey_question SET japanese = 'あなたの睡眠の問題が日常活動を現在どの程度妨げていると思いますか（例：昼間の疲労、気分、職場での作業／日常の家事を行う能力、集中力、記憶力、気分など）？' WHERE american = 'To what extent do you consider your sleep problem to INTERFERE with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) CURRENTLY?';
UPDATE ag.survey_question SET japanese = '種類／商品名：' WHERE american = 'Type/brand';
UPDATE ag.survey_question SET japanese = '体重' WHERE american = 'Weight';
UPDATE ag.survey_question SET japanese = 'あなたは帝王切開（ Cセクション）によって生まれましたか？' WHERE american = 'Were you born via cesarean section (C-section)?';
UPDATE ag.survey_question SET japanese = 'どのような病状ですか？' WHERE american = 'What condition(s)?';
UPDATE ag.survey_question SET japanese = 'あなたはどの食物に対してアレルギーがありますか？該当するものをすべて選択してください。' WHERE american = 'What foods are you allergic to? Select all that apply.';
UPDATE ag.survey_question SET japanese = '通常、どれくらい激しい運動をしますか？該当するものをすべて選択してください。' WHERE american = 'What intensity of exercise do you typically do? Select all that apply.';
UPDATE ag.survey_question SET japanese = 'あなたの最終学歴は何ですか？' WHERE american = 'What is your highest level of education?';
UPDATE ag.survey_question SET japanese = 'あなたの職業は何ですか？' WHERE american = 'What is your occupation?';
UPDATE ag.survey_question SET japanese = 'この研究に参加していて、そのことをあなたに自発的に伝えた人々と、あなたとの関係（パートナー、子供など）をお答えください。 両方の人が同じことを答えた情報のみが使用されることに注意してください。私たちの遺伝子が私たちのマイクロバイオームに影響を与えることが研究により示されているため、この情報は有用です。' WHERE american = 'What is your relationship to those in this study who have voluntarily told you of their participation (e.g. partner, children)? Note that we will only use information that both parties provide. This information is useful because studies have shown that our genes affect our microbiome.';
UPDATE ag.survey_question SET japanese = 'どのような皮膚疾患と診断されましたか？' WHERE american = 'What kind of skin condition have you been diagnosed with?';
UPDATE ag.survey_question SET japanese = 'どのような種類の抗生物質を服用しましたか？' WHERE american = 'What type of antibiotic did you take?';
UPDATE ag.survey_question SET japanese = '通常、どのような運動をしますか？該当するものをすべて選択してください。' WHERE american = 'What type of exercise do you typically do? Select all that apply.';
UPDATE ag.survey_question SET japanese = '通常、どのような種類のアルコールを飲みますか？該当するものをすべて選択してください。' WHERE american = 'What type(s) of alcohol do you typically consume? Select all that apply.';
UPDATE ag.survey_question SET japanese = 'どのような種類のペットですか？' WHERE american = 'What type(s) of pets?';
UPDATE ag.survey_question SET japanese = 'どのような種類のサプリメントですか？' WHERE american = 'What types of supplements?';
UPDATE ag.survey_question SET japanese = '治療に使用された抗生物質は何ですか？' WHERE american = 'What was the antibiotic used to treat?';
UPDATE ag.survey_question SET japanese = '現在の居住地（州）に移動したのはいつですか？' WHERE american = 'When did you move to your current location of residence (state)?';
UPDATE ag.survey_question SET japanese = '発酵食品を食べ始めたのはいつですか？' WHERE american = 'When did you start eating fermented foods?';
UPDATE ag.survey_question SET japanese = '毎日のカロリーのほとんどはいつ摂取しますか？' WHERE american = 'When do you consume most of your daily calories?';
UPDATE ag.survey_question SET japanese = '園芸や庭仕事をする回数は、シーズン中どれくらいですか？' WHERE american = 'When the season allows, how often do you garden or do yard work?';
UPDATE ag.survey_question SET japanese = 'ノンカロリーまたは低カロリーの甘味料を含む食品や飲料を摂取した場合、その後、ガス、膨張、下痢などの消化器の不具合が起きることがよくありますか？ ' WHERE american = 'When you consume foods or beverages containing non-nutritive or low-calorie sweeteners, do you tend to experience gastrointestinal disorders afterwards, such as gas, bloating, and/or diarrhea? ';
UPDATE ag.survey_question SET japanese = '自宅の外で水を飲む前に、追加の処理（沸騰、浄化錠、塩素/漂白剤など）を施しますか ？' WHERE american = 'When you’re outside the home, do you apply additional treatment to your drinking water prior to consumption (e.g., boiling, purification tablet, chlorine/bleach)?';
UPDATE ag.survey_question SET japanese = '自宅の外で飲む、味のついていない普通の飲料水は主にどういうものですか？これには静水または発泡水／炭酸水も含められます。' WHERE american = 'When you''re outside the home, what is the main source of your plain unflavored drinking water? This can include still or sparkling/carbonated water.';
UPDATE ag.survey_question SET japanese = 'あなたの猫は主にどこにいますか？' WHERE american = 'Where does your cat(s) mostly stay?';
UPDATE ag.survey_question SET japanese = 'あなたの犬は主にどこにいますか？' WHERE american = 'Where does your dog(s) mostly stay?';
UPDATE ag.survey_question SET japanese = 'あなたの利き手はどちらですか？' WHERE american = 'Which is your dominant hand?';
UPDATE ag.survey_question SET japanese = 'どのような種類のがんを患っています／いましたか？該当するものをすべて選択してください。' WHERE american = 'Which kind of cancer(s) did you / do you have? Select all that apply.';
UPDATE ag.survey_question SET japanese = 'どんな薬を服用していますか？' WHERE american = 'Which medications are you taking?';
UPDATE ag.survey_question SET japanese = 'お住まいの地域に最も当てはまるのは、次のうちどれですか？' WHERE american = 'Which of the following best describes the area in which you live?';
UPDATE ag.survey_question SET japanese = '次のうち、ご自身に最もあてはまるものはどれでしょうか？' WHERE american = 'Which of the following best describes you?';
UPDATE ag.survey_question SET japanese = '次の発酵食品／飲料のうち、週に1回以上摂取するのはどれですか？該当するものをすべて選択し、記載されていないものを「その他」に記入してください。' WHERE american = 'Which of the following fermented foods/beverages do you consume more than once a week? Select all that apply and write in any that are not listed under ‘Other’.';
UPDATE ag.survey_question SET japanese = 'どのタイプの治療を受け／利用しましたか？該当するものをすべて選択してください。' WHERE american = 'Which types of treatment(s) did you take/use? Select all that apply.';
UPDATE ag.survey_question SET japanese = 'この研究に参加していて、そのことをあなたに自発的に伝えた同居人は誰ですか？ 両方の人が同じことを答えた情報のみが使用されることに注意してください。私たちと一緒に住んでいる人々が私たちのマイクロバイオームに影響を与えることが研究により示されているため、この情報は有用です。' WHERE american = 'Who are your roommates who have voluntarily told you of their participation in this study? Note that we will only use information that both parties provide. This information is useful because studies have shown that the people we live with affect our microbiome.';


-- Add the Japanese text for survey responses
UPDATE ag.survey_response SET japanese = '< 4液量オンス（< 118 ml ）' WHERE american = '<4 fl oz (<118 ml)';
UPDATE ag.survey_response SET japanese = '> 20液量オンス（> 591 ml）' WHERE american = '>20 fl oz (>591 ml)';
UPDATE ag.survey_response SET japanese = '1年' WHERE american = '1 year';
UPDATE ag.survey_response SET japanese = '週に1 ～ 2日' WHERE american = '1-2 days per week';
UPDATE ag.survey_response SET japanese = '週に１〜２回' WHERE american = '1-2 times/week';
UPDATE ag.survey_response SET japanese = '12 ～ 16液量オンス（355 ～ 473 ml）' WHERE american = '12-16 fl oz (355-473 ml)';
UPDATE ag.survey_response SET japanese = '16 ～ 20液量オンス（473 ～ 591 ml）' WHERE american = '16-20 fl oz (473-591 ml)';
UPDATE ag.survey_response SET japanese = '1日2回' WHERE american = '2 times a day';
UPDATE ag.survey_response SET japanese = '21～30種類' WHERE american = '21-30';
UPDATE ag.survey_response SET japanese = '週に2～3日' WHERE american = '2-3 days per week';
UPDATE ag.survey_response SET japanese = '２４時間断食（別名、イート・ストップ・イート法）' WHERE american = '24 hour fast (aka eat-stop-eat method)';
UPDATE ag.survey_response SET japanese = '3ヶ月' WHERE american = '3 months';
UPDATE ag.survey_response SET japanese = '週に３〜５回' WHERE american = '3-5 times/week';
UPDATE ag.survey_response SET japanese = '週に4～6日' WHERE american = '4-6 days per week';
UPDATE ag.survey_response SET japanese = '4〜8液量オンス（118〜237 ml）' WHERE american = '4-8 fl oz (118-237 ml)';
UPDATE ag.survey_response SET japanese = '５：２方法' WHERE american = '5:2 method';
UPDATE ag.survey_response SET japanese = '6ヶ月' WHERE american = '6 months';
UPDATE ag.survey_response SET japanese = '8〜12液量オンス（237〜355 ml）' WHERE american = '8-12 fl oz (237-355 ml)';
UPDATE ag.survey_response SET japanese = '週にわずかな日数' WHERE american = 'A few days per week';
UPDATE ag.survey_response SET japanese = '年に数回' WHERE american = 'A few times a year';
UPDATE ag.survey_response SET japanese = '少し心配' WHERE american = 'A little worried';
UPDATE ag.survey_response SET japanese = '母乳と調整粉乳の両方' WHERE american = 'A mixture of breast milk and formula';
UPDATE ag.survey_response SET japanese = 'アセスルファムカリウム' WHERE american = 'Acesulfame potassium';
UPDATE ag.survey_response SET japanese = '身体活動／運動' WHERE american = 'Activity/exercise';
UPDATE ag.survey_response SET japanese = '副腎がん' WHERE american = 'Adrenal cancer';
UPDATE ag.survey_response SET japanese = 'エアロビック／有酸素トレーニング' WHERE american = 'Aerobic/cardio training';
UPDATE ag.survey_response SET japanese = 'アフガニスタン' WHERE american = 'Afghanistan';
UPDATE ag.survey_response SET japanese = 'オーランド諸島' WHERE american = 'Aland Islands';
UPDATE ag.survey_response SET japanese = 'アルバニア' WHERE american = 'Albania';
UPDATE ag.survey_response SET japanese = 'アルジェリア' WHERE american = 'Algeria';
UPDATE ag.survey_response SET japanese = '隔日断食' WHERE american = 'Alternate day fasting';
UPDATE ag.survey_response SET japanese = 'アメリカ領サモア' WHERE american = 'American Samoa';
UPDATE ag.survey_response SET japanese = 'アンドラ' WHERE american = 'Andorra';
UPDATE ag.survey_response SET japanese = 'アンゴラ' WHERE american = 'Angola';
UPDATE ag.survey_response SET japanese = 'アンギラ' WHERE american = 'Anguilla';
UPDATE ag.survey_response SET japanese = '神経性無食欲症' WHERE american = 'Anorexia nervosa';
UPDATE ag.survey_response SET japanese = '南極' WHERE american = 'Antarctica';
UPDATE ag.survey_response SET japanese = 'アンティグア・バーブーダ' WHERE american = 'Antigua and Barbuda';
UPDATE ag.survey_response SET japanese = '自己免疫障害' WHERE american = 'Any autoimmune disease';
UPDATE ag.survey_response SET japanese = 'リンゴの食物繊維*' WHERE american = 'Apple fiber*';
UPDATE ag.survey_response SET japanese = '4月' WHERE american = 'April';
UPDATE ag.survey_response SET japanese = 'アルゼンチン' WHERE american = 'Argentina';
UPDATE ag.survey_response SET japanese = 'アルメニア' WHERE american = 'Armenia';
UPDATE ag.survey_response SET japanese = '関節炎' WHERE american = 'Arthritis';
UPDATE ag.survey_response SET japanese = 'アルバ' WHERE american = 'Aruba';
UPDATE ag.survey_response SET japanese = 'アジア人' WHERE american = 'Asian';
UPDATE ag.survey_response SET japanese = 'アスパルターム' WHERE american = 'Aspartame';
UPDATE ag.survey_response SET japanese = '準学士号（AA、ASなど）' WHERE american = '"Associate’s degree (e.g. AA, AS))"';
UPDATE ag.survey_response SET japanese = '喘息または他の肺疾患' WHERE american = 'Asthma or other lung problems';
UPDATE ag.survey_response SET japanese = '心房細動または心房粗動' WHERE american = 'Atrial Fibrillation or Atrial Flutter';
UPDATE ag.survey_response SET japanese = '8月' WHERE american = 'August';
UPDATE ag.survey_response SET japanese = 'オーラ' WHERE american = 'Aura';
UPDATE ag.survey_response SET japanese = 'オーストラリア' WHERE american = 'Australia';
UPDATE ag.survey_response SET japanese = 'オーストリア' WHERE american = 'Austria';
UPDATE ag.survey_response SET japanese = 'アゼルバイジャン' WHERE american = 'Azerbaijan';
UPDATE ag.survey_response SET japanese = '学士号（BA、BSなど）' WHERE american = '"Bachelor’s degree (e.g. BA, BS)"';
UPDATE ag.survey_response SET japanese = 'バハマ諸島' WHERE american = 'Bahamas';
UPDATE ag.survey_response SET japanese = 'バーレーン' WHERE american = 'Bahrain';
UPDATE ag.survey_response SET japanese = 'バランストレーニング' WHERE american = 'Balance training';
UPDATE ag.survey_response SET japanese = 'バングラデシュ' WHERE american = 'Bangladesh';
UPDATE ag.survey_response SET japanese = 'バルバドス' WHERE american = 'Barbados';
UPDATE ag.survey_response SET japanese = 'ほとんどわからない' WHERE american = 'Barely noticeable';
UPDATE ag.survey_response SET japanese = '蜂刺され' WHERE american = 'Bee stings';
UPDATE ag.survey_response SET japanese = 'ビール' WHERE american = 'Beer';
UPDATE ag.survey_response SET japanese = 'ベラルーシ' WHERE american = 'Belarus';
UPDATE ag.survey_response SET japanese = 'ベルギー' WHERE american = 'Belgium';
UPDATE ag.survey_response SET japanese = 'ベリーズ' WHERE american = 'Belize';
UPDATE ag.survey_response SET japanese = 'ベナン' WHERE american = 'Benin';
UPDATE ag.survey_response SET japanese = 'バミューダ' WHERE american = 'Bermuda';
UPDATE ag.survey_response SET japanese = 'ブータン' WHERE american = 'Bhutan';
UPDATE ag.survey_response SET japanese = '双極性障害' WHERE american = 'Bipolar disorder';
UPDATE ag.survey_response SET japanese = '黒人またはアフリカ系アメリカ人' WHERE american = 'Black or African American';
UPDATE ag.survey_response SET japanese = '膀胱がん' WHERE american = 'Bladder cancer';
UPDATE ag.survey_response SET japanese = 'ないはずの体の部分に痛みがある；' WHERE american = 'Body pain where it shouldn’t exist;';
UPDATE ag.survey_response SET japanese = 'ボリビア' WHERE american = 'Bolivia';
UPDATE ag.survey_response SET japanese = 'ボスニア・ヘルツェゴビナ' WHERE american = 'Bosnia and Herzegovina';
UPDATE ag.survey_response SET japanese = '両方' WHERE american = 'Both';
UPDATE ag.survey_response SET japanese = '両方とも同じくらい' WHERE american = 'Both equally';
UPDATE ag.survey_response SET japanese = 'ボツワナ' WHERE american = 'Botswana';
UPDATE ag.survey_response SET japanese = '瓶詰めされた*精製水（ラベルに「湧き水」あるいは「天然ミネラルウォーター」とは表示されていない）' WHERE american = 'Bottled* purified water (does not indicate “spring water” or “natural mineral water” on the label)';
UPDATE ag.survey_response SET japanese = 'ブーベ島' WHERE american = 'Bouvet Island';
UPDATE ag.survey_response SET japanese = '脳がん（神経膠腫および神経膠芽腫を含む）' WHERE american = 'Brain cancer (includes gliomas and glioblastomas)';
UPDATE ag.survey_response SET japanese = 'ブラジル' WHERE american = 'Brazil';
UPDATE ag.survey_response SET japanese = '乳がん' WHERE american = 'Breast cancer';
UPDATE ag.survey_response SET japanese = 'イギリス領インド洋地域' WHERE american = 'British Indian Ocean Territory';
UPDATE ag.survey_response SET japanese = 'ブルネイ・ダルサラーム' WHERE american = 'Brunei Darussalam';
UPDATE ag.survey_response SET japanese = 'ブルガリア' WHERE american = 'Bulgaria';
UPDATE ag.survey_response SET japanese = '神経性過食症' WHERE american = 'Bulimia nervosa';
UPDATE ag.survey_response SET japanese = 'ブルキナファソ' WHERE american = 'Burkina Faso';
UPDATE ag.survey_response SET japanese = 'ブルンジ' WHERE american = 'Burundi';
UPDATE ag.survey_response SET japanese = 'カフェイン________' WHERE american = 'Caffeine________';
UPDATE ag.survey_response SET japanese = 'カロリーは1日にわたって均等に分配している' WHERE american = 'Calories are evenly distributed throughout the day';
UPDATE ag.survey_response SET japanese = 'カンボジア' WHERE american = 'Cambodia';
UPDATE ag.survey_response SET japanese = 'カメルーン' WHERE american = 'Cameroon';
UPDATE ag.survey_response SET japanese = 'カナダ' WHERE american = 'Canada';
UPDATE ag.survey_response SET japanese = 'がん' WHERE american = 'Cancer';
UPDATE ag.survey_response SET japanese = 'カーボベルデ' WHERE american = 'Cape Verde';
UPDATE ag.survey_response SET japanese = 'ケイマン諸島' WHERE american = 'Cayman Islands';
UPDATE ag.survey_response SET japanese = 'センチメートル' WHERE american = 'centimeters';
UPDATE ag.survey_response SET japanese = '中央アフリカ共和国' WHERE american = 'Central African Republic';
UPDATE ag.survey_response SET japanese = '子宮頸がん' WHERE american = 'Cervical cancer';
UPDATE ag.survey_response SET japanese = 'チャド' WHERE american = 'Chad';
UPDATE ag.survey_response SET japanese = '化学療法' WHERE american = 'Chemotherapy';
UPDATE ag.survey_response SET japanese = '胸部の痛みまたは圧迫感' WHERE american = 'Chest pain or tightness in chest';
UPDATE ag.survey_response SET japanese = 'チチャ' WHERE american = 'Chicha';
UPDATE ag.survey_response SET japanese = 'チリ' WHERE american = 'Chile';
UPDATE ag.survey_response SET japanese = '中国' WHERE american = 'China';
UPDATE ag.survey_response SET japanese = '胆管がん' WHERE american = 'Cholangiocarcinoma';
UPDATE ag.survey_response SET japanese = 'クリスマス島' WHERE american = 'Christmas Island';
UPDATE ag.survey_response SET japanese = '慢性閉塞性肺疾患（Chronic Obstructive Pulmonary Disease、COPD）' WHERE american = 'Chronic Obstructive Pulmonary Disease (COPD)';
UPDATE ag.survey_response SET japanese = 'シードル' WHERE american = 'Cider';
UPDATE ag.survey_response SET japanese = '都市（人口10万人超、100万人未満）' WHERE american = '"City (population is more than 100,000 and less than 1 million)"';
UPDATE ag.survey_response SET japanese = 'ココス（キーリング）諸島' WHERE american = 'Cocos (Keeling) Islands';
UPDATE ag.survey_response SET japanese = '大学の学位' WHERE american = 'College degree';
UPDATE ag.survey_response SET japanese = 'コロンビア' WHERE american = 'Colombia';
UPDATE ag.survey_response SET japanese = '結腸がん' WHERE american = 'Colon cancer';
UPDATE ag.survey_response SET japanese = '結腸クローン病' WHERE american = 'Colonic Crohn''s disease';
UPDATE ag.survey_response SET japanese = 'コモロ' WHERE american = 'Comoros';
UPDATE ag.survey_response SET japanese = 'うっ血性心不全' WHERE american = 'Congestive Heart Failure';
UPDATE ag.survey_response SET japanese = 'コンゴ' WHERE american = 'Congo';
UPDATE ag.survey_response SET japanese = 'コンゴ民主共和国' WHERE american = '"Congo, The Democratic Republic of The"';
UPDATE ag.survey_response SET japanese = '便秘' WHERE american = 'Constipation';
UPDATE ag.survey_response SET japanese = 'クック諸島' WHERE american = 'Cook Islands';
UPDATE ag.survey_response SET japanese = 'コスタリカ' WHERE american = 'Costa Rica';
UPDATE ag.survey_response SET japanese = 'コートジボワール' WHERE american = 'Cote D''ivoire';
UPDATE ag.survey_response SET japanese = 'カッテージチーズ' WHERE american = 'Cottage cheese';
UPDATE ag.survey_response SET japanese = '咳' WHERE american = 'Cough';
UPDATE ag.survey_response SET japanese = 'クロアチア' WHERE american = 'Croatia';
UPDATE ag.survey_response SET japanese = 'キューバ' WHERE american = 'Cuba';
UPDATE ag.survey_response SET japanese = '現在幼稚園〜高等学校' WHERE american = 'Currently in K-12';
UPDATE ag.survey_response SET japanese = 'キプロス' WHERE american = 'Cyprus';
UPDATE ag.survey_response SET japanese = 'チェコ共和国' WHERE american = 'Czech Republic';
UPDATE ag.survey_response SET japanese = '毎日' WHERE american = 'Daily';
UPDATE ag.survey_response SET japanese = '毎日の時間制限付き断食（time-restricted eating、TRE）' WHERE american = 'Daily time-restricted eating (TRE)';
UPDATE ag.survey_response SET japanese = '12月' WHERE american = 'December';
UPDATE ag.survey_response SET japanese = '10ポンド以上減少' WHERE american = 'Decreased more than 10 pounds';
UPDATE ag.survey_response SET japanese = '深部静脈血栓症' WHERE american = 'Deep vein thrombosis';
UPDATE ag.survey_response SET japanese = 'デンマーク' WHERE american = 'Denmark';
UPDATE ag.survey_response SET japanese = '季節による' WHERE american = 'Depends on the season';
UPDATE ag.survey_response SET japanese = '抑うつ' WHERE american = 'Depression';
UPDATE ag.survey_response SET japanese = '抑うつ______' WHERE american = 'Depression______';
UPDATE ag.survey_response SET japanese = '糖尿病または高血糖' WHERE american = 'Diabetes or high blood sugar';
UPDATE ag.survey_response SET japanese = '医療専門家（医師、医師助手）によって診断されました。' WHERE american = '"Diagnosed by a medical professional (doctor, physician assistant)"';
UPDATE ag.survey_response SET japanese = '代替医療の医師によって診断されました。' WHERE american = 'Diagnosed by an alternative medicine practitioner';
UPDATE ag.survey_response SET japanese = '下痢' WHERE american = 'Diarrhea';
UPDATE ag.survey_response SET japanese = '飲食物' WHERE american = 'Diet';
UPDATE ag.survey_response SET japanese = '不満である' WHERE american = 'Dissatisfied';
UPDATE ag.survey_response SET japanese = 'ジブチ' WHERE american = 'Djibouti';
UPDATE ag.survey_response SET japanese = '博士号（例：PhD、EdD）' WHERE american = '"Doctorate (eg. PhD, EdD)"';
UPDATE ag.survey_response SET japanese = 'ドミニカ' WHERE american = 'Dominica';
UPDATE ag.survey_response SET japanese = 'ドミニカ共和国' WHERE american = 'Dominican Republic';
UPDATE ag.survey_response SET japanese = '薬物（例：ペニシリン）' WHERE american = 'Drug (e.g. Penicillin)';
UPDATE ag.survey_response SET japanese = 'エクアドル' WHERE american = 'Ecuador';
UPDATE ag.survey_response SET japanese = 'エジプト' WHERE american = 'Egypt';
UPDATE ag.survey_response SET japanese = 'エルサルバドル' WHERE american = 'El Salvador';
UPDATE ag.survey_response SET japanese = 'てんかんまたは発作' WHERE american = 'Epilepsy or seizures';
UPDATE ag.survey_response SET japanese = '赤道ギニア' WHERE american = 'Equatorial Guinea';
UPDATE ag.survey_response SET japanese = 'エリトリア' WHERE american = 'Eritrea';
UPDATE ag.survey_response SET japanese = '食道がん' WHERE american = 'Esophageal cancer';
UPDATE ag.survey_response SET japanese = 'エストニア' WHERE american = 'Estonia';
UPDATE ag.survey_response SET japanese = 'エチオピア' WHERE american = 'Ethiopia';
UPDATE ag.survey_response SET japanese = '毎日' WHERE american = 'Every day';
UPDATE ag.survey_response SET japanese = 'すばらしい' WHERE american = 'Excellent';
UPDATE ag.survey_response SET japanese = '乳製品除去食' WHERE american = 'Exclude dairy';
UPDATE ag.survey_response SET japanese = 'ナス科除去食' WHERE american = 'Exclude nightshades';
UPDATE ag.survey_response SET japanese = '精製糖除去食' WHERE american = 'Exclude refined sugars';
UPDATE ag.survey_response SET japanese = 'まあまあ' WHERE american = 'Fair';
UPDATE ag.survey_response SET japanese = 'フォークランド諸島（マルビナス）' WHERE american = 'Falkland Islands (Malvinas)';
UPDATE ag.survey_response SET japanese = '体調を崩した' WHERE american = 'Fallen ill physically';
UPDATE ag.survey_response SET japanese = 'フェロー諸島' WHERE american = 'Faroe Islands';
UPDATE ag.survey_response SET japanese = '疲労' WHERE american = 'Fatigue';
UPDATE ag.survey_response SET japanese = '2月' WHERE american = 'February';
UPDATE ag.survey_response SET japanese = '女性' WHERE american = 'Female';
UPDATE ag.survey_response SET japanese = '発酵豆／味噌／納豆' WHERE american = 'Fermented beans/Miso/Natto';
UPDATE ag.survey_response SET japanese = '発酵パン／サワードウ／インジェラ' WHERE american = 'Fermented bread/sourdough/injera';
UPDATE ag.survey_response SET japanese = '発酵魚' WHERE american = 'Fermented fish';
UPDATE ag.survey_response SET japanese = '腐乳' WHERE american = 'Fermented tofu';
UPDATE ag.survey_response SET japanese = '発熱' WHERE american = 'Fever';
UPDATE ag.survey_response SET japanese = '月に数回' WHERE american = 'Few times/month';
UPDATE ag.survey_response SET japanese = '年に数回' WHERE american = 'Few times/year';
UPDATE ag.survey_response SET japanese = 'フィジー' WHERE american = 'Fiji';
UPDATE ag.survey_response SET japanese = 'ろ過された水道水（ピッチャー、蛇口または流し台下の浄水器、逆浸透システム、軟水器）' WHERE american = '"Filtered tap water (pitcher, faucet or under the sink water purifiers, reverse osmosis systems, water softener)"';
UPDATE ag.survey_response SET japanese = 'フィンランド' WHERE american = 'Finland';
UPDATE ag.survey_response SET japanese = '魚醤' WHERE american = 'Fish sauce';
UPDATE ag.survey_response SET japanese = '柔軟性トレーニング' WHERE american = 'Flexibility training';
UPDATE ag.survey_response SET japanese = 'フォドマップ（FODMAP）' WHERE american = 'FODMAP';
UPDATE ag.survey_response SET japanese = '食品（ワイン、チョコレート、イチゴ） _________' WHERE american = '"Foods (wine, chocolate,strawberries)_________"';
UPDATE ag.survey_response SET japanese = '強化ワイン' WHERE american = 'Fortified wine';
UPDATE ag.survey_response SET japanese = 'フランス' WHERE american = 'France';
UPDATE ag.survey_response SET japanese = 'フランス領ギアナ' WHERE american = 'French Guiana';
UPDATE ag.survey_response SET japanese = 'フランス領ポリネシア' WHERE american = 'French Polynesia';
UPDATE ag.survey_response SET japanese = 'フランス領南方・南極地域' WHERE american = 'French Southern Territories';
UPDATE ag.survey_response SET japanese = '頻繁なまたは非常にひどい頭痛' WHERE american = 'Frequent or very bad headaches';
UPDATE ag.survey_response SET japanese = '機能性食品（例：チアシード、ふすま）*' WHERE american = '"Functional food (e.g. chia seeds, wheat bran)*"';
UPDATE ag.survey_response SET japanese = 'ガボン' WHERE american = 'Gabon';
UPDATE ag.survey_response SET japanese = 'ガンビア' WHERE american = 'Gambia';
UPDATE ag.survey_response SET japanese = '全般性不安障害' WHERE american = 'Generalized anxiety disorder';
UPDATE ag.survey_response SET japanese = 'ジョージア' WHERE american = 'Georgia';
UPDATE ag.survey_response SET japanese = 'ドイツ' WHERE american = 'Germany';
UPDATE ag.survey_response SET japanese = '妊娠糖尿病' WHERE american = 'Gestational diabetes';
UPDATE ag.survey_response SET japanese = 'ガーナ' WHERE american = 'Ghana';
UPDATE ag.survey_response SET japanese = 'ジブラルタル' WHERE american = 'Gibraltar';
UPDATE ag.survey_response SET japanese = '良い' WHERE american = 'Good';
UPDATE ag.survey_response SET japanese = 'ギリシャ' WHERE american = 'Greece';
UPDATE ag.survey_response SET japanese = 'グリーンランド' WHERE american = 'Greenland';
UPDATE ag.survey_response SET japanese = 'グレナダ' WHERE american = 'Grenada';
UPDATE ag.survey_response SET japanese = 'グアドループ' WHERE american = 'Guadeloupe';
UPDATE ag.survey_response SET japanese = 'グアム' WHERE american = 'Guam';
UPDATE ag.survey_response SET japanese = 'グアテマラ' WHERE american = 'Guatemala';
UPDATE ag.survey_response SET japanese = 'ガーンジー' WHERE american = 'Guernsey';
UPDATE ag.survey_response SET japanese = 'ギニア' WHERE american = 'Guinea';
UPDATE ag.survey_response SET japanese = 'ギニアビサウ' WHERE american = 'Guinea-bissau';
UPDATE ag.survey_response SET japanese = 'ガイアナ' WHERE american = 'Guyana';
UPDATE ag.survey_response SET japanese = 'ハイチ' WHERE american = 'Haiti';
UPDATE ag.survey_response SET japanese = 'ハラール食' WHERE american = 'Halaal';
UPDATE ag.survey_response SET japanese = 'リンゴ酒' WHERE american = 'Hard cider';
UPDATE ag.survey_response SET japanese = 'ハードコンブチャ（アルコール入り紅茶キノコ）' WHERE american = 'Hard kombucha';
UPDATE ag.survey_response SET japanese = 'ハードセルツァー' WHERE american = 'Hard seltzer';
UPDATE ag.survey_response SET japanese = 'ハードティー' WHERE american = 'Hard tea';
UPDATE ag.survey_response SET japanese = '頭頚部がん' WHERE american = 'Head and Neck cancer';
UPDATE ag.survey_response SET japanese = 'ハード島とマクドナルド諸島' WHERE american = 'Heard Island and Mcdonald Islands';
UPDATE ag.survey_response SET japanese = '心疾患／心筋梗塞' WHERE american = 'Heart disease / Myocardial infarction';
UPDATE ag.survey_response SET japanese = '心臓障害' WHERE american = 'Heart problems';
UPDATE ag.survey_response SET japanese = '高校卒業またはGED同等' WHERE american = 'High school diploma or GED equivalent';
UPDATE ag.survey_response SET japanese = 'ヒスパニック系またはラテン系' WHERE american = 'Hispanic or Latino';
UPDATE ag.survey_response SET japanese = 'ヒト免疫不全ウイルス（HIV）' WHERE american = 'HIV';
UPDATE ag.survey_response SET japanese = '教皇庁（バチカン市国）' WHERE american = 'Holy See (Vatican City State)';
UPDATE ag.survey_response SET japanese = 'ホメオパシー薬' WHERE american = 'Homeopathic medicines';
UPDATE ag.survey_response SET japanese = 'ホンジュラス' WHERE american = 'Honduras';
UPDATE ag.survey_response SET japanese = '香港' WHERE american = 'Hong Kong';
UPDATE ag.survey_response SET japanese = 'ホルモン療法' WHERE american = 'Hormone therapy';
UPDATE ag.survey_response SET japanese = 'ホルモン__________' WHERE american = 'Hormones__________';
UPDATE ag.survey_response SET japanese = '入院した' WHERE american = 'Hospitalized';
UPDATE ag.survey_response SET japanese = 'ハンガリー' WHERE american = 'Hungary';
UPDATE ag.survey_response SET japanese = '高血圧症' WHERE american = 'Hypertension';
UPDATE ag.survey_response SET japanese = '温熱療法' WHERE american = 'Hyperthermia';
UPDATE ag.survey_response SET japanese = '私は両手利きです。' WHERE american = 'I am ambidextrous';
UPDATE ag.survey_response SET japanese = '私は左利きです。' WHERE american = 'I am left-handed';
UPDATE ag.survey_response SET japanese = '私は右利きです。' WHERE american = 'I am right-handed';
UPDATE ag.survey_response SET japanese = '私は特殊な食習慣をとっていない。' WHERE american = 'I do not eat a specialized diet';
UPDATE ag.survey_response SET japanese = '発酵食品は食べていない' WHERE american = 'I do not eat fermented foods';
UPDATE ag.survey_response SET japanese = '気分が悪くなるのでグルテンは食べません。' WHERE american = 'I do not eat gluten because it makes me feel bad';
UPDATE ag.survey_response SET japanese = '断続的な断食はしていない。' WHERE american = 'I do not practice intermittent fasting';
UPDATE ag.survey_response SET japanese = '食物繊維サプリメントは服用していません。' WHERE american = 'I do not take fiber supplements';
UPDATE ag.survey_response SET japanese = '自身の活動はいずれも追跡していません。' WHERE american = 'I do not track any of my activities';
UPDATE ag.survey_response SET japanese = 'デオドラントも制汗剤も使用していません。' WHERE american = 'I do not use deodorant or an antiperspirant';
UPDATE ag.survey_response SET japanese = '寝る直前にこれらの機器は使用していません。' WHERE american = 'I do not use these devices before bed';
UPDATE ag.survey_response SET japanese = '味のついていない普通の水は飲んでいない' WHERE american = '"I don’t drink plain, unflavored water"';
UPDATE ag.survey_response SET japanese = '味のついていない普通の水は飲んでいない' WHERE american = '"I don''t drink plain, unflavored water"';
UPDATE ag.survey_response SET japanese = '赤肉以外何でも食べる。' WHERE american = 'I eat anything except red meat';
UPDATE ag.survey_response SET japanese = '例外なく何でも食べる（雑食）' WHERE american = 'I eat anything with no exclusions (omnivore)';
UPDATE ag.survey_response SET japanese = '私は1年以上現在の居住状態で暮らしています。' WHERE american = 'I have lived in my current state of residence for more than a year.';
UPDATE ag.survey_response SET japanese = '私が知っている限り食物アレルギーはありません。' WHERE american = 'I have no food allergies that I know of.';
UPDATE ag.survey_response SET japanese = '私は過去1年の期間に、アメリカ合衆国外に行っていません。' WHERE american = 'I have not been outside of the United States in the past year.';
UPDATE ag.survey_response SET japanese = '私は過去1年間にインフルエンザワクチンを接種していません。' WHERE american = 'I have not gotten the flu vaccine in the past year.';
UPDATE ag.survey_response SET japanese = '摂取量は増えていない。' WHERE american = 'I have not increased my intake.';
UPDATE ag.survey_response SET japanese = '私は過去1年間に抗生物質を服用していません。' WHERE american = 'I have not taken antibiotics in the past year.';
UPDATE ag.survey_response SET japanese = 'サプリメントを服用しているが、どのような種類か知らない。*' WHERE american = '"I take a supplement, but do not know what kind*"';
UPDATE ag.survey_response SET japanese = '便が硬かったり、出にくいことが多い——タイプ1および2' WHERE american = 'I tend to have hard stool or have difficulty passing stool -- Types 1 and 2';
UPDATE ag.survey_response SET japanese = '便がゆるいまたは水っぽいことが多い——タイプ5、6および7' WHERE american = '"I tend to have loose or watery stool – Types 5, 6, and 7"';
UPDATE ag.survey_response SET japanese = '普通の硬さの便のことが多い——タイプ3および4' WHERE american = 'I tend to have normally formed stool – Types 3 and 4';
UPDATE ag.survey_response SET japanese = '私は制汗剤を使用しています。' WHERE american = 'I use an antiperspirant';
UPDATE ag.survey_response SET japanese = '私はデオドラントを使っています。' WHERE american = 'I use deodorant';
UPDATE ag.survey_response SET japanese = 'アイスランド' WHERE american = 'Iceland';
UPDATE ag.survey_response SET japanese = '回腸結腸クローン病' WHERE american = 'Ileal and Colonic Crohn''s disease';
UPDATE ag.survey_response SET japanese = '回腸クローン病' WHERE american = 'Ileal Crohn''s disease';
UPDATE ag.survey_response SET japanese = '免疫障害' WHERE american = 'Immune disorder';
UPDATE ag.survey_response SET japanese = '免疫療法' WHERE american = 'Immunotherapy';
UPDATE ag.survey_response SET japanese = '午後' WHERE american = 'In the afternoon';
UPDATE ag.survey_response SET japanese = '夜' WHERE american = 'In the evening';
UPDATE ag.survey_response SET japanese = '午前中' WHERE american = 'In the morning';
UPDATE ag.survey_response SET japanese = 'インチ' WHERE american = 'inches';
UPDATE ag.survey_response SET japanese = '10ポンド以上増加' WHERE american = 'Increased more than 10 pounds';
UPDATE ag.survey_response SET japanese = 'インド' WHERE american = 'India';
UPDATE ag.survey_response SET japanese = 'インドネシア' WHERE american = 'Indonesia';
UPDATE ag.survey_response SET japanese = '屋内' WHERE american = 'Indoors';
UPDATE ag.survey_response SET japanese = '妨げている' WHERE american = 'Interfering';
UPDATE ag.survey_response SET japanese = 'イヌリン（例：Fiber Choice）*' WHERE american = 'Inulin (e.g. Fiber Choice)*';
UPDATE ag.survey_response SET japanese = 'イラン（イスラム共和国）' WHERE american = '"Iran, Islamic Republic of"';
UPDATE ag.survey_response SET japanese = 'イラク' WHERE american = 'Iraq';
UPDATE ag.survey_response SET japanese = 'アイルランド' WHERE american = 'Ireland';
UPDATE ag.survey_response SET japanese = '刺激性を受けやすい、あるいは日常的な行動を避ける；' WHERE american = 'Irritability or avoidance of routine;';
UPDATE ag.survey_response SET japanese = 'マン島' WHERE american = 'Isle of Man';
UPDATE ag.survey_response SET japanese = '一軒家／農家（人口100人未満）' WHERE american = 'Isolated house/farm (population is less than 100)';
UPDATE ag.survey_response SET japanese = 'イスラエル' WHERE american = 'Israel';
UPDATE ag.survey_response SET japanese = 'イタリア' WHERE american = 'Italy';
UPDATE ag.survey_response SET japanese = 'ジャマイカ' WHERE american = 'Jamaica';
UPDATE ag.survey_response SET japanese = '1月' WHERE american = 'January';
UPDATE ag.survey_response SET japanese = '日本' WHERE american = 'Japan';
UPDATE ag.survey_response SET japanese = 'ジャージー' WHERE american = 'Jersey';
UPDATE ag.survey_response SET japanese = 'ヨルダン' WHERE american = 'Jordan';
UPDATE ag.survey_response SET japanese = '7月' WHERE american = 'July';
UPDATE ag.survey_response SET japanese = '6月' WHERE american = 'June';
UPDATE ag.survey_response SET japanese = 'カザフスタン' WHERE american = 'Kazakhstan';
UPDATE ag.survey_response SET japanese = 'ケフィア（牛乳）' WHERE american = 'Kefir (milk)';
UPDATE ag.survey_response SET japanese = 'ケフィア（水）' WHERE american = 'Kefir (water)';
UPDATE ag.survey_response SET japanese = 'ケニア' WHERE american = 'Kenya';
UPDATE ag.survey_response SET japanese = '腎がん' WHERE american = 'Kidney cancer';
UPDATE ag.survey_response SET japanese = '腎臓障害' WHERE american = 'Kidney problems';
UPDATE ag.survey_response SET japanese = 'キログラム' WHERE american = 'kilograms';
UPDATE ag.survey_response SET japanese = 'キムチ' WHERE american = 'Kimchi';
UPDATE ag.survey_response SET japanese = 'キリバス' WHERE american = 'Kiribati';
UPDATE ag.survey_response SET japanese = '紅茶キノコ（コンブチャ）' WHERE american = 'Kombucha';
UPDATE ag.survey_response SET japanese = '朝鮮民主主義人民共和国' WHERE american = '"Korea, Democratic People''s Republic of"';
UPDATE ag.survey_response SET japanese = '大韓民国' WHERE american = '"Korea, Republic of"';
UPDATE ag.survey_response SET japanese = 'コーシャ食' WHERE american = 'Kosher';
UPDATE ag.survey_response SET japanese = 'クウェート' WHERE american = 'Kuwait';
UPDATE ag.survey_response SET japanese = 'キルギスタン' WHERE american = 'Kyrgyzstan';
UPDATE ag.survey_response SET japanese = '食欲低下' WHERE american = 'Lack of appetite';
UPDATE ag.survey_response SET japanese = '睡眠不足____' WHERE american = 'Lack of sleep____';
UPDATE ag.survey_response SET japanese = 'ラオス人民民主共和国' WHERE american = 'Lao People''s Democratic Republic';
UPDATE ag.survey_response SET japanese = 'ラトビア' WHERE american = 'Latvia';
UPDATE ag.survey_response SET japanese = 'レバノン' WHERE american = 'Lebanon';
UPDATE ag.survey_response SET japanese = 'レソト' WHERE american = 'Lesotho';
UPDATE ag.survey_response SET japanese = '5時間未満' WHERE american = 'less than 5';
UPDATE ag.survey_response SET japanese = '白血病' WHERE american = 'Leukemia';
UPDATE ag.survey_response SET japanese = 'リベリア' WHERE american = 'Liberia';
UPDATE ag.survey_response SET japanese = 'リビア' WHERE american = 'Libya';
UPDATE ag.survey_response SET japanese = 'リヒテンシュタイン' WHERE american = 'Liechtenstein';
UPDATE ag.survey_response SET japanese = 'リトアニア' WHERE american = 'Lithuania';
UPDATE ag.survey_response SET japanese = '肝臓がん' WHERE american = 'Liver cancer';
UPDATE ag.survey_response SET japanese = '味覚や嗅覚の喪失' WHERE american = 'Loss of taste or smell';
UPDATE ag.survey_response SET japanese = '失職した' WHERE american = 'Lost job';
UPDATE ag.survey_response SET japanese = '軽い' WHERE american = 'Low';
UPDATE ag.survey_response SET japanese = '肺がん' WHERE american = 'Lung cancer';
UPDATE ag.survey_response SET japanese = 'ルクセンブルク' WHERE american = 'Luxembourg';
UPDATE ag.survey_response SET japanese = 'リンパ腫' WHERE american = 'Lymphoma';
UPDATE ag.survey_response SET japanese = 'マカオ' WHERE american = 'Macao';
UPDATE ag.survey_response SET japanese = 'マケドニア旧ユーゴスラビア共和国' WHERE american = '"Macedonia, The Former Yugoslav Republic of"';
UPDATE ag.survey_response SET japanese = 'マダガスカル' WHERE american = 'Madagascar';
UPDATE ag.survey_response SET japanese = 'マラウィ' WHERE american = 'Malawi';
UPDATE ag.survey_response SET japanese = 'マレーシア' WHERE american = 'Malaysia';
UPDATE ag.survey_response SET japanese = 'モルディブ' WHERE american = 'Maldives';
UPDATE ag.survey_response SET japanese = '男性' WHERE american = 'Male';
UPDATE ag.survey_response SET japanese = 'マリ' WHERE american = 'Mali';
UPDATE ag.survey_response SET japanese = '麦芽酒' WHERE american = 'Malt liquor';
UPDATE ag.survey_response SET japanese = 'マルタ' WHERE american = 'Malta';
UPDATE ag.survey_response SET japanese = '3月' WHERE american = 'March';
UPDATE ag.survey_response SET japanese = 'マーシャル諸島' WHERE american = 'Marshall Islands';
UPDATE ag.survey_response SET japanese = 'マルティニーク' WHERE american = 'Martinique';
UPDATE ag.survey_response SET japanese = '修士号（MS、MAなど）' WHERE american = '"Master’s degree (e.g. MS, MA)"';
UPDATE ag.survey_response SET japanese = 'モーリタニア' WHERE american = 'Mauritania';
UPDATE ag.survey_response SET japanese = 'モーリシャス' WHERE american = 'Mauritius';
UPDATE ag.survey_response SET japanese = '5月' WHERE american = 'May';
UPDATE ag.survey_response SET japanese = 'マヨット' WHERE american = 'Mayotte';
UPDATE ag.survey_response SET japanese = 'ミード' WHERE american = 'Mead';
UPDATE ag.survey_response SET japanese = 'バルビツレートまたはオピオイドを含む医薬品__________' WHERE american = 'Medications that contain barbiturates or opioids__________';
UPDATE ag.survey_response SET japanese = '黒色腫（皮膚）' WHERE american = 'Melanoma (skin)';
UPDATE ag.survey_response SET japanese = 'メチルセルロース（例：Citrucel）*' WHERE american = 'Methylcellulose (e.g. Citrucel)*';
UPDATE ag.survey_response SET japanese = '主要都市（人口100万人以上）' WHERE american = 'Metropolis (population is more than 1 million)';
UPDATE ag.survey_response SET japanese = 'メキシコ' WHERE american = 'Mexico';
UPDATE ag.survey_response SET japanese = '微小大腸炎' WHERE american = 'Microcolitis';
UPDATE ag.survey_response SET japanese = 'ミクロネシア連邦' WHERE american = '"Micronesia, Federated States of"';
UPDATE ag.survey_response SET japanese = '軽い' WHERE american = 'Mild';
UPDATE ag.survey_response SET japanese = '中等度' WHERE american = 'Moderate';
UPDATE ag.survey_response SET japanese = 'ある程度満足している' WHERE american = 'Moderately satisfied';
UPDATE ag.survey_response SET japanese = '変更パレオダイエット' WHERE american = 'Modified paleo diet';
UPDATE ag.survey_response SET japanese = 'モルドバ共和国' WHERE american = '"Moldova, Republic of"';
UPDATE ag.survey_response SET japanese = 'モナコ' WHERE american = 'Monaco';
UPDATE ag.survey_response SET japanese = 'モンゴル' WHERE american = 'Mongolia';
UPDATE ag.survey_response SET japanese = 'モンクフルーツ' WHERE american = 'Monk fruit';
UPDATE ag.survey_response SET japanese = 'モンテネグロ' WHERE american = 'Montenegro';
UPDATE ag.survey_response SET japanese = '1ヶ月' WHERE american = 'Month';
UPDATE ag.survey_response SET japanese = '毎月' WHERE american = 'Monthly';
UPDATE ag.survey_response SET japanese = 'モンセラート' WHERE american = 'Montserrat';
UPDATE ag.survey_response SET japanese = '1日3回以上' WHERE american = 'More than 2 times a day';
UPDATE ag.survey_response SET japanese = '31種類以上' WHERE american = 'more than 30';
UPDATE ag.survey_response SET japanese = '５杯以上' WHERE american = 'more than 4';
UPDATE ag.survey_response SET japanese = '8時間を超える' WHERE american = 'more than 8';
UPDATE ag.survey_response SET japanese = '半日に1回' WHERE american = 'More than half the days';
UPDATE ag.survey_response SET japanese = '4人以上' WHERE american = 'More than three';
UPDATE ag.survey_response SET japanese = 'モロッコ' WHERE american = 'Morocco';
UPDATE ag.survey_response SET japanese = 'モザンビーク' WHERE american = 'Mozambique';
UPDATE ag.survey_response SET japanese = '多民族' WHERE american = 'Multiracial';
UPDATE ag.survey_response SET japanese = 'ミャンマー' WHERE american = 'Myanmar';
UPDATE ag.survey_response SET japanese = 'ナミビア' WHERE american = 'Namibia';
UPDATE ag.survey_response SET japanese = 'アメリカ先住民またはアラスカ先住民' WHERE american = 'Native American or Alaska Native';
UPDATE ag.survey_response SET japanese = 'ハワイまたは他の太平洋諸島の先住民' WHERE american = 'Native Hawaiian or Other Pacific Islander';
UPDATE ag.survey_response SET japanese = '欧州連合の他の国または英国で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* in another country in the European Union or the UK';
UPDATE ag.survey_response SET japanese = '欧州連合または英国以外の国で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* in another country not in the European Union or the UK';
UPDATE ag.survey_response SET japanese = '現地（例：居住国）で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* locally (i.e. in your country of residence)';
UPDATE ag.survey_response SET japanese = 'ナウル' WHERE american = 'Nauru';
UPDATE ag.survey_response SET japanese = '吐き気' WHERE american = 'Nausea';
UPDATE ag.survey_response SET japanese = '吐き気および/または嘔吐；' WHERE american = 'Nausea and/or vomiting;';
UPDATE ag.survey_response SET japanese = 'ほぼ毎日' WHERE american = 'Nearly every day';
UPDATE ag.survey_response SET japanese = 'ネパール' WHERE american = 'Nepal';
UPDATE ag.survey_response SET japanese = 'オランダ' WHERE american = 'Netherlands';
UPDATE ag.survey_response SET japanese = 'オランダ領アンティル' WHERE american = 'Netherlands Antilles';
UPDATE ag.survey_response SET japanese = '全くない' WHERE american = 'Never';
UPDATE ag.survey_response SET japanese = 'ニューカレドニア' WHERE american = 'New Caledonia';
UPDATE ag.survey_response SET japanese = 'ニュージーランド' WHERE american = 'New Zealand';
UPDATE ag.survey_response SET japanese = 'ニカラグア' WHERE american = 'Nicaragua';
UPDATE ag.survey_response SET japanese = 'ニジェール' WHERE american = 'Niger';
UPDATE ag.survey_response SET japanese = 'ナイジェリア' WHERE american = 'Nigeria';
UPDATE ag.survey_response SET japanese = '硝酸塩__________' WHERE american = 'Nitrates__________';
UPDATE ag.survey_response SET japanese = 'ニウエ' WHERE american = 'Niue';
UPDATE ag.survey_response SET japanese = 'いいえ' WHERE american = 'No';
UPDATE ag.survey_response SET japanese = '正規の教育は受けていない' WHERE american = 'No formal education';
UPDATE ag.survey_response SET japanese = '症状や兆候はなかった' WHERE american = 'No symptoms or signs';
UPDATE ag.survey_response SET japanese = 'いいえ、この病状はありません。' WHERE american = '"No, I do not have this condition"';
UPDATE ag.survey_response SET japanese = 'いいえ、アレルギー用の薬は一切服用していません。' WHERE american = '"No, I do not take any medications for my allergies."';
UPDATE ag.survey_response SET japanese = 'いいえ、がんはなくなりました。' WHERE american = '"No, I no longer have cancer"';
UPDATE ag.survey_response SET japanese = '1人もいない' WHERE american = 'None';
UPDATE ag.survey_response SET japanese = 'いずれも該当しない' WHERE american = 'None of the above';
UPDATE ag.survey_response SET japanese = 'ノーフォーク島' WHERE american = 'Norfolk Island';
UPDATE ag.survey_response SET japanese = '北マリアナ諸島' WHERE american = 'Northern Mariana Islands';
UPDATE ag.survey_response SET japanese = 'ノルウェー' WHERE american = 'Norway';
UPDATE ag.survey_response SET japanese = '全くない' WHERE american = 'Not at all';
UPDATE ag.survey_response SET japanese = 'どちらとも言えない' WHERE american = 'Not sure';
UPDATE ag.survey_response SET japanese = 'どちらかわかりませんが、何らかのデオドラントか制汗剤を使用しています。' WHERE american = '"Not sure, but I use some form of deodorant or antiperspirant"';
UPDATE ag.survey_response SET japanese = '11月' WHERE american = 'November';
UPDATE ag.survey_response SET japanese = 'エンバクの食物繊維*' WHERE american = 'Oat fiber*';
UPDATE ag.survey_response SET japanese = '10月' WHERE american = 'October';
UPDATE ag.survey_response SET japanese = 'オマーン' WHERE american = 'Oman';
UPDATE ag.survey_response SET japanese = '1日1回' WHERE american = 'Once a day';
UPDATE ag.survey_response SET japanese = '週に1回' WHERE american = 'Once per week';
UPDATE ag.survey_response SET japanese = '1人' WHERE american = 'One';
UPDATE ag.survey_response SET japanese = '1回か2回' WHERE american = 'One or two days';
UPDATE ag.survey_response SET japanese = 'ラマダン期間中のみ' WHERE american = 'Only during Ramadan';
UPDATE ag.survey_response SET japanese = 'その他' WHERE american = 'Other';
UPDATE ag.survey_response SET japanese = 'その他_____________' WHERE american = 'Other _____________';
UPDATE ag.survey_response SET japanese = 'ここに記載されていないその他の制限' WHERE american = 'Other restrictions not described here';
UPDATE ag.survey_response SET japanese = 'その他*' WHERE american = 'Other*';
UPDATE ag.survey_response SET japanese = '屋外' WHERE american = 'Outdoors';
UPDATE ag.survey_response SET japanese = '卵巣がん' WHERE american = 'Ovarian cancer';
UPDATE ag.survey_response SET japanese = 'パキスタン' WHERE american = 'Pakistan';
UPDATE ag.survey_response SET japanese = 'パラオ' WHERE american = 'Palau';
UPDATE ag.survey_response SET japanese = 'パレオダイエットまたは原始人食' WHERE american = 'Paleo-diet or primal diet';
UPDATE ag.survey_response SET japanese = 'パレスチナ占領地域' WHERE american = '"Palestinian Territory, Occupied"';
UPDATE ag.survey_response SET japanese = 'パナマ' WHERE american = 'Panama';
UPDATE ag.survey_response SET japanese = '膵臓がん' WHERE american = 'Pancreatic cancer';
UPDATE ag.survey_response SET japanese = 'パプアニューギニア' WHERE american = 'Papua New Guinea';
UPDATE ag.survey_response SET japanese = 'パラグアイ' WHERE american = 'Paraguay';
UPDATE ag.survey_response SET japanese = '死亡' WHERE american = 'Passed away';
UPDATE ag.survey_response SET japanese = 'ピーナッツ' WHERE american = 'Peanuts';
UPDATE ag.survey_response SET japanese = '定期的な断食' WHERE american = 'Periodic fasting';
UPDATE ag.survey_response SET japanese = 'ペルー' WHERE american = 'Peru';
UPDATE ag.survey_response SET japanese = 'ペットの毛など' WHERE american = 'Pet dander';
UPDATE ag.survey_response SET japanese = '褐色細胞腫および傍神経節腫がん' WHERE american = 'Pheochromocytoma and paraganglioma cancer';
UPDATE ag.survey_response SET japanese = 'フィリピン' WHERE american = 'Philippines';
UPDATE ag.survey_response SET japanese = '音恐怖症（音に対する敏感性）；' WHERE american = 'Phonophobia (sensitivity to sound);';
UPDATE ag.survey_response SET japanese = '光力学治療' WHERE american = 'Photodynamic therapy';
UPDATE ag.survey_response SET japanese = '光恐怖症（光に対する敏感性）；' WHERE american = 'Photophobia (sensitivity to light);';
UPDATE ag.survey_response SET japanese = '漬け物' WHERE american = 'Pickled vegetables';
UPDATE ag.survey_response SET japanese = 'ピトケアン' WHERE american = 'Pitcairn';
UPDATE ag.survey_response SET japanese = 'ツタウルシ／ウルシ／ウルシ毒' WHERE american = 'Poison ivy/oak/sumac';
UPDATE ag.survey_response SET japanese = 'ポーランド' WHERE american = 'Poland';
UPDATE ag.survey_response SET japanese = '悪い' WHERE american = 'Poor';
UPDATE ag.survey_response SET japanese = 'ポルトガル' WHERE american = 'Portugal';
UPDATE ag.survey_response SET japanese = 'ポンド' WHERE american = 'pounds';
UPDATE ag.survey_response SET japanese = '糖尿病前症' WHERE american = 'Prediabetes';
UPDATE ag.survey_response SET japanese = '主に母乳' WHERE american = 'Primarily breast milk';
UPDATE ag.survey_response SET japanese = '主に調整粉乳' WHERE american = 'Primarily infant formula';
UPDATE ag.survey_response SET japanese = '専門職学位（MD、DDS、DVMなど）' WHERE american = '"Professional degree (e.g. MD,DDS, DVM)"';
UPDATE ag.survey_response SET japanese = '前立腺がん' WHERE american = 'Prostate cancer';
UPDATE ag.survey_response SET japanese = 'サイリウム（例：Metamucil）*' WHERE american = 'Psyllium (e.g. Metamucil)*';
UPDATE ag.survey_response SET japanese = '心的外傷後ストレス障害（post-traumatic stress disorder、PTSD）' WHERE american = 'PTSD (post-traumatic stress disorder)';
UPDATE ag.survey_response SET japanese = 'プエルトリコ' WHERE american = 'Puerto Rico';
UPDATE ag.survey_response SET japanese = '肺塞栓症' WHERE american = 'Pulmonary embolism';
UPDATE ag.survey_response SET japanese = '症状ありで自己隔離に入った' WHERE american = 'Put into self-quarantine with symptoms';
UPDATE ag.survey_response SET japanese = '症状なしで自己隔離に入った（接触した可能性があるためなど）' WHERE american = 'Put into self-quarantine without symptoms (e.g. due to possible exposure)';
UPDATE ag.survey_response SET japanese = 'カタール' WHERE american = 'Qatar';
UPDATE ag.survey_response SET japanese = 'かなり妨げている' WHERE american = 'Quite interfering';
UPDATE ag.survey_response SET japanese = 'かなりわかる' WHERE american = 'Quite Noticeable';
UPDATE ag.survey_response SET japanese = 'かなり心配' WHERE american = 'Quite worried';
UPDATE ag.survey_response SET japanese = '放射線療法' WHERE american = 'Radiotherapy';
UPDATE ag.survey_response SET japanese = '生食（加熱調理していないダイエット）' WHERE american = 'Raw food diet';
UPDATE ag.survey_response SET japanese = '直腸がん' WHERE american = 'Rectal cancer';
UPDATE ag.survey_response SET japanese = '赤ワイン' WHERE american = 'Red wine';
UPDATE ag.survey_response SET japanese = '収入が減った' WHERE american = 'Reduced ability to earn money';
UPDATE ag.survey_response SET japanese = '安定した状態を維持' WHERE american = 'Remained stable';
UPDATE ag.survey_response SET japanese = 'レユニオン' WHERE american = 'Reunion';
UPDATE ag.survey_response SET japanese = 'ルーマニア' WHERE american = 'Romania';
UPDATE ag.survey_response SET japanese = 'ロゼ・ワイン' WHERE american = 'Rose wine';
UPDATE ag.survey_response SET japanese = 'ロシア連邦' WHERE american = 'Russian Federation';
UPDATE ag.survey_response SET japanese = 'ルワンダ' WHERE american = 'Rwanda';
UPDATE ag.survey_response SET japanese = 'サッカリン' WHERE american = 'Saccharin';
UPDATE ag.survey_response SET japanese = 'セントヘレナ' WHERE american = 'Saint Helena';
UPDATE ag.survey_response SET japanese = 'セントキッツ・ネイビス' WHERE american = 'Saint Kitts and Nevis';
UPDATE ag.survey_response SET japanese = 'セントルシア' WHERE american = 'Saint Lucia';
UPDATE ag.survey_response SET japanese = 'サンピエール島・ミクロン島' WHERE american = 'Saint Pierre and Miquelon';
UPDATE ag.survey_response SET japanese = 'セントビンセント・グレナディーン' WHERE american = 'Saint Vincent and The Grenadines';
UPDATE ag.survey_response SET japanese = '日本酒' WHERE american = 'Sake';
UPDATE ag.survey_response SET japanese = 'サモア' WHERE american = 'Samoa';
UPDATE ag.survey_response SET japanese = 'サンマリノ' WHERE american = 'San Marino';
UPDATE ag.survey_response SET japanese = 'サントメ・プリンシペ' WHERE american = 'Sao Tome and Principe';
UPDATE ag.survey_response SET japanese = '肉腫' WHERE american = 'Sarcoma';
UPDATE ag.survey_response SET japanese = '満足している' WHERE american = 'Satisfied';
UPDATE ag.survey_response SET japanese = 'サウジアラビア' WHERE american = 'Saudi Arabia';
UPDATE ag.survey_response SET japanese = 'ザウアークラウト' WHERE american = 'Sauerkraut';
UPDATE ag.survey_response SET japanese = '統合失調症' WHERE american = 'Schizophrenia';
UPDATE ag.survey_response SET japanese = '季節性アレルギー' WHERE american = 'Seasonal allergies';
UPDATE ag.survey_response SET japanese = '自己診断しました。' WHERE american = 'Self-diagnosed';
UPDATE ag.survey_response SET japanese = 'セネガル' WHERE american = 'Senegal';
UPDATE ag.survey_response SET japanese = '9月' WHERE american = 'September';
UPDATE ag.survey_response SET japanese = 'セルビア' WHERE american = 'Serbia';
UPDATE ag.survey_response SET japanese = '重篤なニキビまたは皮膚障害' WHERE american = 'Serious acne or skin problems';
UPDATE ag.survey_response SET japanese = '重篤な胃腸障害' WHERE american = 'Serious stomach or bowel problems';
UPDATE ag.survey_response SET japanese = '週に数日' WHERE american = 'Several days per week';
UPDATE ag.survey_response SET japanese = '重い' WHERE american = 'Severe';
UPDATE ag.survey_response SET japanese = 'セーシェル' WHERE american = 'Seychelles';
UPDATE ag.survey_response SET japanese = '貝類' WHERE american = 'Shellfish';
UPDATE ag.survey_response SET japanese = '息切れ' WHERE american = 'Shortness of breath';
UPDATE ag.survey_response SET japanese = 'シエラレオネ' WHERE american = 'Sierra Leone';
UPDATE ag.survey_response SET japanese = '幼児期／小児期以降' WHERE american = 'Since infancy/childhood';
UPDATE ag.survey_response SET japanese = 'シンガポール' WHERE american = 'Singapore';
UPDATE ag.survey_response SET japanese = '睡眠' WHERE american = 'Sleep';
UPDATE ag.survey_response SET japanese = 'スロバキア' WHERE american = 'Slovakia';
UPDATE ag.survey_response SET japanese = 'スロベニア' WHERE american = 'Slovenia';
UPDATE ag.survey_response SET japanese = '"小さな町または村（人口100人超、1,000人未満）"' WHERE american = '"Small town or village (population is more than 100 and less than 1,000)"';
UPDATE ag.survey_response SET japanese = '軟便' WHERE american = 'Soft stools';
UPDATE ag.survey_response SET japanese = 'ソロモン諸島' WHERE american = 'Solomon Islands';
UPDATE ag.survey_response SET japanese = 'ソマリア' WHERE american = 'Somalia';
UPDATE ag.survey_response SET japanese = 'やや妨げている' WHERE american = 'Somewhat interfering';
UPDATE ag.survey_response SET japanese = 'ややわかる' WHERE american = 'Somewhat noticeable';
UPDATE ag.survey_response SET japanese = 'やや心配' WHERE american = 'Somewhat worried';
UPDATE ag.survey_response SET japanese = '喉の痛み' WHERE american = 'Sore throat';
UPDATE ag.survey_response SET japanese = 'サワービール' WHERE american = 'Sour beer';
UPDATE ag.survey_response SET japanese = 'サワークリーム／クレームフレーシュ' WHERE american = 'Sour cream/crème fraiche';
UPDATE ag.survey_response SET japanese = '南アフリカ' WHERE american = 'South Africa';
UPDATE ag.survey_response SET japanese = 'サウスジョージア・サウスサンドウィッチ諸島' WHERE american = 'South Georgia and The South Sandwich Islands';
UPDATE ag.survey_response SET japanese = 'スペイン' WHERE american = 'Spain';
UPDATE ag.survey_response SET japanese = '発泡ワイン' WHERE american = 'Sparkling wine';
UPDATE ag.survey_response SET japanese = 'ハードリカー／蒸留酒／強い酒' WHERE american = 'Spirits/liquors/hard alcohol';
UPDATE ag.survey_response SET japanese = 'スリランカ' WHERE american = 'Sri Lanka';
UPDATE ag.survey_response SET japanese = '幹細胞移植' WHERE american = 'Stem cell transplant';
UPDATE ag.survey_response SET japanese = 'ステビア' WHERE american = 'Stevia';
UPDATE ag.survey_response SET japanese = '胃がん' WHERE american = 'Stomach cancer';
UPDATE ag.survey_response SET japanese = '腹痛' WHERE american = 'Stomachache';
UPDATE ag.survey_response SET japanese = '筋力トレーニング' WHERE american = 'Strength training';
UPDATE ag.survey_response SET japanese = 'ストレス__________' WHERE american = 'Stress__________';
UPDATE ag.survey_response SET japanese = '脳卒中' WHERE american = 'Stroke';
UPDATE ag.survey_response SET japanese = '薬物乱用' WHERE american = 'Substance abuse';
UPDATE ag.survey_response SET japanese = 'スクラロース' WHERE american = 'Sucralose';
UPDATE ag.survey_response SET japanese = 'スーダン' WHERE american = 'Sudan';
UPDATE ag.survey_response SET japanese = '糖アルコール（ソルビトール、キシリトール、ラクチトール、マンニトール、エリスリトール、マルチトール）' WHERE american = '"Sugar alcohols (sorbitol, xylitol, lactitol, mannitol, erythritol, and maltitol)"';
UPDATE ag.survey_response SET japanese = '日光' WHERE american = 'Sun';
UPDATE ag.survey_response SET japanese = '手術' WHERE american = 'Surgery';
UPDATE ag.survey_response SET japanese = 'スリナム' WHERE american = 'Suriname';
UPDATE ag.survey_response SET japanese = 'スヴァールバル諸島およびヤンマイエン島' WHERE american = 'Svalbard and Jan Mayen';
UPDATE ag.survey_response SET japanese = 'スワジランド' WHERE american = 'Swaziland';
UPDATE ag.survey_response SET japanese = 'スウェーデン' WHERE american = 'Sweden';
UPDATE ag.survey_response SET japanese = 'スイス' WHERE american = 'Switzerland';
UPDATE ag.survey_response SET japanese = 'シリア・アラブ共和国' WHERE american = 'Syrian Arab Republic';
UPDATE ag.survey_response SET japanese = '台湾' WHERE american = 'Taiwan';
UPDATE ag.survey_response SET japanese = 'タジキスタン' WHERE american = 'Tajikistan';
UPDATE ag.survey_response SET japanese = 'タンザニア連合共和国' WHERE american = '"Tanzania, United Republic of"';
UPDATE ag.survey_response SET japanese = '水道水' WHERE american = 'Tap water';
UPDATE ag.survey_response SET japanese = '標的（薬物）療法' WHERE american = 'Targeted (medication) therapy';
UPDATE ag.survey_response SET japanese = 'テンペ' WHERE american = 'Tempeh';
UPDATE ag.survey_response SET japanese = '精巣胚細胞性がん' WHERE american = 'Testicular germ cell cancer';
UPDATE ag.survey_response SET japanese = 'タイ' WHERE american = 'Thailand';
UPDATE ag.survey_response SET japanese = '3人' WHERE american = 'Three';
UPDATE ag.survey_response SET japanese = '甲状腺がん' WHERE american = 'Thyroid cancer';
UPDATE ag.survey_response SET japanese = '東チモール' WHERE american = 'Timor-leste';
UPDATE ag.survey_response SET japanese = 'トーゴ' WHERE american = 'Togo';
UPDATE ag.survey_response SET japanese = 'トケラウ' WHERE american = 'Tokelau';
UPDATE ag.survey_response SET japanese = 'トンガ' WHERE american = 'Tonga';
UPDATE ag.survey_response SET japanese = '"町（人口1,000人超、10万人未満）"' WHERE american = '"Town (population is more than 1,000 and less than 100,000)"';
UPDATE ag.survey_response SET japanese = '木の実' WHERE american = 'Tree nuts';
UPDATE ag.survey_response SET japanese = 'トリニダード・トバゴ' WHERE american = 'Trinidad and Tobago';
UPDATE ag.survey_response SET japanese = 'チュニジア' WHERE american = 'Tunisia';
UPDATE ag.survey_response SET japanese = 'トルコ' WHERE american = 'Turkey';
UPDATE ag.survey_response SET japanese = 'トルクメニスタン' WHERE american = 'Turkmenistan';
UPDATE ag.survey_response SET japanese = 'タークス・カイコス諸島' WHERE american = 'Turks and Caicos Islands';
UPDATE ag.survey_response SET japanese = 'ツバル' WHERE american = 'Tuvalu';
UPDATE ag.survey_response SET japanese = '2人' WHERE american = 'Two';
UPDATE ag.survey_response SET japanese = '1型糖尿病' WHERE american = 'Type I diabetes';
UPDATE ag.survey_response SET japanese = '2型糖尿病' WHERE american = 'Type II diabetes';
UPDATE ag.survey_response SET japanese = 'ウガンダ' WHERE american = 'Uganda';
UPDATE ag.survey_response SET japanese = 'ウクライナ' WHERE american = 'Ukraine';
UPDATE ag.survey_response SET japanese = '潰瘍性大腸炎' WHERE american = 'Ulcerative Colitis';
UPDATE ag.survey_response SET japanese = 'アラブ首長国連邦' WHERE american = 'United Arab Emirates';
UPDATE ag.survey_response SET japanese = 'イギリス' WHERE american = 'United Kingdom';
UPDATE ag.survey_response SET japanese = 'アメリカ合衆国' WHERE american = 'United States';
UPDATE ag.survey_response SET japanese = '合衆国領有小離島' WHERE american = 'United States Minor Outlying Islands';
UPDATE ag.survey_response SET japanese = 'ウルグアイ' WHERE american = 'Uruguay';
UPDATE ag.survey_response SET japanese = '子宮がん' WHERE american = 'Uterine cancer';
UPDATE ag.survey_response SET japanese = 'ぶどう膜メラノーマ' WHERE american = 'Uveal melanoma';
UPDATE ag.survey_response SET japanese = 'ウズベキスタン' WHERE american = 'Uzbekistan';
UPDATE ag.survey_response SET japanese = 'バヌアツ' WHERE american = 'Vanuatu';
UPDATE ag.survey_response SET japanese = 'ビーガン' WHERE american = 'Vegan';
UPDATE ag.survey_response SET japanese = 'ベジタリアン' WHERE american = 'Vegetarian';
UPDATE ag.survey_response SET japanese = 'ベジタリアンだが、海産食品は食べる。' WHERE american = 'Vegetarian but eat seafood';
UPDATE ag.survey_response SET japanese = 'ベネズエラ' WHERE american = 'Venezuela';
UPDATE ag.survey_response SET japanese = '非常に不満である' WHERE american = 'Very dissatisfied';
UPDATE ag.survey_response SET japanese = '大変良い' WHERE american = 'Very good';
UPDATE ag.survey_response SET japanese = '非常に妨げている' WHERE american = 'Very interfering';
UPDATE ag.survey_response SET japanese = '非常によくわかる' WHERE american = 'Very noticeable';
UPDATE ag.survey_response SET japanese = '非常に悪い' WHERE american = 'Very poor';
UPDATE ag.survey_response SET japanese = '大変満足している' WHERE american = 'Very satisfied';
UPDATE ag.survey_response SET japanese = '非常に重い' WHERE american = 'Very severe';
UPDATE ag.survey_response SET japanese = '非常に心配' WHERE american = 'Very worried';
UPDATE ag.survey_response SET japanese = 'ベトナム' WHERE american = 'Vietnam';
UPDATE ag.survey_response SET japanese = '激しい' WHERE american = 'Vigorous';
UPDATE ag.survey_response SET japanese = '英領バージン諸島' WHERE american = '"Virgin Islands, British"';
UPDATE ag.survey_response SET japanese = 'アメリカ領ヴァージン諸島' WHERE american = '"Virgin Islands, U.S."';
UPDATE ag.survey_response SET japanese = '職業訓練' WHERE american = 'Vocational training';
UPDATE ag.survey_response SET japanese = 'ウォリス・フツナ' WHERE american = 'Wallis and Futuna';
UPDATE ag.survey_response SET japanese = '1週間' WHERE american = 'Week';
UPDATE ag.survey_response SET japanese = '毎週' WHERE american = 'Weekly';
UPDATE ag.survey_response SET japanese = '井戸水' WHERE american = 'Well water';
UPDATE ag.survey_response SET japanese = '西サハラ' WHERE american = 'Western Sahara';
UPDATE ag.survey_response SET japanese = 'ウェストン・プライス、またはその他の低穀物、低加工食品の食事' WHERE american = '"Weston-Price, or other low-grain, low processed food diet"';
UPDATE ag.survey_response SET japanese = '小麦デキストリン（例： Benefiber ）*' WHERE american = 'Wheat dextrin (e.g. Benefiber)*';
UPDATE ag.survey_response SET japanese = '白人' WHERE american = 'White';
UPDATE ag.survey_response SET japanese = '白ワイン' WHERE american = 'White wine';
UPDATE ag.survey_response SET japanese = 'ワイン' WHERE american = 'Wine';
UPDATE ag.survey_response SET japanese = '過去10年以内' WHERE american = 'Within the last 10 years';
UPDATE ag.survey_response SET japanese = '過去5年以内' WHERE american = 'Within the last 5 years';
UPDATE ag.survey_response SET japanese = '過去1年以内' WHERE american = 'Within the last year';
UPDATE ag.survey_response SET japanese = '過去3ヶ月以内' WHERE american = 'Within the past 3 months';
UPDATE ag.survey_response SET japanese = '過去6ヶ月以内' WHERE american = 'Within the past 6 months';
UPDATE ag.survey_response SET japanese = '過去1ヶ月以内' WHERE american = 'Within the past month';
UPDATE ag.survey_response SET japanese = '過去1年以内' WHERE american = 'Within the past year';
UPDATE ag.survey_response SET japanese = '1年' WHERE american = 'Year';
UPDATE ag.survey_response SET japanese = 'イエメン' WHERE american = 'Yemen';
UPDATE ag.survey_response SET japanese = 'はい' WHERE american = 'Yes';
UPDATE ag.survey_response SET japanese = 'はい、医療専門家（医師、医師助手）によって診断されました。' WHERE american = '"Yes, diagnosed by a medical professional (doctor, physician assistant)"';
UPDATE ag.survey_response SET japanese = 'はい、代替医療の医師によって診断されました。' WHERE american = '"Yes, diagnosed by an alternative medicine practitioner"';
UPDATE ag.survey_response SET japanese = 'はい、セリアック病と診断されました。' WHERE american = '"Yes, diagnosed with celiac disease"';
UPDATE ag.survey_response SET japanese = 'はい、グルテンアレルギー（抗グルテンIgG ）の診断を受けましたが、セリアック病ではありません。' WHERE american = '"Yes, diagnosed with gluten allergy (anti-gluten IgG), but not celiac disease"';
UPDATE ag.survey_response SET japanese = 'はい、コロナらしい症状がいくつかあったが、陰性の検査結果だった' WHERE american = '"Yes, have had some possible symptoms but tested negative"';
UPDATE ag.survey_response SET japanese = 'はい、コロナらしい症状がいくつかあったが、医師による診断は受けていない' WHERE american = '"Yes, have had some possible symptoms, but no diagnosis by doctor"';
UPDATE ag.survey_response SET japanese = 'はい、「ピル」を服用しています。' WHERE american = '"Yes, I am taking the ""pill"""';
UPDATE ag.survey_response SET japanese = 'はい、現在がんを患っています。' WHERE american = '"Yes, I currently have cancer"';
UPDATE ag.survey_response SET japanese = 'はい、ホメオパシー薬を服用しています。' WHERE american = '"Yes, I take homeopathic medication."';
UPDATE ag.survey_response SET japanese = 'はい、市販薬を服用しています。' WHERE american = '"Yes, I take over-the-counter medication."';
UPDATE ag.survey_response SET japanese = 'はい、処方薬を服用しています。' WHERE american = '"Yes, I take prescription medication."';
UPDATE ag.survey_response SET japanese = 'はい、避妊用パッチを使用しています。' WHERE american = '"Yes, I use a contraceptive patch"';
UPDATE ag.survey_response SET japanese = 'はい、避妊用の膣リングを使用しています。' WHERE american = '"Yes, I use a contraceptive vaginal ring"';
UPDATE ag.survey_response SET japanese = 'はい、銅製の子宮内避妊具を使用しています。' WHERE american = '"Yes, I use a copper IUD"';
UPDATE ag.survey_response SET japanese = 'はい、ホルモン子宮内避妊具／インプラントを使用しています。' WHERE american = '"Yes, I use a hormonal IUD/implant"';
UPDATE ag.survey_response SET japanese = 'はい、注射用避妊薬を使用しています。' WHERE american = '"Yes, I use an injected contraceptive"';
UPDATE ag.survey_response SET japanese = 'はい、ここに記載されていない他の種類の薬を使用しています。' WHERE american = '"Yes, I use other types of medication not listed here."';
UPDATE ag.survey_response SET japanese = 'はい、医療診断を受けたが、検査は受けていない' WHERE american = '"Yes, medical diagnosis, but no test"';
UPDATE ag.survey_response SET japanese = 'はい、医療診断を受けているが検査を受けていない人と接触' WHERE american = '"Yes, someone with medical diagnosis, but no test"';
UPDATE ag.survey_response SET japanese = 'はい、検査結果が陽性の人と接触' WHERE american = '"Yes, someone with positive test"';
UPDATE ag.survey_response SET japanese = 'はい、コロナらしい症状はあるが医師による診断を受けていない人と接触' WHERE american = '"Yes, someone with possible symptoms, but no diagnosis by doctor"';
UPDATE ag.survey_response SET japanese = 'はい、陽性の検査結果だった' WHERE american = '"Yes, with a positive test"';
UPDATE ag.survey_response SET japanese = 'ヨーグルト／ラッシー' WHERE american = 'Yogurt/lassi';
UPDATE ag.survey_response SET japanese = 'ザンビア' WHERE american = 'Zambia';
UPDATE ag.survey_response SET japanese = 'ジンバブエ' WHERE american = 'Zimbabwe';

-- Create Japanese consent documents
INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id)
    VALUES ('adult_data', 'ja_JP', NOW(), '<p class="consent_title">
  <strong>University of California San Diego (カリフォルニア大学サンディエゴ校)<br />
  研究被験者として行動する同意書</strong>
</p>
<p class="consent_title">
  <strong>Microsetta Initiative（マイクロセッタ・イニシアチブ）</strong>
</p>
<p class="consent_header">
  調査研究実施者、参加者が参加を求められている理由、あなたが選択された方法、この研究の参加人数について
</p>
<p class="consent_content">
  本同意書は Microsetta Initiative研究調査へ参加する被験者に対する書面です。
</p>
<p class="consent_content">
  この研究はカリフォルニア大学サンディエゴ校（UC San Diego）のDr. Rob Knightによって実施されています。あなたが地球上の他の誰とも同じではないように、あなたの体が持つ微生物も、地球上の他の誰とも違う固有なものです。個人ごとに違う細菌叢を調べるため、ぜひこの研究へご参加ください。この研究には、米国全体と世界の各国から約500,000人が参加します。
</p>
<p class="consent_header">
  この研究が実施される理由
</p>
<p class="consent_content">
  この研究の目的は、人々の腸内の細菌叢の違いをより正確に評価して、これらの違いが、ライフスタイル、食事、体型、年齢、または病気の存在に関連しているかを調べることです。この研究への参加に同意した方には、オンラインでの調査／質問票への記入が求められます。これらの調査／質問票は内容によって区分され、あなたの年齢、体重、身長、ライフスタイル、食事、病気か健康かなど、あなたに関する質問を行います。各調査の所要時間は平均5~10分ですが、一部には終わるまでに最長30分を要するものもあります。
</p>
<p class="consent_header">
  得られると予想される利益
</p>
<p class="consent_content">
  この研究に金銭的または直接的な利益はありません。「食物頻度の質問票（FFQ）」に回答されると、食事のパターンと栄養摂取を評価する栄養報告書と全体的な食事を採点したスコアを受け取る可能性があります。一方、研究者は、腸に関連した健康状態など、関連するテーマについて詳しく学ぶことができるようになります。
</p>
<p class="consent_header">
  この研究に関連したリスクと守秘義務
</p>
<p class="consent_content">
  この研究に参加することで、一部の最小限のリスクや不快感が増加す可能性があります。調査に回答されている間に、欲求不満、感情的不快感、疲労、および／または退屈を感じるかもしれません。機密性が失われるリスクもありますが、皆様の身元を保護するためにあらゆる努力を払って、そのリスクを最小限にします。提供していただく全データは、米国サンディエゴUC San Diegoにある安全なシステムに保管され、厳しく限定された研究職員のみが直接身元が識別できる情報へアクセスを許可されています。参加者の個人情報とサンプル情報を保有したデータベースは、パスワードで保護されたサーバー上で運用され、Knight博士、共同研究者、プロジェクトおよびサンプルコーディネーター、IT管理者、データベースコーダー等の関連スタッフのみがアクセス可能です。データベースサーバーへは、UC San Diego(カリフォルニア大学サンディエゴ校)が管理するシステムからのネットワーク接続のみ許可しています。データベースサーバーはパスワード保護、ファイアウォールを使用、アクセス制御リストを使用し、高度かつ厳重にセキュリティ対策を施し、キーカード制御のUC San Diego(カリフォルニア大学サンディエゴ校)の施設内で保管しています。データベースのバックアップは夜間に実施し、同施設内の追加セキュリティ対策を施した別システムで管理されています。
</p>
<p class="consent_content">
  研究記録は、法律で許可される範囲で機密性が保持され、UC San DiegoのIRB（施設内審査委員会）によって審査される場合があります。
</p>
<p class="consent_content">
  私たちは小児、被扶養成人または高齢者の、身体的、性的、感情的、財政的虐待または放棄などの既知または合理的に疑われる事態について、報告する必要があります。いずれかの研究者がそのような情報を入手または提供された場合、彼らはそのような情報を適切な当局に報告する可能性があります。
</p>
<p class="consent_content">
  連邦および州の法律は全般的に、健康保険会社、グループ健康保険プラン、および大半の雇用者が、あなたの遺伝的情報に基づいて差別することを違法としています。この法律は、次の方法であなたを保護します： a) 健康保険会社とグループ健康保険プランが、この研究から得られる遺伝的情報を求めることはできません。b) 健康保険会社とグループ健康保険プランは、あなたの適格性または保険の掛け金に関して決定する際に、あなたの遺伝的情報を使うことはできません。c) 5名以上の従業員を有する雇用者は、この研究から取得する遺伝情報を、雇用、昇進、または解雇、またはあなたの雇用条件を設定する際に使用することはできません。
</p>
<p class="consent_content">
  これらの法律は、生命保険、障害保険、または介護保険を販売する会社による遺伝的差別に対してあなたを保護しない点にご注意ください。
</p>
<p class="consent_header">
  研究に参加する意思がなくなったとき、もしくは、参加資格を失う場合の規定
</p>
<p class="consent_content">
  この研究への参加は完全に自由意志によるものであり、参加を拒否することもできます。参加者はいつでも参加を拒否または撤回する権利があり、処罰を課されたり、ご自身の利益を失う事はありません。<br />
  もう研究参加を続けたくない場合は、オンラインアカウントを通して、ご自分のプロファイルおよび／またはアカウントの削除を要請することで、同意を取り下げることができます。どの質問を飛ばして回答してもかまいません。
</p>
<p class="consent_header">
  この研究への参加に対する謝礼の有無
</p>
<p class="consent_content">
  この研究に対する金銭的な謝礼はありません。
</p>
<p class="consent_header">
  この研究参加に関連する費用
</p>
<p class="consent_content">
  標準的な調査／質問票の記入には費用はかかりません。
</p>
<p class="consent_header">
  こので収集する情報
</p>
<p class="consent_content">
  この研究の一環として、あなたに関する情報や参加に関連する情報を、参加者や協力者から入手し作成することで、研究を適切に実施することができます。研究調査データには、連絡先情報、人口統計的情報、個人的経験、ライフスタイルの好み、健康情報、生年月日、意見や価値観が含まれます。
</p>
<p class="consent_header">
  個人データの使用方法
</p>
<p class="consent_content">
  提供していただく個人データは、次の目的に使用されます：
  <ul>
    <li>研究チームのメンバーと共有し、研究を適切に実施できるようにする。</li>
    <li>その他の研究者による将来の研究または追加研究のため。</li>
    <li>あなたの参加状態についての警告の通知、全般的なプログラムの更新、新規または将来の研究への参加への勧誘、および／または質問票へのあなたの回答に対する追跡調査としてあなたに連絡するため。</li>
    <li>この研究を監督する規制当局とデータを共有する要件を含む、法的および規制要件を遵守するため。</li>
    <li>この調査の適切な実施と研究の完全性を確認するため。</li>
  </ul>
</p>
<p class="consent_header">
  個人データの保持
</p>
<p class="consent_content">
  研究目的を達成し、研究の完全性を確実にするために必要な限り、調査実施者はあなたの個人データを保持する可能性があります。この研究でもはや不要となった時、またはあなたが参加同意を取り下げた場合は、削除することがこの研究プロジェクトの目的達成を不可能にしたり深刻に損なったりしない限り、あなたの個人データを削除します。しかし、法的または規制要件を遵守するために必要なあなたの情報は保持されます。
</p>
<p class="consent_header">
  あなたのプライバシー権
</p>
<p class="consent_content">
  一般データ保護規則（「GDPR」）は、あなたが欧州連合（EU）または欧州経済領域（EEA）内に居住している場合、いつ研究データを収集して使用するかについて、研究者があなたに情報を提供することを義務付けています。GDPRは、あなたの個人情報のアクセス、修正、制限、取り下げの権利を含む、個人データに関連した権利を参加者に提供します。
</p>
<p class="consent_content">
  研究チームは、米国内の研究施設であなたの個人データを保管し処理します。米国には、 EU/EEA内の国のように、あなたの個人データを保護するための同様な法律はありません。しかし研究チームは、あなたの個人データの機密性を保護することに全力を尽くします。保護についての追加情報は、この同意文書に含まれています。
</p>
<p class="consent_header">
  お問い合わせ先
</p>
<p class="consent_content">
  ご質問または研究に関連して問題がある場合は、Rob Knight博士に電話をするか、ヘルプアカウントにメールをお送りください。
</p>
<p class="consent_content">
  電話：+1) 858-246-1184 <br />
  メール:  microsetta@ucsd.edu
</p>
<p class="consent_content">
  研究被験者としての権利に関する質問や研究関連の問題を報告するには、UC San Diego(カリフォルニア大学サンディエゴ校)のIRB管理オフィスに電話（+1)858-246-4777）かメール（irb@ucsd.edu）で連絡してください。
</p>
<p class="consent_content">
  あなたの個人データの取り扱い、または全般的なプライバシーの実践についてご質問または苦情がある場合は、遠慮なくUC San Diego(カリフォルニア大学サンディエゴ校)のucsdprivacy@ucsd.eduまでメールをお送りください。
</p>
<p class="consent_header">
  署名と同意
</p>
<p class="consent_content">
  この同意文書のコピーおよび「<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">研究被験者の権利章典</a>」のコピーを保管のためにダウンロードすることができます。
</p>
<p class="consent_content">
  同意は完全に自由意志によるものですが、その提出を拒否される場合、この研究に参加できなくなる可能性があります。
</p>', true, '000fc4cd-8fa4-db8b-e050-8a800c5d81b7');
INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id)
    VALUES ('adult_biospecimen', 'ja_JP', NOW(), '<p class="consent_title">
  <strong>University of California San Diego (カリフォルニア大学サンディエゴ校)<br />
  研究被験者として行動することへの同意書</strong>
</p>
<p class="consent_title">
  <strong>Microsetta Initiative（マイクロセッタ・イニシアチブ）
  生物学的標本と将来の研究への使用</strong>
<p>
<p class="consent_header">
  研究実施者、参加者が参加を求められている理由、あなたが選択された方法、この研究の参加者人数について
</p>
<p class="consent_content">
  Dr. Rob Knight（ロブ・ナイト博士）は、ヒトの体表と体内に住む何兆もの細菌と他の微生物全て（微生物叢と呼ばれます）について、詳細を知るための研究を実施しています。これには、真菌や寄生虫のような真核生物と細菌、古細菌、ウイルスのような原核生物が含まれます。ヒトの体に共生する微生物は、地球上の他の誰とも違う固有なものです。個人ごとに違う細菌叢を調べるため、ぜひこの研究へご参加ください。この研究には、米国全体と世界中の国から、約500,000人が参加します。
</p>
<p class="consent_header">
  この研究が実施される理由
</p>
<p class="consent_content">
  この研究の目的は、人々の間の腸内の細菌叢の違いをより正確に評価して、これらの違いが、ライフスタイル、食事、体型、年齢、または病気の存在に関連しているのかを調べることです。 この研究では研究参加者の体から得られる便検体などのサンプル（生物学的標本）を研究目的に使います。この研究では、研究参加者の情報と生物学的標本を採取、保管、使用することが含まれています。本研究の結果として、生物学的標本由来のDNA配列、そしてサンプル提供者の詳細に関する情報が得られ、それらはデータベースに格納されます。この情報はは、腸管関連の健康状態などの関連テーマを研究するために公に公開さて、一般に使用できるようになります。
</p>
<p class="consent_header">
  この研究中に参加者に行なわれること
</p>
<p class="consent_content">
  生物学的標本の採取と処理に同意すると、以下の作業を行って頂きます。
</p>
<p class="consent_content">
  採便キットお受け取りください。キットにはサンプルを採取するのに使われる器具と使用方法が含まれています。採取器具にはサンプルを保存し、感染性がないようにするために95%エタノールが含まれています。それらを使って、キットに同封の指示書、または研究員の指示に従って、ご自分でサンプルを採取してください。また、サンプルが採取された日付と時刻などの、基本的な情報の提供をお願いします。全サンプルは、指示に従って、付属の容器に入れてご返送ください。
</p>
<p class="consent_content">
  便採取は、使用したトイレットペーパーに付着した便にキット専用の綿棒の先端をこすり付け、その綿棒を付属のプラスチック製の容器の中に入れます。
</p>
<p class="consent_content">
  サンプルの分析が終了すると、報告書を閲覧する為のリンクをメールでお送りします。自身のアカウントに報告書をアップロードします。お送りするまで1〜3か月かかります。ご了承ください。
</p>
<p class="consent_header">
  各研究手順の所要時間、研究参加者が参加する合計時間、研究の持続期間
</p>
<p class="consent_content">
  便サンプルの採取所用時間は5分以下ですが、この研究は何年も継続することが予想されます。
</p>
<p class="consent_header">
  この研究に関連したリスク
</p>
<p class="consent_content">
  この研究への参加者のプライバシーは保護されます。個人情報の保護のため万全のシステムを導入し情報漏洩を防止します。​しかしながら、現時点では予測できない事象による参加者の個人情報漏洩のリスクなど、いくつかの付加的なリスクを伴う可能性はあります。<br />
  本調査は研究であるため、現時点では予測できない未知のリスクが存在する可能性があります。
</p>
<p class="consent_content">
  重要な新知見が得られた場合は、お知らせします。
</p>
<p class="consent_header">
  研究に参加する意思がなくなったとき、もしくは、参加資格を失う場合の規定
</p>
<p class="consent_content">
  参加は義務ではありません。この研究への参加は完全に自由意志によるものであり、参加を拒否することもできます。参加の意思に影響を及ぼす可能性のある重要な新しい情報がこの研究中に見つかった場合はお知らせします。参加者はいつでも参加を拒否または撤回する権利があり、処罰を課されたり、ご自身の利益を失う事はありません。<br />
  もう研究参加を続けたくない場合は、オンラインアカウントを通して、ご自分のプロファイルおよび／またはアカウントの削除を要請することで、同意を取り下げることができます。
</p>
<p class="consent_content">
  研究担当者の指示に従わない場合、研究参加を取り消される可能性があります。
</p>
<p class="consent_header">
  得られると予想される利益
</p>
<p class="consent_content">
  この研究参加には、金銭的または直接的な利益はありません。研究参加者の生物学的標本に関する分析の詳細な報告書、そして微生物叢の構成を他の研究参加者と比較した正確な情報を受け取ることが出来ます。
</p>
<p class="consent_header">
  生物学的標本の採取参加に関連にかかる費用
</p>
<p class="consent_content">
  このサンプル採取に対し参加者に費用はかかりません。
</p>
<p class="consent_header">
  秘匿性とは
</p>
<p class="consent_content">
  研究記録は、個人情報の保護に関する米国の法律の下で秘匿されます。研究参加の一環として、研究参加者は個人情報を提供します。その情報とは、氏名、生年月日、住所など、公表されると研究参加者の身元を特定できるものです。研究参加者のプライバシー保護の為、本プロジェクトは細心の注意を払います。提供していただく全データは、米国サンディエゴUC San Diegoにある安全なシステムに保管され、限定された研究職員のみが直接身元が識別できる情報へアクセスを許可されています。参加者の個人情報とサンプル情報を保有したデータベースは、パスワードで保護されたサーバー上で運用され、Knight博士、共同研究者、プロジェクトおよびサンプルコーディネーター、IT管理者、データベースコーダー等の関連スタッフのみがアクセス可能です。データベースサーバーへは、UC San Diego(カリフォルニア大学サンディエゴ校)が管理するシステムからのネットワーク接続のみ許可しています。データベースサーバーはパスワード保護、ファイアウォールを使用、アクセス制御リストを使用し、高度かつ厳重にセキュリティ対策を施し、キーカード制御のUC San Diego(カリフォルニア大学サンディエゴ校)の施設内で保管しています。データベースのバックアップは夜間に実施し、同施設内の追加セキュリティ対策を施した別システムで管理されています。サンプルの解析は、直接身元を識別できる情報を取り除いたデータを使って実施され、公的保管機関で共有される全データもこの処理を行います。<br />
  研究記録は、UC San DiegoのIRB（施設内審査委員会）によって審査される場合があります。
</p>
<p class="consent_header">
  研究参加者のサンプルが使用される方法
</p>
<p class="consent_content">
  研究参加者のデータと生物学的標本の解析から得られる情報は ヒト以外のDNA（例：細菌のDNA）が研究に使用されます。本プロジェクトのサンプルから取得したデータ（研究参加者のものを含む）は、科学論文に発表される可能性があります。<br />
  一部のサンプルは、RNA、タンパク質、または代謝物などの他の化合物を使う追加研究を行う研究者が使用するために保持される場合があります。 その場合は、使用または共有前に、身元を識別できる全情報を取り除きます。<br />
  身元識別情報を取り除いた後は、今後の研究で研究参加者のデータ、サンプルの使用または共有について、都度同意を求めることはありません。加えて、身元識別情報を取り除いたデータは、欧州バイオインフォマティクス研究所（http://www.ebi.ac.uk）およびQiita （https://qiita.ucsd.edu）などにアップロードされ、他の研究者のアクセスと使用を可能とします。将来研究参加者のサンプルを処理する為に追加情報または何らかの措置が必要となった場合には再度同意のお願いの連絡をする場合があります。
</p>
<p class="consent_content">
  この研究で参加者から採取される生物学的標本とその情報は、この研究または他の研究に使用され、他の組織と共有される場合があります。この生物学的標本とその情報の使用により得られた商業的価値や利益は参加者に共有されません。
</p>
<p class="consent_header">
  注記
</p>
<p class="consent_content">
  この研究または将来の研究の一環として、 ヒトDNAは分析されることはありません。さらに、サンプルの中の微生物の特定に使われる解析手法は<strong>病気や感染症の診断には使用しません</strong>。
</p>
<p class="consent_header">
  お問い合わせ先
</p>
<p class="consent_content">
  ご質問または研究関連の問題がある場合はRob Knight博士に電話するか、ヘルプアカウントにメールをお送りください。<br />
  電話：+1) 858-246-1184 <br />
  メール:  microsetta@ucsd.edu
</p>
<p class="consent_header">
  署名と同意
</p>
<p class="consent_content">
  この同意文書のコピーおよび「<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">調査対象の権利章典</a>」のコピーを保管のためにダウンロードすることができます。
</p>
<p class="consent_content">
  同意は完全に自由意志によるものですが、同意を拒否される場合、この研究への参加およびサンプルの処理ができなくなる可能性があります。
</p>', true, '000fc4cd-8fa4-db8b-e050-8a800c5d81b7');