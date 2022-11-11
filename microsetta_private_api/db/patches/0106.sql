CREATE TABLE ag.consent_documents (
    consent_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    consent_type varchar(50) NOT NULL,
    locale varchar(10) NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    consent_content varchar NOT NULL,
    reconsent_required boolean NOT NULL,
    account_id uuid NOT NULL,
    PRIMARY KEY (consent_id)
);
CREATE TABLE ag.consent_audit (
    signature_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    parent_1_name varchar(200),
    parent_2_name varchar(200),
    deceased_parent boolean,
    assent_obtainer varchar(200),
    consent_id uuid NOT NULL,
    source_id uuid NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (signature_id),
    FOREIGN KEY (consent_id) REFERENCES ag.consent_documents (consent_id),
    FOREIGN KEY (source_id) REFERENCES ag.source (id)
);

INSERT INTO ag.account 
    ("id", "email", "account_type", "first_name", "last_name",
     "street", "city", "post_code", "country_code", "preferred_language",
     "address_verified", "cannot_geocode")
     VALUES ('000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 'microsetta+consentdummy@ucsd.edu', 'standard', 'demo', 'demo', 'demo', 'demo', '46839', 'US', 'en_US', 'false', 'false');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_biospecimen', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
  (Ages 13-17 years)
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong><br />
  Biospecimen and Future Use Research
</p>
<p class="consent_header">
  Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight from the University of California - San Diego (UCSD is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. You have been asked to participate in this study because you, and everyone else on earth, have a unique microbiome, and the more people we study of all ages, the more we will understand about how the microorganisms may help or harm us. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done?
</p>
<p class="consent_content">
  The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your information and biospecimens for the purpose of processing your biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What will happen to you in this study and which procedures are standard of care and which are experimental?
</p>
<p class="consent_content">
  If you agree to participate in this study, the following will happen to you:
</p>
<p class="consent_content">
  You will sample yourself using the kit that was provided to you.  Instructions are included in the kit so you know what to do.  The most common sample is of your poop (stool) where you apply a small smear to the tips of a swab from used toilet tissue or to a card (called an FOBT card). You may also be asked to scoop some poop using a small spoon-like tool, place used toilet paper into a special receptacle we provide, or poop into a plastic container that you place under the toilet seat. You may also need to sample a small area of skin, your tongue or mouth, your nostrils, ear wax, or vagina.  We may also ask someone (like your mom or dad) to take a small sample of blood by pricking your finger and then collecting the blood on 2 small swabs. None of these samples or investigations will allow us to make a diagnosis of disease and we are not looking at anything in your own DNA that can also be found in your poop, skin, or saliva.
</p>
<p class="consent_header">
  How much time will each study procedure take, what is your total time commitment, and how long will the study last?
</p>
<p class="consent_content">
  Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years, but your results will be available to you before the end of the study.
</p>
<p class="consent_header">
  What risks are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added risks or discomforts. These include the following:
  <ol>
    <li>You may experience temporary pain or a bruise at the site of the needle-stick if you take the blood test.</li>
    <li>There is a risk of loss of confidentiality. </li>
  </ol>
  Because this is a research study, there may be some unknown risks that are currently unforeseeable. You and your parents will be informed of any significant new findings.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
  You do not have to participate. Your participation in this study is completely voluntary and you can refuse to participate or withdraw at any time by withdrawing your consent and deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no direct benefit to you for participating in this study. You will get access to your data that will give you and your parents an idea of what is in your sample and how it compares with other people like you (age, sex).
</p>
<p class="consent_header">
  Will you be compensated for participating in this study?
</p>
<p class="consent_content">
  You will not be financially compensated in this study.
</p>
<p class="consent_header">
  Are there any costs associated with participating in the collection of your biospecimen(s)
</p>
<p class="consent_content">
  There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure.
</p>
<p class="consent_header">
  What if you are injured as a direct result of being in this study?
</p>
<p class="consent_content">
  If you are injured or become ill as a direct result of this research study, you will be provided with medical care.
</p>
<p class="consent_header">
  What about your confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law.  As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  How we will use your Sample
</p>
<p class="consent_content">
  Information from analyses of your data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or sample(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
  Biospecimens (such as stool, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
  <strong><u>Please Note:</u></strong><br />
  Please be aware that <strong>no human DNA</strong> will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample <strong>cannot be used to diagnose disease or infection</strong>.
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach us by emailing our help account microsetta@ucsd.edu or Rob Knight at 858-246-1184.
</p>
<p class="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_data', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject
  (Ages 13-17 years)
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
  Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight from the University of California - San Diego (UCSD) is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. You have been asked to participate in this study because you, and everyone else on earth, have a unique microbiome, and the more people we study of all ages, the more we will understand about how the microorganisms may help or harm us. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done and what will happen to you?
</p>
<p class="consent_content">
  The purpose of this research study is to assess more accurately the differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. If you agree to take part in this study, you will be asked to complete online surveys/questionnaires. This survey/questionnaire will ask questions about you, such as your age, weight, height, lifestyle, diet, and  if you have certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no monetary or direct benefit for participating in this study. If you complete one of the questionnaires called the Food Frequency Questionnaire (FFQ), you may receive a nutritional report evaluating your eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What risks and confidentiality are associated with this study?
</p>
<p class="consent_content">
  Participation in this study can involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
  Your participation in this study is completely voluntary and you can refuse to participate or withdraw at any time by simply exiting the survey or withdrawing your consent and deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you. You are free to skip any question that you choose.
</p>
<p class="consent_header">
  Know what we will collect
</p>
<p class="consent_content">
  As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
  How we will use your Personal Data
</p>
<p class="consent_content">
  The Personal Data you provide will be used for the following purposes:
  <ul>
    <li>To share with members of the research team so they can properly conduct the research.</li>
    <li>For future research studies or additional research by other researchers.</li>
    <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
    <li>To confirm proper conduct of the study and research integrity.</li>
  </ul>
</p>
<p class="consent_header">
  Retention of your Personal Data
</p>
<p class="consent_content">
  We may retain your Personal Data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements.
</p>
<p class="consent_header">
  Your Privacy Rights
</p>
<p class="consent_content">
  The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information.
</p>
<p class="consent_content">
  The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Study Data. Additional information about the protections we will use is included in this consent document.
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
  If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Your Signature and Consent
</p>
<p class="consent_content">
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_biospecimen', 'en_US', NOW(), '<p class="content_title">
  <strong>University of California, San Diego</strong><br />
  Consent to Act as a Research Subject
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong>
  Biospecimen and Future Use Research
</p>
<p class="consent_header">
  Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called your microbiome) that live in and on your body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You have been asked to participate in this study because your microbiome is unique - not the same as anyone else"s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done?
</p>
<p class="consent_content">
  The purpose of this study is to assess more accurately the microbial differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your information and biospecimens for the purpose of processing your biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites,, as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What will happen to you in this study?
</p>
<p class="consent_content">
  If you agree to the collection and processing of your biospecimen(s), the following will happen to you:
</p>
<p class="consent_content">
  You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.  You will then collect a sample of yourself (e.g. feces, skin, mouth, nostril, ear, vagina), pet, or environment as described in the kit instructions or in the instructions provided to you by study coordinators. You will also be asked to provide general collection information such as the date and time your sample was collected. All samples should be returned to us in the included containers according to the instructions provided.
</p>
<p class="consent_content">
  If collecting from stool, you will be asked to sample in one of a variety of ways, such as the following:
  <ol>
    <li>By inserting swab tip(s) into used toilet tissue and returning the swab(s) in the provided plastic container;</li>
    <li>By inserting swab tip(s) into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
    <li>By using a scooper device to scoop a part of the fecal material into the provided tube;</li>
    <li>Depositing soiled toilet paper into the provided receptacle;</li>
    <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celsius/-4 degrees Fahrenheit.</li>
  </ol>
</p>
<p class="consent_content">
  If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your finger.
</p>
<p class="consent_content">
  Once your sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them.  We estimate that it can take 1-3 months for you to learn the results of your microbiome analysis. If you are a part of a specific sub-study, it  may take longer, depending on the duration of the study.
</p>
<p class="consent_header">
  How much time will each study procedure take, what is your total time commitment, and how long will the study last?
</p>
<p class="consent_content">
  Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but your results will be available to you before the end of the study.
</p>
<p class="consent_header">
  What risks are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added risks or discomforts. These include the following:
  <ol>
    <li>If using the blood collection device, you may experience temporary pain or a bruise at the site of the needle-stick.</li>
    <li>There is a risk of loss of confidentiality. </li>
  </ol>
</p>
<p class="consent_content">
  Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
  You do not have to participate. Your participation in this study is completely voluntary and you may refuse to participate or withdraw at any time without penalty or loss of benefits to which you are entitled. If you decide that you no longer wish to continue in this study, you may withdraw your consent by requesting the deletion of your profile and/or account through your online account. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no monetary or direct benefit for participating in this study. You will receive a report detailing the results of our analysis on your biospecimen(s), as well as facts and figures comparing your microbiome"s composition to that of other study participants.
</p>
<p class="consent_header">
  Are there any costs associated with participating in the collection of your biospecimen(s)?
</p>
<p class="consent_content">
  There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure.
</p>
<p class="consent_header">
  What if you are injured as a direct result of being in this study?
</p>
<p class="consent_content">
  If you are injured as a direct result of participation in this research, the University of California will provide any medical care you need to treat those injuries. The University will not provide any other form of compensation to you if you are injured. You may call the Office of IRB Administration at (858) 246-4777 for more information about this, to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
  What about your confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law. As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  How we will use your Sample
</p>
<p class="consent_content">
  Information from analyses of your data and biospecimen(s) will be used  to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use.We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
  Biospecimens (such as stool, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
  <strong><u>Please Note:</u></strong><br />
  Please be aware that <strong>no human DNA</strong> will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample <strong>cannot be used to diagnose disease or infection</strong>.
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
  Your Signature and Consent
</p>
<p class="consent_content">
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research and have your sample(s) processed.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_data', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
  Consent to Act as a Research Subject</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
  Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  You are being invited to participate in a research study titled The Microsetta Initiative. This study is being done by Dr. Rob Knight from the University of California - San Diego (UCSD). You were selected to participate in this study because you are unique and your microbiome is unique - not the same as anyone else"s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done and what will happen to you?
</p>
<p class="consent_content">
  The purpose of this research study is to assess more accurately the microbial differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. If you agree to take part in this study, you will be asked to complete online surveys/questionnaires. These surveys/questionnaires are categorized by content type and will ask questions about you, such as your age, weight, height, lifestyle, diet, and if you have certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no monetary or direct benefit for participating in this study. If you complete one of the questionnaires, called a Food Frequency Questionnaire (FFQ), you may receive a nutritional report evaluating your eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What risks and confidentiality are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_content">
  We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, they may report such information to the appropriate authorities.
</p>
<p class="consent_content">
  Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.
</p>
<p class="consent_content">
  Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.
</p>
<p class="consent_header">
  What if you are injured as a direct result of being in this study?
</p>
<p class="consent_content">
  If you are injured as a direct result of participation in this research, the University of California will provide any medical care you need to treat those injuries. The University will not provide any other form of compensation to you if you are injured. You may call the Office of IRB Administration at (858) 246-4777 for more information about this, to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
  Your participation in this study is completely voluntary and you can withdraw at any time by simply exiting the survey, withdrawing your consent, or by requesting the deletion of your account through your online account. You are free to skip any question that you choose.
</p>
<p class="consent_header">
  Will you be compensated for participating in this study?
</p>
<p class="consent_content">
  You will not be financially compensated in this study.
</p>
<p class="consent_header">
  Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
  There will be no cost to you for completing the standard survey/questionnaire(s). However, there may be costs associated with having certain diet assessment tools made available to you, such as the Food Frequency Questionnaire (FFQ).
</p>
<p class="consent_header">
  Know what we will collect
</p>
<p class="consent_content">
  As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
  How we will use your Personal Data
</p>
<p class="consent_content">
  The Personal Data you provide will be used for the following purposes:
  <ul>
    <li>To share with members of the research team so they can properly conduct the research.</li>
    <li>For future research studies or additional research by other researchers.</li>
    <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
    <li>To confirm proper conduct of the study and research integrity.</li>
  </ul>
</p>
<p class="consent_header">
  Retention of your Personal Data
</p>
<p class="consent_content">
  We may retain your Personal Data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements.
</p>
<p class="consent_header">
  Your Privacy Rights
</p>
<p class="consent_content">
  The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information.
</p>
<p class="consent_content">
  The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Study Data. Additional information about the protections we will use is included in this consent document.
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p clsas="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
  If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Your Signature and Consent
</p>
<p class="consent_content">
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_biospecimen', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
  (Ages 7-12 years)
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (a study about microbes)</strong>
</p>
<p class="consent_content">
  Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of  tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something (like the virus that causes COVID-19) but we can"t tell you that because we are not allowed to do that.
</p>
<p class="consent_content">
  If you decide you want to be in this research study, this is what will happen to you:
</p>
<p class="consent_content">
  We will ask you or your mom or dad to sample some place on your body (like skin or mouth) or your poop (from toilet paper) with something that looks like 2 Q-tips.  Sometimes we need more poop for our research and then we will ask you to poop into a plastic bowl that is under the seat of the toilet and catches the poop as it comes out.  Your mom or dad will send it to us in the bowl. We may also ask your mom or dad to prick your finger so that we can get a little bit of your blood.
</p>
<p class="consent_content">
  Sometimes kids don"t feel good while being in this study. You might feel a little bit sore if your skin is rubbed with the Q-tip and temporary pain if they prick your finger to get blood. Most people don"t mind these feelings.
</p>
<p class="consent_content">
  If you feel any of these things, or other things, be sure to tell your mom or dad.
</p>
<p class="consent_content">
  You don"t have to be in this research study if you don"t want to. Nobody will be mad at you if you say no. Even if you say yes now and change your mind after you start doing this study, you can stop and no one will be mad.
</p>
<p class="consent_content">
  Be sure to ask your parents if you have questions.  You can also ask them to call Dr. Knight or his research team so they can tell you more about anything you don"t understand.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_data', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
  (Ages 7-12 years)
</p>
<p class="consent_title">
  The Microsetta Initiative (a study about microbes)
</p>
<p class="consent_content">
  Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something (like the virus that causes COVID-19) but we can"t tell you that because we are not allowed to do that.
</p>
<p class="consent_content">
  If you decide you want to be in this research study, this is what will happen to you:
</p>
<p class="consent_content">
  We will ask you to answer survey questions about you, like your age, weight, height, your lifestyle, what you eat, if you have taken antibiotics, if you have certain diseases and if you take supplements like vitamins.  There are also other surveys that you can choose to complete if you want to.
</p>
<p class="consent_content">
  Your answers will be kept private. We will not share any information about whether or not you took part in this study.
</p>
<p class="consent_content">
  Sometimes kids don"t feel good while being in this study. You might feel a little tired, bored, or uncomfortable. Most people don"t mind these feelings.
</p>
<p class="consent_content">
  If you feel any of these things, or other things, be sure to tell your mom or dad.
</p>
<p class="consent_content">
  You don"t have to be in this research study if you don"t want to. Nobody will be mad at you if you say no. Even if you say yes now and change your mind after you start doing this study, you can stop and no one will be mad.
</p>
<p class="consent_content">
  Be sure to ask your parents if you have questions.  You can also ask them to call Dr. Knight or his research team so they can tell you more about anything you don"t understand.
</p>', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_biospecimen', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Parent Consent for Child to Act as a Research Subject
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong><br />
  Biospecimen and Future Use Research
</p>
<p class="consent_header">
  Who is conducting the study, why has your child been asked to participate, how was your child selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called the microbiome) that live in and on the body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You are volunteering your child for this study because you want to know more about the microbiome of your child. Children like all humans have a unique microbiome and including them in the study will help elucidate the development of the microbiome. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done?
</p>
<p class="consent_content">
  The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your child"s information and biospecimens for the purpose of processing your child"s biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about the child participant supplying the sample. Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What will happen to your child in this study?
</p>
<p class="consent_content">
  If you agree to the collection and processing of your child"s biospecimen(s), the following will happen to your child:
</p>
<p class="consent_content">
  You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.
</p>
<p class="consent_content">
  You will sample a part of your child"s body (e.g. feces, skin, mouth, nostril, ear, vagina) as described in the kit instructions. You will also be asked to provide general collection information such as the date and time your child"s sample was collected. All samples should be returned to us in the included containers according to the instructions provided.
</p>
<p class="consent_content">
  If collecting from your child"s stool, you will be asked to sample in one of a variety of ways, such as the following:
  <ol>
    <li>By inserting swab tips into used toilet tissue or diaper and returning the sample in the provided plastic container;</li>
    <li>By inserting swab tips into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
    <li>By using a scooper device to scoop a part of the fecal material into the provided tube;</li>
    <li>Depositing soiled toilet paper into the provided receptacle;</li>
    <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celcius/-4 degrees Fahrenheit.</li>
  </ol>
</p>
<p class="consent_content">
  If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your child"s finger.
</p>
<p class="consent_content">
  Once your child"s sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them. We estimate that it can take 1-3 months for you to learn the results of your child"s microbiome analysis. If your child is a part of a specific sub-study, it may take longer, depending on the duration of the study.
</p>
<p class="consent_header">
  How much time will each study procedure take, what is your child"s total time commitment, and how long will the study last?
</p>
<p class="consent_content">
  Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but the results will be available to you before the end of the study.
</p>
<p class="consent_header">
  What risks are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added risks or discomforts. These include the following:
  <ol>
    <li>If using the blood collection device, your child may experience temporary pain or a bruise at the site of the needle-stick.</li>
    <li>There is a risk of loss of confidentiality.</li>
  </ol>
</p>
<p class="consent_content">
  Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study? Can your child withdraw or be withdrawn from the study?
</p>
<p class="consent_consent">
  Participation in research is entirely voluntary. You may refuse to have your child participate or withdraw your child at any time without penalty or loss of benefits to which you or your child are entitled. If you decide that you no longer wish your child to continue in this study, you may withdraw your consent by requesting the deletion of your child"s profile through your online account. We will inform you and your child if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  Your child may be withdrawn from the study if the instructions given to you by the study personnel are not followed.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no direct benefit to your child for participating in this study. You will receive a report detailing the results of our analysis on your child"s sample, as well as facts and figures comparing your child"s microbial composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
</p>
<p class="consent_header">
  Will you be compensated for participating in this study?
</p>
<p class="consent_content">
  You will not be financially compensated in this study.
</p>
<p class="consent_header">
  Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
  There may be costs associated with obtaining a kit but there will be no cost for participating in the sampling procedure.
</p>
<p class="consent_header">
  What if your child is injured as a direct result of being in this study?
</p>
<p class="consent_content">
  If your child is injured as a direct result of participation in this research, the University of California will provide any medical care you need to treat those injuries. The University will not provide any other form of compensation to you if your child is injured. You or your child may call the Office of IRB Administration at 858-246-4777 for more information about this, to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
  What about your or your child"s confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law. As part of your child"s participation in the study, you or your child will provide personal and/or sensitive information that could allow your child to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you or your child provide are stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  How we will use your child"s Sample
</p>
<p class="consent_content">
  Information from analyses of your child"s data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including your child"s) may be analyzed and published in scientific articles. We may save some of your child"s sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your child"s data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your child"s sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
  Biospecimens (such as stool, skin, urine, or blood) collected from your child for this study and information obtained from your child"s biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your child"s biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
  <strong><u>Please Note:</u></strong><br />
  Please be aware that <strong>no human DNA</strong> will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample <strong>cannot be used to diagnose disease or infection</strong>.
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
  Your Signature and Consent
</p>
<p class="consent_content">
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your child"s ability to participate in this research and have your child"s sample(s) processed.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');


INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_data', 'en_US', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Parent Consent for Child to Act as a Research Subject
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
  Who is conducting the study, why has your child been asked to participate, how was your child selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called the microbiome) that live in and on the body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You are volunteering your child for this study because you want to know more about the microbiome of your child. Children like all humans have a unique microbiome and including them in the study will help elucidate the development of the microbiome. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
  Why is this study being done and what will happen to your child?
</p>
<p class="consent_content">
  The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. If you agree to allow your child to take part in this study, we will ask you to complete online surveys/questionnaires about your child such as their age, weight, height, lifestyle, diet, and if your child has certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no direct benefit to your child for participating in this study.  If you complete one of the questionnaires called Food Frequency Questionnaire (FFQ) for your child, you may receive a nutritional report evaluating your child"s eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What risks are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you or your child may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you or your child provide is stored on secure systems within UC San Diego"s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_content">
  We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, they may report such information to the appropriate authorities.
</p>
<p class="consent_content">
  Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.
</p>
<p class="consent_content">
  Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.
</p>
<p class="consent_header">
  What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
  Participation in this study is completely voluntary and you or your child can withdraw at any time by simply exiting the survey, withdrawing consent and deleting your child"s online profile, or by requesting the deletion of your online account. You are free to skip any question that you choose.
</p>
<p class="consent_header">
  Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
  There will be no cost to you or your child for completing the standard survey/questionnaire(s). However, there may be costs associated with having certain diet assessment tools made available to your child, such as the Food Frequency Questionnaire (FFQ).
</p>
<p class="consent_header">
  Know what we will collect
</p>
<p class="consent_content">
  As part of this research study, we will create and obtain information related to you or your child"s participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
  How we will use your child"s Personal Data
</p>
<p class="consent_content">
  The Personal Data you provide will be used for the following purposes:
  <ul>
    <li>To share with members of the research team so they can properly conduct the research.</li>
    <li>For future research studies or additional research by other researchers.</li>
    <li>To contact you for the purpose of receiving alerts of your child"s participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
    <li>To confirm proper conduct of the study and research integrity.</li>
  </ul>
</p>
<p class="consent_header">
  Retention of your child"s Personal Data
</p>
<p class="consent_content">
  We may retain the Personal Data you provide for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your child"s Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your child"s information will be retained as necessary to comply with legal or regulatory requirements.
</p>
<p class="consent_header">
  Your Privacy Rights
</p>
<p class="consent_content">
  The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your child"s Personal Data, including the right to access, correct, restrict, and withdraw your child"s personal information.
</p>
<p class="consent_content">
  The research team will store and process your child"s Personal Data at our research site in the United States. The United States does not have the same laws to protect your child"s Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your child"s Study Data. Additional information about the protections we will use is included in this consent document. 
</p>
<p class="consent_header">
  Who can you call if you have questions?
</p>
<p class="consent_content">
  If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
  If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Your Signature and Consent
</p>
<p class="consent_content">
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your child"s ability to participate in this research.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');


INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 13-17 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespec�menes e investigaci�n de uso futuro</strong>
</p>
<p class="consent_header">
  �Qui�n realiza el estudio, por qu� se le ha pedido que participe, c�mo fue seleccionado y cu�l es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) est� realizando un estudio de investigaci�n para obtener m�s informaci�n sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los dem�s en la tierra, tienen un microbioma �nico, y cuantas m�s personas estudiemos de todas las edades, m�s entenderemos acerca de c�mo los microorganismos pueden ayudarnos o da�arnos. Habr� aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros pa�ses alrededor del mundo.
</p>
<p class="consent_header">
  �Por qu� se est� llevando a cabo este estudio?
</p>
<p class="consent_content">
  El prop�sito de este estudio es evaluar con mayor precisi�n las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constituci�n corporal, la edad o la presencia de enfermedades asociadas. Las muestras biol�gicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigaci�n. Este estudio implica la recopilaci�n, el almacenamiento y el uso de su informaci�n y muestras biol�gicas con el fin de procesar sus muestras biol�gicas y para futuras investigaciones. Los resultados se utilizar�n para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, as� como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podr�n usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  �Qu� le suceder� en este estudio y qu� procedimientos son el est�ndar de atenci�n y cu�les son experimentales?
</p>
<p class="consent_content">
  Si usted acepta participar en este estudio, le ocurrir� lo siguiente:
</p>
<p class="consent_content">
  Usted mismo tomar� la muestra usando el kit que se le proporcion�. Las instrucciones est�n incluidas en el kit para que sepa qu� hacer. La muestra m�s com�n es de heces (fecal) donde se recoge una peque�a muestra insertando las puntas de un hisopo en el papel higi�nico usado o en una tarjeta (tarjeta llamada FOBT). Tambi�n se le puede pedir que saque un trozo de materia fecal con una peque�a herramienta similar a una cuchara, que coloque papel higi�nico usado en un recept�culo especial que le proporcionaremos o que defeque en un recipiente de pl�stico que se coloca debajo del asiento del ba�o. Tambi�n es posible que deba tomar muestras de una peque�a �rea de la piel, la lengua o la boca, las fosas nasales, la cera del o�do o la vagina. Tambi�n podemos pedirle a alguien (como su mam� o pap�) que tome una peque�a muestra de sangre pinchando su dedo y luego recolectando la sangre en 2 hisopos peque�os. Ninguna de estas muestras o investigaciones nos permitir� hacer un diagn�stico de enfermedad y no estamos buscando nada en su propio ADN que tambi�n se pueda encontrar en sus heces, piel o saliva.
</p>
<p class="consent_header">
  �Cu�nto tiempo es necesario para realizar cada procedimiento del estudio, cu�nto tiempo debe dedicar en total y cu�nto durar� el estudio?
</p>
<p class="consent_content">
  Cada muestra que env�e se puede obtener en 5 minutos o menos. Esperamos que el estudio contin�e durante muchos a�os, pero sus resultados estar�n disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  �Cu�les son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participaci�n en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el an�lisis de sangre.</li>
    <li>Existe el riesgo de p�rdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigaci�n, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres ser�n informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  �Cu�les son las alternativas a participar en este estudio? �Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participaci�n en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en l�nea. Nuestros investigadores seguir�n utilizando los datos sobre usted que se recopilaron antes de que se retirara. Despu�s de retirarse, no se recopilar�n m�s datos sobre usted. Le informaremos si se encuentra nueva informaci�n importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  �Cu�les podr�an ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ning�n beneficio directo para usted por participar en este estudio. Usted tendr� acceso a sus datos que le dar�n a usted y a sus padres una idea de lo que hay en su muestra y c�mo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
  �Se le pagar� por participar en este estudio?
</p>
<p class="consent_content">
  Usted  no recibir� ninguna remuneraci�n econ�mica por participar en este estudio.
</p>
<p class="consent_header">
  �Hay alg�n costo vinculado con la participaci�n en la colecci�n de su(s) muestra(s) biol�gica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtenci�n de un kit. Una vez que reciba su kit, no habr� ning�n costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  �Qu� sucede si sufre una lesi�n como consecuencia directa del estudio?
</p>
<p class="consent_content">
  Si usted se lesiona o se enferma como resultado directo de este estudio de investigaci�n, se le brindar� atenci�n m�dica.
</p>
<p class="consent_header">
  �Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigaci�n se mantendr�n confidenciales en la medida permitida por la ley. Como parte de su participaci�n en el estudio, usted proporcionar� informaci�n personal y/o confidencial que podr�a permitir su identificaci�n si se hiciera p�blica, como nombre, fecha de nacimiento o direcci�n. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la informaci�n proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la informaci�n de identificaci�n directa s�lo es accesible para el personal de investigaci�n cr�tico. El c�digo (que vincula los datos personales del participante con los c�digos de barras de la muestras) se guarda en otro servidor protegido con contrase�a, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El an�lisis de muestras se realiza utilizando datos de los que se ha eliminado la informaci�n de identificaci�n directa, y todos los datos compartidos con los repositorios p�blicos tambi�n se someten a este tratamiento. Los registros de investigaci�n pueden ser revisados por la Junta de Revisi�n Institucional de UC San Diego.
</p>
<p class="consent_header">
  C�mo usaremos su Muestra
</p>
<p class="consent_content">
  La informaci�n de los an�lisis de sus datos y muestras biol�gicas se utilizar� para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en art�culos cient�ficos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, prote�nas o metabolitos. Si lo hacemos, eliminaremos toda la informaci�n directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Adem�s, los datos que se hayan eliminado de la informaci�n de identificaci�n directa se cargar�n en el Instituto Europeo de Bioinform�tica (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita informaci�n o acci�n adicional para procesar su(s) muestra(s) y/o para prop�sitos de re-consentimiento.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong><br />
  Tenga en cuenta que <strong>no se analizar� ADN humano</strong> como parte de este ni de ning�n estudio futuro. Adem�s, los m�todos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  �A qui�n puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigaci�n, usted puede comunicarse con nosotros enviando un correo electr�nico a nuestra cuenta de ayuda microsetta@ucsd.edu o  llamando a Rob Knight al 858-246-1184.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administraci�n del IRB de UC San Diego al 858-246-4777 o enviar un correo electr�nico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigaci�n o para reportar  problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaraci�n de derechos del sujeto experimental</a>" para que las conserve.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_data', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)</strong>
</p>
<p class="consent_title">
  The Microsetta Initiative
</p>
<p class="consent_header">
  ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas le pueden tomar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar razonablemente?
</p>
<p class="consent_content">
  No hay ningún beneficio monetario o directo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ), puede recibir un informe nutricional que evalúe su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
  Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento simplemente saliendo de la encuesta o retirando su consentimiento y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, crearemos y obtendremos información relacionada a usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Para compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de sus datos personales
</p>
<p class="consent_content">
  Podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos del estudio. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespec�menes e investigaci�n de uso futuro</strong>
</p>
<p class="consent_header">
  �Qui�n realiza el estudio, por qu� se le ha pedido que participe, c�mo fue seleccionado y cu�l es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) est� realizando un estudio de investigaci�n para obtener m�s informaci�n sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los dem�s en la tierra, tienen un microbioma �nico, y cuantas m�s personas estudiemos de todas las edades, m�s entenderemos acerca de c�mo los microorganismos pueden ayudarnos o da�arnos. Habr� aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros pa�ses alrededor del mundo.
</p>
<p class="consent_header">
  �Por qu� se est� llevando a cabo este estudio?
</p>
<p class="consent_content">
  El prop�sito de este estudio es evaluar con mayor precisi�n las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constituci�n corporal, la edad o la presencia de enfermedades asociadas. Las muestras biol�gicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigaci�n. Este estudio implica la recopilaci�n, el almacenamiento y el uso de su informaci�n y muestras biol�gicas con el fin de procesar sus muestras biol�gicas y para futuras investigaciones. Los resultados se utilizar�n para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, as� como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podr�n usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  �Qu� le suceder� durante el estudio?
</p>
<p class="consent_content">
  Si acepta la recolecci�n y el procesamiento de su(s) muestra(s) biol�gica(s), le ocurrir� lo siguiente:
</p>
<p class="consent_content">
  Usted ha recibido o recibir� un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolecci�n tambi�n puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa. Luego, recolectar� una muestra de usted mismo (por ejemplo, heces, piel, boca, orificio nasal, o�do, vagina), mascota o entorno, como se describe en las instrucciones del kit o en las instrucciones que le proporcionaron los coordinadores del estudio. Tambi�n se le pedir� que proporcione informaci�n general sobre la recolecci�n, como la fecha y la hora en que se recolect� su muestra. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
  Si se recolecta muestra de heces, se le pedir� que tome muestras en una variedad de formas, como las siguientes:
  <ol>
    <li>Insertando las punta(s) del hisopo en papel higi�nico usado y devolviendo el hisopo(s) en el recipiente de pl�stico suministrado;</li>
    <li>Insertando las puntas del hisopo en el papel higi�nico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devu�lvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su m�dico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior an�lisis. No verificaremos si hay sangre en las heces con fines diagn�sticos, puesto que no somos un laboratorio cl�nico;</li>
    <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
    <li>Depositando papel higi�nico sucio en el recept�culo suministrado;</li>
    <li>Enviando una muestra completa de heces en el recipiente de env�o que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriar�n la muestra de manera fiable a -20 �C/-4 �F.</li>
  </ol>
</p>
<p class="consent_content">
  Si recibi� un kit de recolecci�n de sangre, este contiene materiales e instrucciones sobre c�mo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
  Una vez que se haya analizado su muestra, cargaremos los resultados en su cuenta y le enviaremos un correo electr�nico con un enlace para iniciar sesi�n y verlos. Calculamos que puede tardar de 1 a 3 meses en conocer los resultados de su an�lisis del microbioma. Si forma parte de un subestudio espec�fico, puede llevar m�s tiempo, seg�n la duraci�n del estudio.
</p>
<p class="consent_header">
  �Cu�nto tiempo es necesario para realizar cada procedimiento del estudio, cu�nto tiempo debe dedicar en total y cu�nto durar� el estudio?
</p>
<p class="consent_content">
  Cada muestra que env�e se puede obtener en 5 minutos o menos. Esperamos que el estudio contin�e durante muchos a�os, pero sus resultados estar�n disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  �Cu�les son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participaci�n en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el an�lisis de sangre.</li>
    <li>Existe el riesgo de p�rdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigaci�n, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres ser�n informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  �Cu�les son las alternativas a participar en este estudio? �Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participaci�n en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en l�nea. Nuestros investigadores seguir�n utilizando los datos sobre usted que se recopilaron antes de que se retirara. Despu�s de retirarse, no se recopilar�n m�s datos sobre usted. Le informaremos si se encuentra nueva informaci�n importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  �Cu�les podr�an ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ning�n beneficio monetario o directo por participar en este estudio. Usted recibir� un informe que detalla los resultados de nuestro an�lisis en su(s) muestra(s) biol�gica(s), as� como datos y cifras que comparan la composici�n de su microbioma con la de otros participantes del estudio.
</p>
<p class="consent_header">
  �Hay alg�n costo vinculado con la participaci�n en la colecci�n de su(s) muestra(s) biol�gica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtenci�n de un kit. Una vez que reciba su kit, no habr� ning�n costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  �Qu� sucede si sufre una lesi�n como consecuencia directa del estudio?
</p>
<p class="consent_content">
  Si sufre una lesi�n como resultado directo de su participaci�n en esta investigaci�n, la Universidad de California le brindar� la atenci�n m�dica que necesite para tratar esas lesiones. La Universidad no le proporcionar� ninguna otra forma de compensaci�n si se lesiona. Puede llamar a la Oficina de Administraci�n del IRB al (858) 246-4777 para obtener m�s informaci�n al respecto, para preguntar sobre sus derechos como sujeto de investigaci�n o para informar problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  �Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigaci�n se mantendr�n confidenciales en la medida permitida por la ley. Como parte de su participaci�n en el estudio, usted proporcionar� informaci�n personal y/o confidencial que podr�a permitir su identificaci�n si se hiciera p�blica, como nombre, fecha de nacimiento o direcci�n. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la informaci�n proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la informaci�n de identificaci�n directa s�lo es accesible para el personal de investigaci�n cr�tico. El c�digo (que vincula los datos personales del participante con los c�digos de barras de la muestras) se guarda en otro servidor protegido con contrase�a, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El an�lisis de muestras se realiza utilizando datos de los que se ha eliminado la informaci�n de identificaci�n directa, y todos los datos compartidos con los repositorios p�blicos tambi�n se someten a este tratamiento. Los registros de investigaci�n pueden ser revisados por la Junta de Revisi�n Institucional de UC San Diego.
</p>
<p class="consent_header">
  C�mo usaremos su Muestra
</p>
<p class="consent_content">
  La informaci�n de los an�lisis de sus datos y muestras biol�gicas se utilizar� para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en art�culos cient�ficos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, prote�nas o metabolitos. Si lo hacemos, eliminaremos toda la informaci�n directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Adem�s, los datos que se hayan eliminado de la informaci�n de identificaci�n directa se cargar�n en el Instituto Europeo de Bioinform�tica (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita informaci�n o acci�n adicional para procesar su(s) muestra(s) y/o para prop�sitos de re-consentimiento.
</p>
<p class="consent_content">
  Las muestras biol�gicas (como heces, piel, orina o sangre) recolectadas de usted para este estudio y la informaci�n obtenida de sus muestras biol�gicas pueden usarse en esta investigaci�n u otra investigaci�n, y compartirse con otras organizaciones. Usted no participar� en ning�n valor comercial o beneficio derivado del uso de sus muestras biol�gicas y/o la informaci�n obtenida de ellas.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong> <br />
  Tenga en cuenta que <strong>no se analizar� ADN humano</strong> como parte de este ni de ning�n estudio futuro. Adem�s, los m�todos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  �A qui�n puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigaci�n, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electr�nico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administraci�n del IRB de UC San Diego al 858-246-4777 o enviar un correo electr�nico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigaci�n o para reportar problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaraci�n de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigaci�n y procesar su(s) muestra(s).
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_data', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación</strong>
</p>
<p class="consent_title">
  The Microsetta Initiative
</p>
<p class="consent_header">
  ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  Usted ha sido invitado a participar en un estudio de investigación titulado La Iniciativa Microsetta. Este estudio está siendo realizado por el Dr. Rob Knight de la Universidad de California - San Diego (UCSD). Usted fue seleccionado para participar en este estudio porque usted es único y su microbioma es único, no es el mismo que el de cualquier otra persona en la tierra. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se está llevando a cabo este estudio y qué le sucederá a usted durante el estudio?
</p>
<p class="consent_content">
  El propósito de este estudio de investigación es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios se clasifican por tipo de contenido y le harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio monetario o directo por participar en este estudio. Si completa uno de los cuestionarios, llamado Cuestionario de frecuencia de alimentos (FFQ), usted podrá recibir un reporte nutricional que evalúa su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores podrían aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
  Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido el abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
  Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
  Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
  ¿Qué sucede si se lesiona como resultado directo de participar en este estudio?
</p>
<p class="consent_content">
  Si sufre una lesión como resultado directo de su participación en esta investigación, la Universidad de California le brindará la atención médica que necesite para tratar esas lesiones. La Universidad no le proporcionará ninguna otra forma de compensación si se lesiona. Puede llamar a la Oficina de Administración del IRB al (858) 246-4777 para obtener más información al respecto, para preguntar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse del estudio?
</p>
<p class="consent_content">
  Su participación en este estudio es completamente voluntaria y puede retirarse en cualquier momento simplemente saliendo de la encuesta, retirando su consentimiento o solicitando la eliminación de su cuenta a través de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
  Usted no será compensado económicamente en este estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  No habrá ningún costo para usted por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados al tener a su disposición ciertas herramientas para la evaluación de la dieta, como el Cuestionario de frecuencia de alimentos (FFQ por sus siglas en inglés).
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, nosotros crearemos y obtendremos información relacionada con usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluyendo los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de sus datos personales
</p>
<p class="consent_content">
  Nosotros podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Nosotros eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos Personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos del Estudio. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 7-12 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
  El Dr. Rob Knight y su equipo de investigaci�n est�n realizando un estudio de investigaci�n para obtener m�s informaci�n sobre los trillones de peque�os seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas peque�as cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es �nico, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo (como el virus que causa el COVID-19), pero no podemos dec�rselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
  Si usted decide que quiere participar en este estudio de investigaci�n, esto es lo que le suceder�:
</p>
<p class="consent_content">
  Le pediremos a usted, a su mam� o a su pap� que tomen muestras de alg�n lugar de su cuerpo (como la piel o la boca) o sus heces (del papel higi�nico) con algo parecido a 2 hisopos. A veces necesitamos m�s heces para nuestra investigaci�n y luego le pediremos que defeque en un recipiente de pl�stico que est� debajo del asiento del inodoro y atrapa la materia fecal a medida que sale. Su mam� o pap� nos lo enviar� en el bol. Tambi�n podemos pedirle a tu mam� o pap� que te pinchen el dedo para que podamos obtener un poco de tu sangre.
</p>
<p class="consent_content">
  A veces, los ni�os no se sienten bien mientras participan en este estudio. Es posible que sienta un poco de dolor si le frotan la piel con el hisopo y un dolor temporal si le pinchan el dedo para sacar sangre. A la mayor�a de las personas no les molesta esto.
</p>
<p class="consent_content">
  No tiene que participar en este estudio de investigaci�n si no lo desea. Nadie se enfadar� con usted si dice que no. Incluso si dice que s� ahora y cambia de opini�n despu�s de comenzar a hacer este estudio, puede detenerse y nadie se enojar�.
</p>
<p class="consent_content">
  Aseg�rese de preguntarle a sus padres si tiene preguntas. Tambi�n puede pedirles que llamen al Dr. Knight o a su equipo de investigaci�n para que puedan brindarle m�s informaci�n sobre cualquier cosa que no entienda.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_data', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 7-12 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
  El Dr. Rob Knight y su equipo de investigaci�n est�n realizando un estudio de investigaci�n para obtener m�s informaci�n sobre los trillones de peque�os seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas peque�as cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es �nico, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo (como el virus que causa el COVID-19), pero no podemos dec�rselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
  Si decide que quiere participar en este estudio de investigaci�n, esto es lo que le suceder�:
</p>
<p class="consent_content">
  Le pediremos que responda preguntas en forma de encuesta sobre usted, como su edad, peso, altura, su estilo de vida, lo que come, si ha tomado antibi�ticos, si tiene ciertas enfermedades y si toma suplementos como vitaminas. Tambi�n hay otras encuestas que puede elegir completar si lo desea.
</p>
<p class="consent_content">
  Sus respuestas se mantendr�n en privado. No compartiremos ninguna informaci�n sobre si particip� o no en este estudio.
</p>
<p class="consent_content">
  A veces, los ni�os no se sienten bien mientras participan en este estudio. Es posible que se sienta un poco cansado, aburrido o inc�modo. A la mayor�a de las personas no les molesta esto.
</p>
<p class="consent_content">
  Si siente alguna de estas cosas u otras cosas, aseg�rese de dec�rselo a su mam� o pap�.
</p>
<p class="consent_content">
  No tiene que participar en este estudio de investigaci�n si no lo desea. Nadie se enfadar� con usted si dice que no. Incluso si dice que s� ahora y cambia de opini�n despu�s de comenzar este estudio, puede detenerse y nadie se enojar�.
</p>
<p class="consent_content">
  Aseg�rese de preguntarle a sus padres si tiene preguntas. Tambi�n puede pedirles que llamen al Dr. Knight o a su equipo de investigaci�n para que puedan brindarle m�s informaci�n sobre cualquier cosa que no entienda.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespecímenes e Investigación de Uso Futuro</strong>
</p>
<p class="consent_header">
  ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamado el microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y los virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se realiza este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de la información y las muestras biológicas de su hijo con el fin de procesar las muestras biológicas de su hijo y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre el niño participante que proporciona la muestra. Luego, los investigadores pueden usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué le pasará a su hijo(a) en este estudio?
</p>
<p class="consent_content">
  Si acepta la recolección y el procesamiento de las muestras biológicas de su hijo, le sucederá lo siguiente a su hijo:
</p>
<p class="consent_content">
  Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa.
</p>
<p class="consent_content">
  Tomará muestras de una parte del cuerpo de su hijo (p. ej., heces, piel, boca, orificios nasales, orejas, vagina) como se describe en las instrucciones del kit. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó la muestra de su hijo. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
  Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:
  <ol>
    <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
    <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
    <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
    <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
    <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
  </ol>
</p>
<p class="consent_content">
  Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo.
</p>
<p class="consent_content">
  Una vez que se haya analizado la muestra de su hijo, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Calculamos que puede tardar de 1 a 3 meses en conocer los resultados del análisis del microbioma de su hijo. Si su hijo es parte de un subestudio específico, puede tomar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
  ¿Cuánto tiempo llevará cada procedimiento del estudio, cuánto tiempo debe dedicar en total su hijo y cuánto durará el estudio?
</p>
<p class="consent_content">
  Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero los resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Si usa el dispositivo de recolección de sangre, su hijo puede experimentar un dolor temporal o un hematoma en el lugar del pinchazo de la aguja.</li>
    <li>Existe el riesgo de pérdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted será informado de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio? ¿Puede su hijo retirarse o ser retirado del estudio?
</p>
<p class="consent_content">
  La participación en la investigación es totalmente voluntaria. Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento sin penalización ni pérdida de los beneficios a los que usted o su hijo tienen derecho. Si decide que ya no desea que su hijo continúe en este estudio, puede retirar su consentimiento solicitando la eliminación del perfil de su hijo a través de su cuenta en línea. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio directo para su hijo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis de la muestra de su hijo, así como datos y cifras que comparan la composición microbiana de su hijo con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
  ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
  Usted no será compensado económicamente en este estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtención de un kit, pero no habrá ningún costo por participar en el procedimiento de muestreo.
</p>
<p class="consent_header">
  ¿Qué sucede si su hijo se lesiona como resultado directo de participar en este estudio?
</p>
<p class="consent_content">
  Si su hijo se lesiona como resultado directo de la participación en esta investigación, la Universidad de California le brindará la atención médica que necesite para tratar esas lesiones. La Universidad no le proporcionará ninguna otra forma de compensación si su hijo resulta lesionado. Usted o su hijo pueden llamar a la Oficina de Administración del IRB al 858-246-4777 para obtener más información al respecto, para preguntar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  ¿Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La clave del código (que relaciona la información personal del participante con los códigos de barras de la muestra) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
  La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
  Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong><br />
  Tenga en cuenta que <strong>no se analizará ADN humano</strong> como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación y que se procesen la(s) muestra(s) de su hijo.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');


INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_data', 'es_ES', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative </strong>
</p>
<p class="consent_header">
  ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamados microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se realiza este estudio y qué le pasará a su hijo en este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta permitir que su hijo participe en este estudio, le pediremos que complete encuestas/cuestionarios en línea sobre su hijo, como su edad, peso, altura, estilo de vida, dieta y si su hijo tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio directo para su hijo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ) por su hijo, puede recibir un informe nutricional que evalúe el patrón de alimentación y la ingesta de nutrientes de su hijo con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
  Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
  Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
  Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse?
</p>
<p class="consent_content">
  La participación en este estudio es completamente voluntaria y usted o su hijo pueden retirarse en cualquier momento simplemente saliendo de la encuesta, retirando el consentimiento y eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  No habrá ningún costo para usted o su hijo por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados con tener ciertas herramientas de evaluación de la dieta disponibles para su hijo, como el Cuestionario de frecuencia de alimentos (FFQ).
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, crearemos y obtendremos información relacionada con su participación o la de su hijo en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos los datos personales de su hijo
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre el estado de participación de su hijo, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de los datos personales de su hijo
</p>
<p class="consent_content">
  Podemos retener los Datos Personales que nos proporcione durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos los Datos Personales de su hijo cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, la información de su hijo se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con los Datos personales de su hijo, incluido el derecho a acceder, corregir, restringir y retirar la información personal de su hijo.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los datos del estudio de su hijo. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de Privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 13-17 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespec�menes e investigaci�n de uso futuro</strong>
</p>
<p class="consent_header">
  �Qui�n realiza el estudio, por qu� se le ha pedido que participe, c�mo fue seleccionado y cu�l es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) est� realizando un estudio de investigaci�n para obtener m�s informaci�n sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los dem�s en la tierra, tienen un microbioma �nico, y cuantas m�s personas estudiemos de todas las edades, m�s entenderemos acerca de c�mo los microorganismos pueden ayudarnos o da�arnos. Habr� aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros pa�ses alrededor del mundo.
</p>
<p class="consent_header">
  �Por qu� se est� llevando a cabo este estudio?
</p>
<p class="consent_content">
  El prop�sito de este estudio es evaluar con mayor precisi�n las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constituci�n corporal, la edad o la presencia de enfermedades asociadas. Las muestras biol�gicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigaci�n. Este estudio implica la recopilaci�n, el almacenamiento y el uso de su informaci�n y muestras biol�gicas con el fin de procesar sus muestras biol�gicas y para futuras investigaciones. Los resultados se utilizar�n para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, as� como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podr�n usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  �Qu� le suceder� en este estudio y qu� procedimientos son el est�ndar de atenci�n y cu�les son experimentales?
</p>
<p class="consent_content">
  Si usted acepta participar en este estudio, le ocurrir� lo siguiente:
</p>
<p class="consent_content">
  Usted mismo tomar� la muestra usando el kit que se le proporcion�. Las instrucciones est�n incluidas en el kit para que sepa qu� hacer. La muestra m�s com�n es de heces (fecal) donde se recoge una peque�a muestra insertando las puntas de un hisopo en el papel higi�nico usado o en una tarjeta (tarjeta llamada FOBT). Tambi�n se le puede pedir que saque un trozo de materia fecal con una peque�a herramienta similar a una cuchara, que coloque papel higi�nico usado en un recept�culo especial que le proporcionaremos o que defeque en un recipiente de pl�stico que se coloca debajo del asiento del ba�o. Tambi�n es posible que deba tomar muestras de una peque�a �rea de la piel, la lengua o la boca, las fosas nasales, la cera del o�do o la vagina. Tambi�n podemos pedirle a alguien (como su mam� o pap�) que tome una peque�a muestra de sangre pinchando su dedo y luego recolectando la sangre en 2 hisopos peque�os. Ninguna de estas muestras o investigaciones nos permitir� hacer un diagn�stico de enfermedad y no estamos buscando nada en su propio ADN que tambi�n se pueda encontrar en sus heces, piel o saliva.
</p>
<p class="consent_header">
  �Cu�nto tiempo es necesario para realizar cada procedimiento del estudio, cu�nto tiempo debe dedicar en total y cu�nto durar� el estudio?
</p>
<p class="consent_content">
  Cada muestra que env�e se puede obtener en 5 minutos o menos. Esperamos que el estudio contin�e durante muchos a�os, pero sus resultados estar�n disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  �Cu�les son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participaci�n en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el an�lisis de sangre.</li>
    <li>Existe el riesgo de p�rdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigaci�n, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres ser�n informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  �Cu�les son las alternativas a participar en este estudio? �Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participaci�n en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en l�nea. Nuestros investigadores seguir�n utilizando los datos sobre usted que se recopilaron antes de que se retirara. Despu�s de retirarse, no se recopilar�n m�s datos sobre usted. Le informaremos si se encuentra nueva informaci�n importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  �Cu�les podr�an ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ning�n beneficio directo para usted por participar en este estudio. Usted tendr� acceso a sus datos que le dar�n a usted y a sus padres una idea de lo que hay en su muestra y c�mo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
  �Se le pagar� por participar en este estudio?
</p>
<p class="consent_content">
  Usted  no recibir� ninguna remuneraci�n econ�mica por participar en este estudio.
</p>
<p class="consent_header">
  �Hay alg�n costo vinculado con la participaci�n en la colecci�n de su(s) muestra(s) biol�gica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtenci�n de un kit. Una vez que reciba su kit, no habr� ning�n costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  �Qu� sucede si sufre una lesi�n como consecuencia directa del estudio?
</p>
<p class="consent_content">
  Si usted se lesiona o se enferma como resultado directo de este estudio de investigaci�n, se le brindar� atenci�n m�dica.
</p>
<p class="consent_header">
  �Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigaci�n se mantendr�n confidenciales en la medida permitida por la ley. Como parte de su participaci�n en el estudio, usted proporcionar� informaci�n personal y/o confidencial que podr�a permitir su identificaci�n si se hiciera p�blica, como nombre, fecha de nacimiento o direcci�n. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la informaci�n proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la informaci�n de identificaci�n directa s�lo es accesible para el personal de investigaci�n cr�tico. El c�digo (que vincula los datos personales del participante con los c�digos de barras de la muestras) se guarda en otro servidor protegido con contrase�a, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El an�lisis de muestras se realiza utilizando datos de los que se ha eliminado la informaci�n de identificaci�n directa, y todos los datos compartidos con los repositorios p�blicos tambi�n se someten a este tratamiento. Los registros de investigaci�n pueden ser revisados por la Junta de Revisi�n Institucional de UC San Diego.
</p>
<p class="consent_header">
  C�mo usaremos su Muestra
</p>
<p class="consent_content">
  La informaci�n de los an�lisis de sus datos y muestras biol�gicas se utilizar� para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en art�culos cient�ficos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, prote�nas o metabolitos. Si lo hacemos, eliminaremos toda la informaci�n directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Adem�s, los datos que se hayan eliminado de la informaci�n de identificaci�n directa se cargar�n en el Instituto Europeo de Bioinform�tica (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita informaci�n o acci�n adicional para procesar su(s) muestra(s) y/o para prop�sitos de re-consentimiento.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong><br />
  Tenga en cuenta que <strong>no se analizar� ADN humano</strong> como parte de este ni de ning�n estudio futuro. Adem�s, los m�todos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  �A qui�n puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigaci�n, usted puede comunicarse con nosotros enviando un correo electr�nico a nuestra cuenta de ayuda microsetta@ucsd.edu o  llamando a Rob Knight al 858-246-1184.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administraci�n del IRB de UC San Diego al 858-246-4777 o enviar un correo electr�nico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigaci�n o para reportar  problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaraci�n de derechos del sujeto experimental</a>" para que las conserve.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adolescent_data', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)</strong>
</p>
<p class="consent_title">
  The Microsetta Initiative
</p>
<p class="consent_header">
  ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas le pueden tomar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar razonablemente?
</p>
<p class="consent_content">
  No hay ningún beneficio monetario o directo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ), puede recibir un informe nutricional que evalúe su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
  Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento simplemente saliendo de la encuesta o retirando su consentimiento y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, crearemos y obtendremos información relacionada a usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Para compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de sus datos personales
</p>
<p class="consent_content">
  Podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos del estudio. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespec�menes e investigaci�n de uso futuro</strong>
</p>
<p class="consent_header">
  �Qui�n realiza el estudio, por qu� se le ha pedido que participe, c�mo fue seleccionado y cu�l es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight de la Universidad de California - San Diego (UCSD) est� realizando un estudio de investigaci�n para obtener m�s informaci�n sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los dem�s en la tierra, tienen un microbioma �nico, y cuantas m�s personas estudiemos de todas las edades, m�s entenderemos acerca de c�mo los microorganismos pueden ayudarnos o da�arnos. Habr� aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros pa�ses alrededor del mundo.
</p>
<p class="consent_header">
  �Por qu� se est� llevando a cabo este estudio?
</p>
<p class="consent_content">
  El prop�sito de este estudio es evaluar con mayor precisi�n las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constituci�n corporal, la edad o la presencia de enfermedades asociadas. Las muestras biol�gicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigaci�n. Este estudio implica la recopilaci�n, el almacenamiento y el uso de su informaci�n y muestras biol�gicas con el fin de procesar sus muestras biol�gicas y para futuras investigaciones. Los resultados se utilizar�n para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, as� como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podr�n usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  �Qu� le suceder� durante el estudio?
</p>
<p class="consent_content">
  Si acepta la recolecci�n y el procesamiento de su(s) muestra(s) biol�gica(s), le ocurrir� lo siguiente:
</p>
<p class="consent_content">
  Usted ha recibido o recibir� un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolecci�n tambi�n puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa. Luego, recolectar� una muestra de usted mismo (por ejemplo, heces, piel, boca, orificio nasal, o�do, vagina), mascota o entorno, como se describe en las instrucciones del kit o en las instrucciones que le proporcionaron los coordinadores del estudio. Tambi�n se le pedir� que proporcione informaci�n general sobre la recolecci�n, como la fecha y la hora en que se recolect� su muestra. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
  Si se recolecta muestra de heces, se le pedir� que tome muestras en una variedad de formas, como las siguientes:
  <ol>
    <li>Insertando las punta(s) del hisopo en papel higi�nico usado y devolviendo el hisopo(s) en el recipiente de pl�stico suministrado;</li>
    <li>Insertando las puntas del hisopo en el papel higi�nico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devu�lvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su m�dico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior an�lisis. No verificaremos si hay sangre en las heces con fines diagn�sticos, puesto que no somos un laboratorio cl�nico;</li>
    <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
    <li>Depositando papel higi�nico sucio en el recept�culo suministrado;</li>
    <li>Enviando una muestra completa de heces en el recipiente de env�o que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriar�n la muestra de manera fiable a -20 �C/-4 �F.</li>
  </ol>
</p>
<p class="consent_content">
  Si recibi� un kit de recolecci�n de sangre, este contiene materiales e instrucciones sobre c�mo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
  Una vez que se haya analizado su muestra, cargaremos los resultados en su cuenta y le enviaremos un correo electr�nico con un enlace para iniciar sesi�n y verlos. Calculamos que puede tardar de 1 a 3 meses en conocer los resultados de su an�lisis del microbioma. Si forma parte de un subestudio espec�fico, puede llevar m�s tiempo, seg�n la duraci�n del estudio.
</p>
<p class="consent_header">
  �Cu�nto tiempo es necesario para realizar cada procedimiento del estudio, cu�nto tiempo debe dedicar en total y cu�nto durar� el estudio?
</p>
<p class="consent_content">
  Cada muestra que env�e se puede obtener en 5 minutos o menos. Esperamos que el estudio contin�e durante muchos a�os, pero sus resultados estar�n disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  �Cu�les son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participaci�n en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el an�lisis de sangre.</li>
    <li>Existe el riesgo de p�rdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigaci�n, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres ser�n informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  �Cu�les son las alternativas a participar en este estudio? �Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participaci�n en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en l�nea. Nuestros investigadores seguir�n utilizando los datos sobre usted que se recopilaron antes de que se retirara. Despu�s de retirarse, no se recopilar�n m�s datos sobre usted. Le informaremos si se encuentra nueva informaci�n importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  �Cu�les podr�an ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ning�n beneficio monetario o directo por participar en este estudio. Usted recibir� un informe que detalla los resultados de nuestro an�lisis en su(s) muestra(s) biol�gica(s), as� como datos y cifras que comparan la composici�n de su microbioma con la de otros participantes del estudio.
</p>
<p class="consent_header">
  �Hay alg�n costo vinculado con la participaci�n en la colecci�n de su(s) muestra(s) biol�gica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtenci�n de un kit. Una vez que reciba su kit, no habr� ning�n costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  �Qu� sucede si sufre una lesi�n como consecuencia directa del estudio?
</p>
<p class="consent_content">
  Si sufre una lesi�n como resultado directo de su participaci�n en esta investigaci�n, la Universidad de California le brindar� la atenci�n m�dica que necesite para tratar esas lesiones. La Universidad no le proporcionar� ninguna otra forma de compensaci�n si se lesiona. Puede llamar a la Oficina de Administraci�n del IRB al (858) 246-4777 para obtener m�s informaci�n al respecto, para preguntar sobre sus derechos como sujeto de investigaci�n o para informar problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  �Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigaci�n se mantendr�n confidenciales en la medida permitida por la ley. Como parte de su participaci�n en el estudio, usted proporcionar� informaci�n personal y/o confidencial que podr�a permitir su identificaci�n si se hiciera p�blica, como nombre, fecha de nacimiento o direcci�n. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la informaci�n proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la informaci�n de identificaci�n directa s�lo es accesible para el personal de investigaci�n cr�tico. El c�digo (que vincula los datos personales del participante con los c�digos de barras de la muestras) se guarda en otro servidor protegido con contrase�a, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El an�lisis de muestras se realiza utilizando datos de los que se ha eliminado la informaci�n de identificaci�n directa, y todos los datos compartidos con los repositorios p�blicos tambi�n se someten a este tratamiento. Los registros de investigaci�n pueden ser revisados por la Junta de Revisi�n Institucional de UC San Diego.
</p>
<p class="consent_header">
  C�mo usaremos su Muestra
</p>
<p class="consent_content">
  La informaci�n de los an�lisis de sus datos y muestras biol�gicas se utilizar� para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en art�culos cient�ficos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, prote�nas o metabolitos. Si lo hacemos, eliminaremos toda la informaci�n directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Adem�s, los datos que se hayan eliminado de la informaci�n de identificaci�n directa se cargar�n en el Instituto Europeo de Bioinform�tica (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita informaci�n o acci�n adicional para procesar su(s) muestra(s) y/o para prop�sitos de re-consentimiento.
</p>
<p class="consent_content">
  Las muestras biol�gicas (como heces, piel, orina o sangre) recolectadas de usted para este estudio y la informaci�n obtenida de sus muestras biol�gicas pueden usarse en esta investigaci�n u otra investigaci�n, y compartirse con otras organizaciones. Usted no participar� en ning�n valor comercial o beneficio derivado del uso de sus muestras biol�gicas y/o la informaci�n obtenida de ellas.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong> <br />
  Tenga en cuenta que <strong>no se analizar� ADN humano</strong> como parte de este ni de ning�n estudio futuro. Adem�s, los m�todos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  �A qui�n puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigaci�n, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electr�nico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administraci�n del IRB de UC San Diego al 858-246-4777 o enviar un correo electr�nico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigaci�n o para reportar problemas relacionados con la investigaci�n.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaraci�n de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigaci�n y procesar su(s) muestra(s).
</p>', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('adult_data', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación</strong>
</p>
<p class="consent_title">
  The Microsetta Initiative
</p>
<p class="consent_header">
  ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
  Usted ha sido invitado a participar en un estudio de investigación titulado La Iniciativa Microsetta. Este estudio está siendo realizado por el Dr. Rob Knight de la Universidad de California - San Diego (UCSD). Usted fue seleccionado para participar en este estudio porque usted es único y su microbioma es único, no es el mismo que el de cualquier otra persona en la tierra. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se está llevando a cabo este estudio y qué le sucederá a usted durante el estudio?
</p>
<p class="consent_content">
  El propósito de este estudio de investigación es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios se clasifican por tipo de contenido y le harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio monetario o directo por participar en este estudio. Si completa uno de los cuestionarios, llamado Cuestionario de frecuencia de alimentos (FFQ), usted podrá recibir un reporte nutricional que evalúa su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores podrían aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
  Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido el abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
  Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
  Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
  ¿Qué sucede si se lesiona como resultado directo de participar en este estudio?
</p>
<p class="consent_content">
  Si sufre una lesión como resultado directo de su participación en esta investigación, la Universidad de California le brindará la atención médica que necesite para tratar esas lesiones. La Universidad no le proporcionará ninguna otra forma de compensación si se lesiona. Puede llamar a la Oficina de Administración del IRB al (858) 246-4777 para obtener más información al respecto, para preguntar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse del estudio?
</p>
<p class="consent_content">
  Su participación en este estudio es completamente voluntaria y puede retirarse en cualquier momento simplemente saliendo de la encuesta, retirando su consentimiento o solicitando la eliminación de su cuenta a través de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
  Usted no será compensado económicamente en este estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  No habrá ningún costo para usted por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados al tener a su disposición ciertas herramientas para la evaluación de la dieta, como el Cuestionario de frecuencia de alimentos (FFQ por sus siglas en inglés).
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, nosotros crearemos y obtendremos información relacionada con usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluyendo los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de sus datos personales
</p>
<p class="consent_content">
  Nosotros podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Nosotros eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos Personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos del Estudio. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 7-12 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
  El Dr. Rob Knight y su equipo de investigaci�n est�n realizando un estudio de investigaci�n para obtener m�s informaci�n sobre los trillones de peque�os seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas peque�as cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es �nico, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo (como el virus que causa el COVID-19), pero no podemos dec�rselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
  Si usted decide que quiere participar en este estudio de investigaci�n, esto es lo que le suceder�:
</p>
<p class="consent_content">
  Le pediremos a usted, a su mam� o a su pap� que tomen muestras de alg�n lugar de su cuerpo (como la piel o la boca) o sus heces (del papel higi�nico) con algo parecido a 2 hisopos. A veces necesitamos m�s heces para nuestra investigaci�n y luego le pediremos que defeque en un recipiente de pl�stico que est� debajo del asiento del inodoro y atrapa la materia fecal a medida que sale. Su mam� o pap� nos lo enviar� en el bol. Tambi�n podemos pedirle a tu mam� o pap� que te pinchen el dedo para que podamos obtener un poco de tu sangre.
</p>
<p class="consent_content">
  A veces, los ni�os no se sienten bien mientras participan en este estudio. Es posible que sienta un poco de dolor si le frotan la piel con el hisopo y un dolor temporal si le pinchan el dedo para sacar sangre. A la mayor�a de las personas no les molesta esto.
</p>
<p class="consent_content">
  No tiene que participar en este estudio de investigaci�n si no lo desea. Nadie se enfadar� con usted si dice que no. Incluso si dice que s� ahora y cambia de opini�n despu�s de comenzar a hacer este estudio, puede detenerse y nadie se enojar�.
</p>
<p class="consent_content">
  Aseg�rese de preguntarle a sus padres si tiene preguntas. Tambi�n puede pedirles que llamen al Dr. Knight o a su equipo de investigaci�n para que puedan brindarle m�s informaci�n sobre cualquier cosa que no entienda.
</p>', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('child_data', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigaci�n<br />
    (Edades 7-12 a�os)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
  El Dr. Rob Knight y su equipo de investigaci�n est�n realizando un estudio de investigaci�n para obtener m�s informaci�n sobre los trillones de peque�os seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas peque�as cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es �nico, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo (como el virus que causa el COVID-19), pero no podemos dec�rselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
  Si decide que quiere participar en este estudio de investigaci�n, esto es lo que le suceder�:
</p>
<p class="consent_content">
  Le pediremos que responda preguntas en forma de encuesta sobre usted, como su edad, peso, altura, su estilo de vida, lo que come, si ha tomado antibi�ticos, si tiene ciertas enfermedades y si toma suplementos como vitaminas. Tambi�n hay otras encuestas que puede elegir completar si lo desea.
</p>
<p class="consent_content">
  Sus respuestas se mantendr�n en privado. No compartiremos ninguna informaci�n sobre si particip� o no en este estudio.
</p>
<p class="consent_content">
  A veces, los ni�os no se sienten bien mientras participan en este estudio. Es posible que se sienta un poco cansado, aburrido o inc�modo. A la mayor�a de las personas no les molesta esto.
</p>
<p class="consent_content">
  Si siente alguna de estas cosas u otras cosas, aseg�rese de dec�rselo a su mam� o pap�.
</p>
<p class="consent_content">
  No tiene que participar en este estudio de investigaci�n si no lo desea. Nadie se enfadar� con usted si dice que no. Incluso si dice que s� ahora y cambia de opini�n despu�s de comenzar este estudio, puede detenerse y nadie se enojar�.
</p>
<p class="consent_content">
  Aseg�rese de preguntarle a sus padres si tiene preguntas. Tambi�n puede pedirles que llamen al Dr. Knight o a su equipo de investigaci�n para que puedan brindarle m�s informaci�n sobre cualquier cosa que no entienda.
</p>', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');

INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespecímenes e Investigación de Uso Futuro</strong>
</p>
<p class="consent_header">
  ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamado el microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y los virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se realiza este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de la información y las muestras biológicas de su hijo con el fin de procesar las muestras biológicas de su hijo y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre el niño participante que proporciona la muestra. Luego, los investigadores pueden usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué le pasará a su hijo(a) en este estudio?
</p>
<p class="consent_content">
  Si acepta la recolección y el procesamiento de las muestras biológicas de su hijo, le sucederá lo siguiente a su hijo:
</p>
<p class="consent_content">
  Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa.
</p>
<p class="consent_content">
  Tomará muestras de una parte del cuerpo de su hijo (p. ej., heces, piel, boca, orificios nasales, orejas, vagina) como se describe en las instrucciones del kit. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó la muestra de su hijo. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
  Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:
  <ol>
    <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
    <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
    <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
    <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
    <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
  </ol>
</p>
<p class="consent_content">
  Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo.
</p>
<p class="consent_content">
  Una vez que se haya analizado la muestra de su hijo, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Calculamos que puede tardar de 1 a 3 meses en conocer los resultados del análisis del microbioma de su hijo. Si su hijo es parte de un subestudio específico, puede tomar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
  ¿Cuánto tiempo llevará cada procedimiento del estudio, cuánto tiempo debe dedicar en total su hijo y cuánto durará el estudio?
</p>
<p class="consent_content">
  Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero los resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Si usa el dispositivo de recolección de sangre, su hijo puede experimentar un dolor temporal o un hematoma en el lugar del pinchazo de la aguja.</li>
    <li>Existe el riesgo de pérdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted será informado de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio? ¿Puede su hijo retirarse o ser retirado del estudio?
</p>
<p class="consent_content">
  La participación en la investigación es totalmente voluntaria. Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento sin penalización ni pérdida de los beneficios a los que usted o su hijo tienen derecho. Si decide que ya no desea que su hijo continúe en este estudio, puede retirar su consentimiento solicitando la eliminación del perfil de su hijo a través de su cuenta en línea. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio directo para su hijo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis de la muestra de su hijo, así como datos y cifras que comparan la composición microbiana de su hijo con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
  ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
  Usted no será compensado económicamente en este estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtención de un kit, pero no habrá ningún costo por participar en el procedimiento de muestreo.
</p>
<p class="consent_header">
  ¿Qué sucede si su hijo se lesiona como resultado directo de participar en este estudio?
</p>
<p class="consent_content">
  Si su hijo se lesiona como resultado directo de la participación en esta investigación, la Universidad de California le brindará la atención médica que necesite para tratar esas lesiones. La Universidad no le proporcionará ninguna otra forma de compensación si su hijo resulta lesionado. Usted o su hijo pueden llamar a la Oficina de Administración del IRB al 858-246-4777 para obtener más información al respecto, para preguntar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  ¿Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La clave del código (que relaciona la información personal del participante con los códigos de barras de la muestra) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
  La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
  Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong><br />
  Tenga en cuenta que <strong>no se analizará ADN humano</strong> como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación y que se procesen la(s) muestra(s) de su hijo.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');


INSERT INTO ag.consent_documents ("consent_type", "locale", "date_time", "consent_content", "reconsent_required", "account_id")
    VALUES ('parent_data', 'es_MX', NOW(), '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative </strong>
</p>
<p class="consent_header">
  ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
  El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamados microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
  ¿Por qué se realiza este estudio y qué le pasará a su hijo en este estudio?
</p>
<p class="consent_content">
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta permitir que su hijo participe en este estudio, le pediremos que complete encuestas/cuestionarios en línea sobre su hijo, como su edad, peso, altura, estilo de vida, dieta y si su hijo tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
  ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
  No hay ningún beneficio directo para su hijo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ) por su hijo, puede recibir un informe nutricional que evalúe el patrón de alimentación y la ingesta de nutrientes de su hijo con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué riesgos están asociados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La clave del código (que relaciona la información personal del participante) se conserva en un servidor separado protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El código se destruirá mediante la eliminación del servidor al final del estudio o si se retira del estudio. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
  Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
  Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
  Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse?
</p>
<p class="consent_content">
  La participación en este estudio es completamente voluntaria y usted o su hijo pueden retirarse en cualquier momento simplemente saliendo de la encuesta, retirando el consentimiento y eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
</p>
<p class="consent_header">
  ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
  No habrá ningún costo para usted o su hijo por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados con tener ciertas herramientas de evaluación de la dieta disponibles para su hijo, como el Cuestionario de frecuencia de alimentos (FFQ).
</p>
<p class="consent_header">
  Conoce lo que recopilaremos
</p>
<p class="consent_content">
  Como parte de este estudio de investigación, crearemos y obtendremos información relacionada con su participación o la de su hijo en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
  Cómo utilizaremos los datos personales de su hijo
</p>
<p class="consent_content">
  Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
  <ul>
    <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
    <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
    <li>Para comunicarnos con usted con el fin de recibir alertas sobre el estado de participación de su hijo, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
    <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
    <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
  </ul>
</p>
<p class="consent_header">
  Conservación de los datos personales de su hijo
</p>
<p class="consent_content">
  Podemos retener los Datos Personales que nos proporcione durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos los Datos Personales de su hijo cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, la información de su hijo se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
  Sus derechos de privacidad
</p>
<p class="consent_content">
  El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con los Datos personales de su hijo, incluido el derecho a acceder, corregir, restringir y retirar la información personal de su hijo.
</p>
<p class="consent_content">
  El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los datos del estudio de su hijo. En este documento de consentimiento se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
  Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
  Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de Privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación.
</p>
', 'true','000fc4cd-8fa4-db8b-e050-8a800c5d81b7');