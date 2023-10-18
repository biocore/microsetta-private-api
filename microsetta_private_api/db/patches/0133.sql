-- Create the table that will house external reports
-- NB: The file_title column will not go through any translation mechanisms. It might be wise to revisit this in the future, but since our only current use
-- is for highly specific documents with a pre-defined language (FFQs from the THDMI Japan project), the approach makes sense.

-- The report_type value will dictate which section of the My Reports tab it displays under.
-- I'm setting the enum up to reflect current structure (sample = My Kits/ffq = My FFQs) but this could be extended to "Other" or various specifics later.
CREATE TYPE EXTERNAL_REPORT_TYPE AS ENUM ('sample', 'ffq');
CREATE TABLE ag.external_reports (
    external_report_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_id UUID NOT NULL,
    file_name VARCHAR NOT NULL, -- The file name that will be used when the user downloads the file
    file_title VARCHAR NOT NULL, -- The label that will be displayed in the UI when the user views their list of reports
    file_type VARCHAR NOT NULL, -- The Content-Type header that Interface will use to render the file for display/download
    file_contents BYTEA NOT NULL,
    report_type EXTERNAL_REPORT_TYPE NOT NULL,

    CONSTRAINT fk_external_reports_source FOREIGN KEY (source_id) REFERENCES ag.source (id)
);

-- Add Japanese translations for survey groups
UPDATE ag.survey_group SET japanese = '基本情報' WHERE group_order = -10; -- Basic Information
UPDATE ag.survey_group SET japanese = '自宅において' WHERE group_order = -11; -- At Home
UPDATE ag.survey_group SET japanese = '生活様式' WHERE group_order = -12; -- Lifestyle
UPDATE ag.survey_group SET japanese = '消化器' WHERE group_order = -13; -- Gut
UPDATE ag.survey_group SET japanese = '健康全般' WHERE group_order = -14; -- General Health
UPDATE ag.survey_group SET japanese = '健康診断' WHERE group_order = -15; -- Health Diagnosis
UPDATE ag.survey_group SET japanese = 'アレルギー' WHERE group_order = -16; -- Allergies
UPDATE ag.survey_group SET japanese = '食事' WHERE group_order = -17; -- Diet
UPDATE ag.survey_group SET japanese = '食事の詳細' WHERE group_order = -18; -- Detailed Diet
UPDATE ag.survey_group SET japanese = '他の' WHERE group_order = -22; -- Other

-- Add missing Japanese translations for survey questions
UPDATE ag.survey_question SET japanese = 'どれくらい定期的にチームスポーツに参加していますか？' WHERE survey_question_id = 333;
UPDATE ag.survey_question SET japanese = '園芸や庭仕事をする回数は、シーズン中どれくらいですか？' WHERE survey_question_id = 334;
UPDATE ag.survey_question SET japanese = '通常、どのような運動をしますか？該当するものをすべて選択してください。' WHERE survey_question_id = 331;
UPDATE ag.survey_question SET japanese = 'アプリを使用して次のいずれかを追跡していますか？該当するものをすべて選択してください。' WHERE survey_question_id = 328;
UPDATE ag.survey_question SET japanese = '出生時の生物学的性別' WHERE survey_question_id = 502;
UPDATE ag.survey_question SET japanese = '次のうち、ご自身に最もあてはまるものはどれでしょうか？' WHERE survey_question_id = 492;
UPDATE ag.survey_question SET japanese = 'あなたの最終学歴は何ですか？' WHERE survey_question_id = 493;
UPDATE ag.survey_question SET japanese = 'お住まいの地域に最も当てはまるのは、次のうちどれですか？' WHERE survey_question_id = 313;
UPDATE ag.survey_question SET japanese = '家畜をよく触ったり定期的に触ったりすることはありますか？' WHERE survey_question_id = 326;
UPDATE ag.survey_question SET japanese = 'この研究に参加していて、そのことをあなたに自発的に伝えた人々と、あなたとの関係（パートナー、子供など）をお答えください。' WHERE survey_question_id = 316;
UPDATE ag.survey_question SET japanese = '種類／商品名：' WHERE survey_question_id = 490;
UPDATE ag.survey_question SET japanese = 'この研究に参加していて、そのことをあなたに自発的に伝えた同居人は誰ですか？' WHERE survey_question_id = 319;
UPDATE ag.survey_question SET japanese = '参加者名' WHERE survey_question_id = 508;
UPDATE ag.survey_question SET japanese = 'この人とあなたは血のつながりがありますか？' WHERE survey_question_id = 509;
UPDATE ag.survey_question SET japanese = 'この人はあなたと一緒に住んでいますか？' WHERE survey_question_id = 510;
UPDATE ag.survey_question SET japanese = 'あなたの犬は主にどこにいますか？' WHERE survey_question_id = 501;
UPDATE ag.survey_question SET japanese = 'あなたの猫は主にどこにいますか？' WHERE survey_question_id = 503;
UPDATE ag.survey_question SET japanese = '歯磨きは1日何回していますか？' WHERE survey_question_id = 495;
UPDATE ag.survey_question SET japanese = '通常、どれくらい激しい運動をしますか？該当するものをすべて選択してください。' WHERE survey_question_id = 332;
UPDATE ag.survey_question SET japanese = '通常、どのような種類のアルコールを飲みますか？該当するものをすべて選択してください。' WHERE survey_question_id = 494;
UPDATE ag.survey_question SET japanese = '硝酸塩' WHERE survey_question_id = 517;
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どのタイプのIBDですか？' WHERE survey_question_id = 360;
UPDATE ag.survey_question SET japanese = '過去1週間に、腹痛や腹部不快感を感じたことはどれくらいありましたか？' WHERE survey_question_id = 362;
UPDATE ag.survey_question SET japanese = '過去1週間に、腹部膨満感が起こったことはどれくらいありましたか？' WHERE survey_question_id = 363;
UPDATE ag.survey_question SET japanese = '過去1週間に、膨満感（おならが出る）を感じたことはどれくらいありましたか？' WHERE survey_question_id = 364;
UPDATE ag.survey_question SET japanese = '過去1週間で、お腹が鳴る／胃が鳴ることはどれくらいありましたか？' WHERE survey_question_id = 365;
UPDATE ag.survey_question SET japanese = 'ホルモン' WHERE survey_question_id = 518;
UPDATE ag.survey_question SET japanese = '今までに皮膚疾患の診断を受けたことはありますか？' WHERE survey_question_id = 500;
UPDATE ag.survey_question SET japanese = '現在、何らかのホルモン避妊法を使用していますか？' WHERE survey_question_id = 497;
UPDATE ag.survey_question SET japanese = 'どのような皮膚疾患と診断されましたか？' WHERE survey_question_id = 374;
UPDATE ag.survey_question SET japanese = 'その皮膚疾患はどのように診断されましたか？' WHERE survey_question_id = 375;
UPDATE ag.survey_question SET japanese = '出産予定日：' WHERE survey_question_id = 370;
UPDATE ag.survey_question SET japanese = '過去1ヶ月間におけるあなたの平均的なストレスレベルを、1を「ストレスがほとんどまたは全くない」、10を「かなりのストレス」とした10段階で評価してください。' WHERE survey_question_id = 387;
UPDATE ag.survey_question SET japanese = '診断されたのはいつ頃ですか？' WHERE survey_question_id = 407;
UPDATE ag.survey_question SET japanese = '今までに精神疾患と診断されたことはありますか？' WHERE survey_question_id = 504;
UPDATE ag.survey_question SET japanese = 'どのような種類のがんを患っています／いましたか？該当するものをすべて選択してください。' WHERE survey_question_id = 409;
UPDATE ag.survey_question SET japanese = 'どのタイプの治療を受け／利用しましたか？該当するものをすべて選択してください。' WHERE survey_question_id = 410;
UPDATE ag.survey_question SET japanese = '次のうち、片頭痛に伴う全ての症状にチェックを入れてください。' WHERE survey_question_id = 487;
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どの障害かを次のリストから選択してください：' WHERE survey_question_id = 505;
UPDATE ag.survey_question SET japanese = 'それはどのように診断されましたか？' WHERE survey_question_id = 413;
UPDATE ag.survey_question SET japanese = 'どのような頻度で片頭痛がしますか？' WHERE survey_question_id = 485;
UPDATE ag.survey_question SET japanese = '回答が「はい」の場合、どのタイプの糖尿病かを選択してください：' WHERE survey_question_id = 506;
UPDATE ag.survey_question SET japanese = '現在、がんを患っていますか？' WHERE survey_question_id = 408;
UPDATE ag.survey_question SET japanese = 'あなたの一番血のつながりが近い親族（一親等）で、片頭痛に悩まされている人はいますか？' WHERE survey_question_id = 488;
UPDATE ag.survey_question SET japanese = 'あなたは片頭痛用の薬を飲んでいますか。' WHERE survey_question_id = 489;
UPDATE ag.survey_question SET japanese = '片頭痛を起こす主な原因を、「1」が最も可能性が高い、「2」が2番目に可能性が高いとして、ランク付けしてください。片頭痛を引き起こす原因でないものは、空白のままにしておいてください。' WHERE survey_question_id = 511;
UPDATE ag.survey_question SET japanese = 'カフェイン' WHERE survey_question_id = 512;
UPDATE ag.survey_question SET japanese = '抑うつ' WHERE survey_question_id = 513;
UPDATE ag.survey_question SET japanese = '睡眠不足' WHERE survey_question_id = 514;
UPDATE ag.survey_question SET japanese = '食品（ワイン、チョコレート、イチゴ）' WHERE survey_question_id = 515;
UPDATE ag.survey_question SET japanese = 'バルビツレートまたはオピオイドを含む医薬品' WHERE survey_question_id = 516;
UPDATE ag.survey_question SET japanese = '今までに他に何かの病気の症状で診断を受けたことはありますか？' WHERE survey_question_id = 499;
UPDATE ag.survey_question SET japanese = '症状を和らげるために薬を服用していますか？' WHERE survey_question_id = 415;
UPDATE ag.survey_question SET japanese = '断続的な断食をする場合、どのよう種類の断食をしますか？' WHERE survey_question_id = 423;
UPDATE ag.survey_question SET japanese = '通常、1日に何回食事をしますか？' WHERE survey_question_id = 425;
UPDATE ag.survey_question SET japanese = '通常、1日に何回軽食（おやつ）を食べますか？' WHERE survey_question_id = 426;
UPDATE ag.survey_question SET japanese = '毎日のカロリーのほとんどはいつ摂取しますか？' WHERE survey_question_id = 427;
UPDATE ag.survey_question SET japanese = '繊維サプリメントを服用する場合、どのような種類のものを服用していますか？該当するものをすべて選択してください。' WHERE survey_question_id = 433;
UPDATE ag.survey_question SET japanese = 'あなたは母乳や調整粉乳から栄養のほとんどを受け取っている乳児ですか、それとも成人用栄養シェイクから栄養のほとんど（1日のカロリーの75%以上）を受け取っている成人ですか？' WHERE survey_question_id = 498;
UPDATE ag.survey_question SET japanese = '上記に記載されていないその他の特殊な食事制限があったら列挙／説明してください。' WHERE survey_question_id = 424;
UPDATE ag.survey_question SET japanese = '通常、寝る前の最後の食事や軽食を何時に食べますか？' WHERE survey_question_id = 428;
UPDATE ag.survey_question SET japanese = '繊維サプリメントをどれくらいの回数服用していますか？' WHERE survey_question_id = 434;
UPDATE ag.survey_question SET japanese = '普通の1週間に、繊維含有量の多い強化食品（例： Fiber One ）はどれくらい食べていますか？' WHERE survey_question_id = 443;
UPDATE ag.survey_question SET japanese = '自宅で飲む、味のついていない普通の飲料水は主にどういうものですか？これには静水または発泡水／炭酸水も含められます。' WHERE survey_question_id = 474;
UPDATE ag.survey_question SET japanese = '自宅の外で飲む、味のついていない普通の飲料水は主にどういうものですか？これには静水または発泡水／炭酸水も含められます。' WHERE survey_question_id = 476;
UPDATE ag.survey_question SET japanese = '発酵食品を食べ始めたのはいつですか？' WHERE survey_question_id = 478;
UPDATE ag.survey_question SET japanese = '通常、一度にどのくらい飲みますか？' WHERE survey_question_id = 462;
UPDATE ag.survey_question SET japanese = '質問24および／または25の回答が「はい」の場合、定期的に摂取するノンカロリーまたは低カロリーの甘味料はどのような種類のものですか？該当するものをすべて選択してください。' WHERE survey_question_id = 464;
UPDATE ag.survey_question SET japanese = '自宅で水を飲む前に、追加の処理（ろ過を除く）を施していますか（例：沸騰、浄化タブレット、塩素／漂白剤） ？' WHERE survey_question_id = 475;
UPDATE ag.survey_question SET japanese = '自宅の外で水を飲む前に、追加の処理（沸騰、浄化錠、塩素/漂白剤など）を施しますか ？' WHERE survey_question_id = 477;
UPDATE ag.survey_question SET japanese = '今までにがんと診断されたことはありますか？' WHERE survey_question_id = 507;
UPDATE ag.survey_question SET japanese = '自宅で使用する水の水源は何ですか？' WHERE survey_question_id = 519;
UPDATE ag.survey_question SET japanese = 'お住まいの地域の公共用水の水源は何ですか？' WHERE survey_question_id = 520;
UPDATE ag.survey_question SET japanese = '海のアクテビティ（水泳、サーフィン、シュノーケリングなど）を定期的にしていますか？' WHERE survey_question_id = 354;
UPDATE ag.survey_question SET japanese = 'これまで新型コロナウィルスに何回感染しましたか？' WHERE survey_question_id = 521;
UPDATE ag.survey_question SET japanese = '過敏性腸症候群（IBS）と診断されたことはありますか？注：IBSはIBDと異なります。 IBSは症状、通常再発性腹痛と排便の変化によって定義されます。 IBDは、炎症または胃腸管の内側の損傷によって判断されています。' WHERE survey_question_id = 79;
UPDATE ag.survey_question SET japanese = '現在（過去2週間ほど）の寝つき（入眠障害）の程度を教えてください。' WHERE survey_question_id = 229;
UPDATE ag.survey_question SET japanese = '現在（過去2週間ほど）の中途覚醒（何度も目覚める）の程度を教えて下さい。' WHERE survey_question_id = 230;
UPDATE ag.survey_question SET japanese = '現在（過去2週間ほど）の早朝覚醒（朝早く目覚めてしまう）の程度を教えて下さい。' WHERE survey_question_id = 231;
UPDATE ag.survey_question SET japanese = '現在の睡眠パターンにどの程度満足/不満を感じていますか？' WHERE survey_question_id = 232;
UPDATE ag.survey_question SET japanese = '睡眠障害があなたの生活に悪影響を与えている事をまわりの人はどの程度気づいていると思いますか？' WHERE survey_question_id = 233;
UPDATE ag.survey_question SET japanese = 'あなたは自身の睡眠障害をどの程度辛く感じていますか？' WHERE survey_question_id = 234;
UPDATE ag.survey_question SET japanese = '現在、睡眠障害が毎日の生活に支障をきたしていますか？（日中の疲労、機嫌、仕事、家事の生産性、集中力、記憶力など）' WHERE survey_question_id = 235;

-- Add missing translations for survey responses
UPDATE ag.survey_response SET japanese = '0' WHERE american = '0';
UPDATE ag.survey_response SET japanese = '10' WHERE american = '10';
UPDATE ag.survey_response SET japanese = '12 ～ 16液量オンス（355 ～ 473 ml）' WHERE american = '12-16 fl oz (355-473 ml)';
UPDATE ag.survey_response SET japanese = '16 ～ 20液量オンス（473 ～ 591 ml）' WHERE american = '16-20 fl oz (473-591 ml)';
UPDATE ag.survey_response SET japanese = '2' WHERE american = '2';
UPDATE ag.survey_response SET japanese = '1日2回' WHERE american = '2 times a day';
UPDATE ag.survey_response SET japanese = '週に2～3日' WHERE american = '2-3 days per week';
UPDATE ag.survey_response SET japanese = '２４時間断食（別名、イート・ストップ・イート法）' WHERE american = '24 hour fast (aka eat-stop-eat method)';
UPDATE ag.survey_response SET japanese = '3' WHERE american = '3';
UPDATE ag.survey_response SET japanese = '4' WHERE american = '4';
UPDATE ag.survey_response SET japanese = '週に4～6日' WHERE american = '4-6 days per week';
UPDATE ag.survey_response SET japanese = '4〜8液量オンス（118〜237 ml）' WHERE american = '4-8 fl oz (118-237 ml)';
UPDATE ag.survey_response SET japanese = '5' WHERE american = '5';
UPDATE ag.survey_response SET japanese = '５：２方法' WHERE american = '5:2 method';
UPDATE ag.survey_response SET japanese = '6' WHERE american = '6';
UPDATE ag.survey_response SET japanese = '7' WHERE american = '7';
UPDATE ag.survey_response SET japanese = '8' WHERE american = '8';
UPDATE ag.survey_response SET japanese = '8〜12液量オンス（237〜355 ml）' WHERE american = '8-12 fl oz (237-355 ml)';
UPDATE ag.survey_response SET japanese = '9' WHERE american = '9';
UPDATE ag.survey_response SET japanese = '< 4液量オンス（< 118 ml ）' WHERE american = '<4 fl oz (<118 ml)';
UPDATE ag.survey_response SET japanese = '> 20液量オンス（> 591 ml）' WHERE american = '>20 fl oz (>591 ml)';
UPDATE ag.survey_response SET japanese = '年に数回' WHERE american = 'A few times a year';
UPDATE ag.survey_response SET japanese = 'アセスルファムカリウム' WHERE american = 'Acesulfame potassium';
UPDATE ag.survey_response SET japanese = '身体活動／運動' WHERE american = 'Activity/exercise';
UPDATE ag.survey_response SET japanese = '副腎がん' WHERE american = 'Adrenal cancer';
UPDATE ag.survey_response SET japanese = 'エアロビック／有酸素トレーニング' WHERE american = 'Aerobic/cardio training';
UPDATE ag.survey_response SET japanese = '隔日断食' WHERE american = 'Alternate day fasting';
UPDATE ag.survey_response SET japanese = 'リンゴの食物繊維' WHERE american = 'Apple fiber';
UPDATE ag.survey_response SET japanese = 'アジア人' WHERE american = 'Asian';
UPDATE ag.survey_response SET japanese = 'アスパルターム' WHERE american = 'Aspartame';
UPDATE ag.survey_response SET japanese = '準学士号（AA、ASなど）' WHERE american = 'Associate''s degree (e.g. AA, AS))';
UPDATE ag.survey_response SET japanese = 'オーラ' WHERE american = 'Aura';
UPDATE ag.survey_response SET japanese = '学士号（BA、BSなど）' WHERE american = 'Bachelor''s degree (e.g. BA, BS)';
UPDATE ag.survey_response SET japanese = 'バランストレーニング' WHERE american = 'Balance training';
UPDATE ag.survey_response SET japanese = '黒人またはアフリカ系アメリカ人' WHERE american = 'Black or African American';
UPDATE ag.survey_response SET japanese = '膀胱がん' WHERE american = 'Bladder cancer';
UPDATE ag.survey_response SET japanese = 'ないはずの体の部分に痛みがある；' WHERE american = 'Body pain where it shouldn''t exist;';
UPDATE ag.survey_response SET japanese = '瓶詰めされた*精製水（ラベルに「湧き水」あるいは「天然ミネラルウォーター」とは表示されていない）' WHERE american = 'Bottled* purified water (does not indicate "spring water" or "natural mineral water" on the label)';
UPDATE ag.survey_response SET japanese = '脳がん（神経膠腫および神経膠芽腫を含む）' WHERE american = 'Brain cancer (includes gliomas and glioblastomas)';
UPDATE ag.survey_response SET japanese = '乳がん' WHERE american = 'Breast cancer';
UPDATE ag.survey_response SET japanese = 'カロリーは1日にわたって均等に分配している' WHERE american = 'Calories are evenly distributed throughout the day';
UPDATE ag.survey_response SET japanese = '子宮頸がん' WHERE american = 'Cervical cancer';
UPDATE ag.survey_response SET japanese = '胆管がん' WHERE american = 'Cholangiocarcinoma';
UPDATE ag.survey_response SET japanese = '結腸がん' WHERE american = 'Colon cancer';
UPDATE ag.survey_response SET japanese = '結腸クローン病' WHERE american = 'Colonic Crohn''s disease';
UPDATE ag.survey_response SET japanese = '現在幼稚園〜高等学校' WHERE american = 'Currently in K-12';
UPDATE ag.survey_response SET japanese = '毎日の時間制限付き断食（time-restricted eating、TRE）' WHERE american = 'Daily time-restricted eating (TRE)';
UPDATE ag.survey_response SET japanese = '飲食物' WHERE american = 'Diet';
UPDATE ag.survey_response SET japanese = '博士号（例：PhD、EdD）' WHERE american = 'Doctorate (eg. PhD, EdD)';
UPDATE ag.survey_response SET japanese = '食道がん' WHERE american = 'Esophageal cancer';
UPDATE ag.survey_response SET japanese = '年に数回' WHERE american = 'Few times/year';
UPDATE ag.survey_response SET japanese = 'ろ過された水道水（ピッチャー、蛇口または流し台下の浄水器、逆浸透システム、軟水器）' WHERE american = 'Filtered tap water (pitcher, faucet or under the sink water purifiers, reverse osmosis systems, water softener)';
UPDATE ag.survey_response SET japanese = '柔軟性トレーニング' WHERE american = 'Flexibility training';
UPDATE ag.survey_response SET japanese = '強化ワイン' WHERE american = 'Fortified wine';
UPDATE ag.survey_response SET japanese = '機能性食品（例：チアシード、ふすま）' WHERE american = 'Functional food (e.g. chia seeds, wheat bran)';
UPDATE ag.survey_response SET japanese = '全般性不安障害' WHERE american = 'Generalized anxiety disorder';
UPDATE ag.survey_response SET japanese = 'リンゴ酒' WHERE american = 'Hard cider';
UPDATE ag.survey_response SET japanese = 'ハードコンブチャ（アルコール入り紅茶キノコ）' WHERE american = 'Hard kombucha';
UPDATE ag.survey_response SET japanese = 'ハードセルツァー' WHERE american = 'Hard seltzer';
UPDATE ag.survey_response SET japanese = 'ハードティー' WHERE american = 'Hard tea';
UPDATE ag.survey_response SET japanese = '頭頚部がん' WHERE american = 'Head and Neck cancer';
UPDATE ag.survey_response SET japanese = '高校卒業またはGED同等' WHERE american = 'High school diploma or GED equivalent';
UPDATE ag.survey_response SET japanese = 'ヒスパニック系またはラテン系' WHERE american = 'Hispanic or Latino';
UPDATE ag.survey_response SET japanese = 'ホメオパシー薬' WHERE american = 'Homeopathic medicines';
UPDATE ag.survey_response SET japanese = 'ホルモン療法' WHERE american = 'Hormone therapy';
UPDATE ag.survey_response SET japanese = '温熱療法' WHERE american = 'Hyperthermia';
UPDATE ag.survey_response SET japanese = '発酵食品は食べていない' WHERE american = 'I do not eat fermented foods';
UPDATE ag.survey_response SET japanese = '断続的な断食はしていない。' WHERE american = 'I do not practice intermittent fasting';
UPDATE ag.survey_response SET japanese = '食物繊維サプリメントは服用していません。' WHERE american = 'I do not take fiber supplements';
UPDATE ag.survey_response SET japanese = '自身の活動はいずれも追跡していません。' WHERE american = 'I do not track any of my activities';
UPDATE ag.survey_response SET japanese = '味のついていない普通の水は飲んでいない' WHERE american = 'I don''t drink plain, unflavored water';
UPDATE ag.survey_response SET japanese = 'サプリメントを服用しているが、どのような種類か知らない。' WHERE american = 'I take a supplement, but do not know what kind';
UPDATE ag.survey_response SET japanese = '回腸クローン病' WHERE american = 'Ileal Crohn''s disease';
UPDATE ag.survey_response SET japanese = '回腸結腸クローン病' WHERE american = 'Ileal and Colonic Crohn''s disease';
UPDATE ag.survey_response SET japanese = '免疫療法' WHERE american = 'Immunotherapy';
UPDATE ag.survey_response SET japanese = '午後' WHERE american = 'In the afternoon';
UPDATE ag.survey_response SET japanese = '夜' WHERE american = 'In the evening';
UPDATE ag.survey_response SET japanese = '午前中' WHERE american = 'In the morning';
UPDATE ag.survey_response SET japanese = 'イヌリン（例：Fiber Choice）' WHERE american = 'Inulin (e.g. Fiber Choice)';
UPDATE ag.survey_response SET japanese = '刺激性を受けやすい、あるいは日常的な行動を避ける；' WHERE american = 'Irritability or avoidance of routine;';
UPDATE ag.survey_response SET japanese = '一軒家／農家（人口100人未満）' WHERE american = 'Isolated house/farm (population is less than 100)';
UPDATE ag.survey_response SET japanese = '腎がん' WHERE american = 'Kidney cancer';
UPDATE ag.survey_response SET japanese = '白血病' WHERE american = 'Leukemia';
UPDATE ag.survey_response SET japanese = '肝臓がん' WHERE american = 'Liver cancer';
UPDATE ag.survey_response SET japanese = '肺がん' WHERE american = 'Lung cancer';
UPDATE ag.survey_response SET japanese = 'リンパ腫' WHERE american = 'Lymphoma';
UPDATE ag.survey_response SET japanese = '麦芽酒' WHERE american = 'Malt liquor';
UPDATE ag.survey_response SET japanese = '修士号（MS、MAなど）' WHERE american = 'Master''s degree (e.g. MS, MA)';
UPDATE ag.survey_response SET japanese = '黒色腫（皮膚）' WHERE american = 'Melanoma (skin)';
UPDATE ag.survey_response SET japanese = 'メチルセルロース（例：Citrucel）' WHERE american = 'Methylcellulose (e.g. Citrucel)';
UPDATE ag.survey_response SET japanese = '主要都市（人口100万人以上）' WHERE american = 'Metropolis (population is more than 1 million)';
UPDATE ag.survey_response SET japanese = 'モンクフルーツ' WHERE american = 'Monk fruit';
UPDATE ag.survey_response SET japanese = '毎月' WHERE american = 'Monthly';
UPDATE ag.survey_response SET japanese = '1日3回以上' WHERE american = 'More than 2 times a day';
UPDATE ag.survey_response SET japanese = '５杯以上' WHERE american = 'More than 4';
UPDATE ag.survey_response SET japanese = '多民族' WHERE american = 'Multiracial';
UPDATE ag.survey_response SET japanese = 'アメリカ先住民またはアラスカ先住民' WHERE american = 'Native American or Alaska Native';
UPDATE ag.survey_response SET japanese = 'ハワイまたは他の太平洋諸島の先住民' WHERE american = 'Native Hawaiian or Other Pacific Islander';
UPDATE ag.survey_response SET japanese = '欧州連合の他の国または英国で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* in another country in the European Union or the UK';
UPDATE ag.survey_response SET japanese = '欧州連合または英国以外の国で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* in another country not in the European Union or the UK';
UPDATE ag.survey_response SET japanese = '現地（例：居住国）で瓶詰めされた*天然のミネラルウォーターまたは湧き水' WHERE american = 'Natural mineral or spring water bottled* locally (i.e. in your country of residence)';
UPDATE ag.survey_response SET japanese = '吐き気および/または嘔吐；' WHERE american = 'Nausea and/or vomiting;';
UPDATE ag.survey_response SET japanese = '正規の教育は受けていない' WHERE american = 'No formal education';
UPDATE ag.survey_response SET japanese = 'いいえ、この病状はありません。' WHERE american = 'No, I do not have this condition';
UPDATE ag.survey_response SET japanese = 'いいえ、アレルギー用の薬は一切服用していません。' WHERE american = 'No, I do not take any medications for my allergies';
UPDATE ag.survey_response SET japanese = 'いいえ、がんはなくなりました。' WHERE american = 'No, I no longer have cancer';
UPDATE ag.survey_response SET japanese = 'エンバクの食物繊維' WHERE american = 'Oat fiber';
UPDATE ag.survey_response SET japanese = '週に1回' WHERE american = 'Once per week';
UPDATE ag.survey_response SET japanese = 'ラマダン期間中のみ' WHERE american = 'Only during Ramadan';
UPDATE ag.survey_response SET japanese = '卵巣がん' WHERE american = 'Ovarian cancer';
UPDATE ag.survey_response SET japanese = '膵臓がん' WHERE american = 'Pancreatic cancer';
UPDATE ag.survey_response SET japanese = '定期的な断食' WHERE american = 'Periodic fasting';
UPDATE ag.survey_response SET japanese = '褐色細胞腫および傍神経節腫がん' WHERE american = 'Pheochromocytoma and paraganglioma cancer';
UPDATE ag.survey_response SET japanese = '音恐怖症（音に対する敏感性）；' WHERE american = 'Phonophobia (sensitivity to sound);';
UPDATE ag.survey_response SET japanese = '光力学治療' WHERE american = 'Photodynamic therapy';
UPDATE ag.survey_response SET japanese = '光恐怖症（光に対する敏感性）；' WHERE american = 'Photophobia (sensitivity to light);';
UPDATE ag.survey_response SET japanese = '専門職学位（MD、DDS、DVMなど）' WHERE american = 'Professional degree (e.g. MD,DDS, DVM)';
UPDATE ag.survey_response SET japanese = '前立腺がん' WHERE american = 'Prostate cancer';
UPDATE ag.survey_response SET japanese = 'サイリウム（例：Metamucil）' WHERE american = 'Psyllium (e.g. Metamucil)';
UPDATE ag.survey_response SET japanese = '放射線療法' WHERE american = 'Radiotherapy';
UPDATE ag.survey_response SET japanese = '直腸がん' WHERE american = 'Rectal cancer';
UPDATE ag.survey_response SET japanese = 'ロゼ・ワイン' WHERE american = 'Rose wine';
UPDATE ag.survey_response SET japanese = 'サッカリン' WHERE american = 'Saccharin';
UPDATE ag.survey_response SET japanese = '日本酒' WHERE american = 'Sake';
UPDATE ag.survey_response SET japanese = '肉腫' WHERE american = 'Sarcoma';
UPDATE ag.survey_response SET japanese = '幼児期／小児期以降' WHERE american = 'Since infancy/childhood';
UPDATE ag.survey_response SET japanese = '睡眠' WHERE american = 'Sleep';
UPDATE ag.survey_response SET japanese = '小さな町または村（人口100人超、1,000人未満）' WHERE american = 'Small town or village (population is more than 100 and less than 1,000)';
UPDATE ag.survey_response SET japanese = 'サワービール' WHERE american = 'Sour beer';
UPDATE ag.survey_response SET japanese = '発泡ワイン' WHERE american = 'Sparkling wine';
UPDATE ag.survey_response SET japanese = 'ハードリカー／蒸留酒／強い酒' WHERE american = 'Spirits/liquors/hard alcohol';
UPDATE ag.survey_response SET japanese = '幹細胞移植' WHERE american = 'Stem cell transplant';
UPDATE ag.survey_response SET japanese = 'ステビア' WHERE american = 'Stevia';
UPDATE ag.survey_response SET japanese = '胃がん' WHERE american = 'Stomach cancer';
UPDATE ag.survey_response SET japanese = '筋力トレーニング' WHERE american = 'Strength training';
UPDATE ag.survey_response SET japanese = 'スクラロース' WHERE american = 'Sucralose';
UPDATE ag.survey_response SET japanese = '糖アルコール（ソルビトール、キシリトール、ラクチトール、マンニトール、エリスリトール、マルチトール）' WHERE american = 'Sugar alcohols (sorbitol, xylitol, lactitol, mannitol, erythritol, and maltitol)';
UPDATE ag.survey_response SET japanese = '手術' WHERE american = 'Surgery';
UPDATE ag.survey_response SET japanese = '水道水' WHERE american = 'Tap water';
UPDATE ag.survey_response SET japanese = '標的（薬物）療法' WHERE american = 'Targeted (medication) therapy';
UPDATE ag.survey_response SET japanese = '精巣胚細胞性がん' WHERE american = 'Testicular germ cell cancer';
UPDATE ag.survey_response SET japanese = '甲状腺がん' WHERE american = 'Thyroid cancer';
UPDATE ag.survey_response SET japanese = '町（人口1,000人超、10万人未満）' WHERE american = 'Town (population is more than 1,000 and less than 100,000)';
UPDATE ag.survey_response SET japanese = '潰瘍性大腸炎' WHERE american = 'Ulcerative Colitis';
UPDATE ag.survey_response SET japanese = '子宮がん' WHERE american = 'Uterine cancer';
UPDATE ag.survey_response SET japanese = 'ぶどう膜メラノーマ' WHERE american = 'Uveal melanoma';
UPDATE ag.survey_response SET japanese = '激しい' WHERE american = 'Vigorous';
UPDATE ag.survey_response SET japanese = '職業訓練' WHERE american = 'Vocational training';
UPDATE ag.survey_response SET japanese = '毎週' WHERE american = 'Weekly';
UPDATE ag.survey_response SET japanese = '井戸水' WHERE american = 'Well water';
UPDATE ag.survey_response SET japanese = '小麦デキストリン（例： Benefiber ）' WHERE american = 'Wheat dextrin (e.g. Benefiber)';
UPDATE ag.survey_response SET japanese = '過去10年以内' WHERE american = 'Within the last 10 years';
UPDATE ag.survey_response SET japanese = '過去5年以内' WHERE american = 'Within the last 5 years';
UPDATE ag.survey_response SET japanese = '過去1年以内' WHERE american = 'Within the last year';
UPDATE ag.survey_response SET japanese = 'はい、現在がんを患っています。' WHERE american = 'Yes, I currently have cancer';
UPDATE ag.survey_response SET japanese = 'はい、ホメオパシー薬を服用しています。' WHERE american = 'Yes, I take homeopathic medication';
UPDATE ag.survey_response SET japanese = 'はい、市販薬を服用しています。' WHERE american = 'Yes, I take over-the-counter medication';
UPDATE ag.survey_response SET japanese = 'はい、処方薬を服用しています。' WHERE american = 'Yes, I take prescription medication';
UPDATE ag.survey_response SET japanese = 'はい、避妊用パッチを使用しています。' WHERE american = 'Yes, I use a contraceptive patch';
UPDATE ag.survey_response SET japanese = 'はい、避妊用の膣リングを使用しています。' WHERE american = 'Yes, I use a contraceptive vaginal ring';
UPDATE ag.survey_response SET japanese = 'はい、ホルモン子宮内避妊具／インプラントを使用しています。' WHERE american = 'Yes, I use a hormonal IUD/implant';
UPDATE ag.survey_response SET japanese = 'はい、注射用避妊薬を使用しています。' WHERE american = 'Yes, I use an injected contraceptive';
UPDATE ag.survey_response SET japanese = 'はい、ここに記載されていない他の種類の薬を使用しています。' WHERE american = 'Yes, I use other types of medication not listed here';
UPDATE ag.survey_response SET japanese = 'はい、医療専門家（医師、医師助手）によって診断されました。' WHERE american = 'Yes, diagnosed by a medical professional (doctor, physician assistant)';
UPDATE ag.survey_response SET japanese = 'はい、代替医療の医師によって診断されました。' WHERE american = 'Yes, diagnosed by an alternative or complementary practitioner';
UPDATE ag.survey_response SET japanese = '両方とも同じくらい' WHERE american = 'Both equally';
UPDATE ag.survey_response SET japanese = '都市（人口10万人超、100万人未満）' WHERE american = 'City (population is more than 100,000 and less than 1 million)';
UPDATE ag.survey_response SET japanese = '2021' WHERE american = '2021';
UPDATE ag.survey_response SET japanese = '2022' WHERE american = '2022';
UPDATE ag.survey_response SET japanese = 'わからない' WHERE american = 'Don''t know';
UPDATE ag.survey_response SET japanese = 'はい、認可されたメンタルヘルスの専門家によって診断されました' WHERE american = 'Yes, diagnosed by a licensed mental health professional';
UPDATE ag.survey_response SET japanese = 'N/A' WHERE american = 'N/A';
UPDATE ag.survey_response SET japanese = '息切れや呼吸困難' WHERE american = 'Shortness of breath or difficulty breathing';
UPDATE ag.survey_response SET japanese = '頭痛' WHERE american = 'Headaches';
UPDATE ag.survey_response SET japanese = '筋肉痛' WHERE american = 'Muscle aches';
UPDATE ag.survey_response SET japanese = '鼻水または鼻詰まり' WHERE american = 'Runny or stuffy nose';
UPDATE ag.survey_response SET japanese = '喘鳴(ゼーゼーとした咳）' WHERE american = 'Wheezing';
UPDATE ag.survey_response SET japanese = '3回以上' WHERE american = '3 or more';
UPDATE ag.survey_response SET japanese = '両方使います' WHERE american = 'I use both';
UPDATE ag.survey_response SET japanese = '発酵食品は作りません。' WHERE american = 'I do not produce fermented foods';
UPDATE ag.survey_response SET japanese = 'いいえ。私は子宮内避妊具銅IUDを使用しています' WHERE american = 'No, I use a copper IUD';

-- Load Japanese consent documents
-- Critical to note that we only have adult data/biospecimen documents, so Japanese users may not create profiles for minors
INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_data', 'ja_JP', NOW(), '<p class="consent_title">
	<strong>University of California San Diego (カリフォルニア大学サンディエゴ校)</strong><br />
	研究被験者として行動する同意書
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
	この研究への参加は完全に自由意志によるものであり、参加を拒否することもできます。どの質問を飛ばして回答してもかまいません。参加の意思に影響を及ぼす可能性のある重要な新しい情報がこの研究中に見つかった場合はお知らせします。
</p>
<p class="consent_content">
	参加者はいつでも参加を拒否または撤回する権利があり、処罰を課されたり、ご自身の利益を失う事はありません。もう研究参加を続けたくない場合は、オンラインアカウントを通して、ご自分のプロファイルおよび／またはアカウントの削除を要請することで、同意を取り下げることができます。ただし、当研究所の研究者は、あなたが参加を辞退する前に収集されたデータを引き続き使用する場合があります。これらのデータには、あなたを直接特定できるような個人情報は含まれません。あなたが参加を辞退した後に、新たなデータが収集されることはありません。
</p>
<p class="consent_content">
	研究担当者の指示に従わない場合、研究参加を取り消される可能性があります。
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
	提供していただく個人データは、次の目的に使用されます：<br />
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
	電話：+1) 858-822-2379<br />
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
</p>', TRUE, '000fc4cd-8fa4-db8b-e050-8a800c5d81b7');
INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_biospecimen', 'ja_JP', NOW(), '<p class="consent_title">
	<strong>University of California San Diego (カリフォルニア大学サンディエゴ校)</strong><br />
	研究被験者として行動することへの同意書
</p>
<p class="consent_title">
	<strong>Microsetta Initiative（マイクロセッタ・イニシアチブ）</strong><br />
	生物学的標本と将来の研究への使用
</p>
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
	この研究への参加者のプライバシーは保護されます。個人情報の保護のため万全のシステムを導入し情報漏洩を防止します。​しかしながら、現時点では予測できない事象による参加者の個人情報漏洩のリスクなど、いくつかの付加的なリスクを伴う可能性はあります。
</p>
<p class="consent_content">
	本調査は研究であるため、現時点では予測できない未知のリスクが存在する可能性があります。
</p>
<p class="consent_content">
	重要な新知見が得られた場合は、お知らせします。
</p>
<p class="consent_header">
	研究に参加する意思がなくなったとき、もしくは、参加資格を失う場合の規定
</p>
<p class="consent_content">
	この研究への参加は完全に自由意志によるものであり、参加を拒否することもできます。参加の意思に影響を及ぼす可能性のある重要な新しい情報がこの研究中に見つかった場合はお知らせします。参加者はいつでも参加を拒否または撤回する権利があり、処罰を課されたり、ご自身の利益を失う事はありません。
</p>
<p class="consent_content">
	もう研究参加を続けたくない場合は、オンラインアカウントを通して、ご自分のプロファイルおよび／またはアカウントの削除を要請することで、同意を取り下げることができます。ただし、当研究所の研究者は、あなたが参加を辞退する前に収集されたデータを引き続き使用する場合があります。これらのデータには、あなたを直接特定できるような個人情報は含まれません。あなたが参加を辞退した後に、新たなデータが収集されることはありません。
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
	研究記録は、個人情報の保護に関する米国の法律の下で秘匿されます。研究参加の一環として、研究参加者は個人情報を提供します。その情報とは、氏名、生年月日、住所など、公表されると研究参加者の身元を特定できるものです。研究参加者のプライバシー保護の為、本プロジェクトは細心の注意を払います。提供していただく全データは、米国サンディエゴUC San Diegoにある安全なシステムに保管され、限定された研究職員のみが直接身元が識別できる情報へアクセスを許可されています。参加者の個人情報とサンプル情報を保有したデータベースは、パスワードで保護されたサーバー上で運用され、Knight博士、共同研究者、プロジェクトおよびサンプルコーディネーター、IT管理者、データベースコーダー等の関連スタッフのみがアクセス可能です。データベースサーバーへは、UC San Diego(カリフォルニア大学サンディエゴ校)が管理するシステムからのネットワーク接続のみ許可しています。データベースサーバーはパスワード保護、ファイアウォールを使用、アクセス制御リストを使用し、高度かつ厳重にセキュリティ対策を施し、キーカード制御のUC San Diego(カリフォルニア大学サンディエゴ校)の施設内で保管しています。データベースのバックアップは夜間に実施し、同施設内の追加セキュリティ対策を施した別システムで管理されています。サンプルの解析は、直接身元を識別できる情報を取り除いたデータを使って実施され、公的保管機関で共有される全データもこの処理を行います。
</p>
<p class="consent_content">
	研究記録は、UC San DiegoのIRB（施設内審査委員会）によって審査される場合があります。
</p>
<p class="content_header">
	研究参加者のサンプルが使用される方法
</p>
<p class="consent_content">
	研究参加者のデータと生物学的標本の解析から得られる情報は ヒト以外のDNA（例：細菌のDNA）が研究に使用されます。本プロジェクトのサンプルから取得したデータ（研究参加者のものを含む）は、科学論文に発表される可能性があります。
</p>
<p class="consent_content">
	一部のサンプルは、RNA、タンパク質、または代謝物などの他の化合物を使う追加研究を行う研究者が使用するために保持される場合があります。 その場合は、使用または共有前に、身元を識別できる全情報を取り除きます。
</p>
<p class="consent_content">
	身元識別情報を取り除いた後は、今後の研究で研究参加者のデータ、サンプルの使用または共有について、都度同意を求めることはありません。加えて、身元識別情報を取り除いたデータは、欧州バイオインフォマティクス研究所（http://www.ebi.ac.uk）およびQiita （https://qiita.ucsd.edu）などにアップロードされ、他の研究者のアクセスと使用を可能とします。将来研究参加者のサンプルを処理する為に追加情報または何らかの措置が必要となった場合には再度同意のお願いの連絡をする場合があります。
</p>
<p class="consent_content">
	この研究で参加者から採取される生物学的標本とその情報は、この研究または他の研究に使用され、他の組織と共有される場合があります。この生物学的標本とその情報の使用により得られた商業的価値や利益は参加者に共有されません。
</p>
<p class="consent_header">
	注記：
</p>
<p class="consent_content">
	この研究または将来の研究の一環として、 ヒトDNAは分析されることはありません。さらに、サンプルの中の微生物の特定に使われる解析手法は<strong>病気や感染症の診断には使用しません</strong>。
</p>
<p class="consent_header">
	お問い合わせ先
</p>
<p class="consent_content">
	ご質問または研究関連の問題がある場合はRob Knight博士に電話するか、ヘルプアカウントにメールをお送りください。
</p>
<p class="consent_content">
	電話：+1) 858-822-2379<br />
	メール:  microsetta@ucsd.edu
</p>
<p class="consent_content">
	研究対象者としての権利に関するお問い合わせや、研究関連の問題を報告する場合は、UC San Diego(カリフォルニア大学サンディエゴ校)のIRB管理室（+1 858-246-4777）または電子メール（irb@ucsd.edu）にご連絡ください。
</p>
<p class="consent_header">
	署名と同意
</p>
<p class="consent_content">
	この同意文書のコピーおよび「<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">調査対象の権利章典</a>」のコピーを保管のためにダウンロードすることができます。
</p>
<p class="consent_content">
	同意は完全に自由意志によるものですが、同意を拒否される場合、この研究への参加およびサンプルの処理ができなくなる可能性があります。
</p>', TRUE,'000fc4cd-8fa4-db8b-e050-8a800c5d81b7');
