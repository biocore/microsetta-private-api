-- Jun 22, 2016
-- Add IMPACT OF PERSONAL MICROBIOME INFORMATION survey
----------------------------------------------------------
-- survey_group
----------------------------------------------------------
INSERT INTO survey_group (group_order, american, british) VALUES (-5, 'Personal_Microbiome', 'Personal_Microbiome');

----------------------------------------------------------
-- surveys
----------------------------------------------------------
INSERT INTO surveys (survey_id, survey_group) VALUES (5, -5);

----------------------------------------------------------
-- survey_question
----------------------------------------------------------
-- Change so can have the same wording on supplemental questionares, but the short name must still be unique
ALTER TABLE ag.survey_question DROP CONSTRAINT idx_survey_question;
ALTER TABLE ag.survey_question DROP CONSTRAINT idx_survey_question_0;
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(186, 'PM_GENDER', 'What is your gender?', 'What is your gender?'),
(187, 'PM_AGE', 'What is your age?', 'What is your age?'),
(188, 'PM_ETHNICITY', 'What is your ethnicity?', 'What is your ethnicity?'),
(189, 'PM_EDUCATION', 'What is your highest level of education?', 'What is your highest level of education?'),
(190, 'PM_HEALTH', 'How good is your health?', 'How good is your health?'),
(191, 'PM_PARTICIPATION_REASON', 'What prompted you to participate in the American Gut Project? Please select all that apply.', 'What prompted you to participate in the American Gut Project? Please select all that apply.'),
(192, 'PM_GASTRO_PROBLEMS', 'If you checked "I have gastrointestinal problems", what type of problems do you have? Please select all that apply.', 'If you checked "I have gastrointestinal problems", what type of problems do you have? Please select all that apply.'),
(193, 'PM_UNDERSTAND_RESULTS', 'Do you feel you understand your personal microbiome results?', 'Do you feel you understand your personal microbiome results?'),
(194, 'PM_USEFUL', 'In general, do you feel that your personal microbiome results are useful to you?', 'In general, do you feel that your personal microbiome results are useful to you?'),
(195, 'PM_LIFESTYLE_CHANGE', 'Do you think receiving your personal microbiome results has changed your behavior or lifestyle in any way?', 'Do you think receiving your personal microbiome results has changed your behavior or lifestyle in any way?'),
(196, 'PM_LIFESTYLE_CHANGE_HOW', 'If you responded "YES" to the question above, in what way has receiving your personal microbiome results changed your behavior or lifestyle? Please select all that apply.', 'If you responded "YES" to the question above, in what way has receiving your personal microbiome results changed your behavior or lifestyle? Please select all that apply.'),
(197, 'PM_CONCERN', 'Now that you have your personal microbiome results, OVERALL are you', 'Now that you have your personal microbiome results, OVERALL are you'),
(198, 'PM_SHARED', 'Have you shared or discussed your personal microbiome results with anyone else?', 'Have you shared or discussed your personal microbiome results with anyone else?'),
(199, 'PM_SHARED_WHO', 'If you responded "YES" to the question above, with whom did you share or discuss your personal microbiome results? Please select all that apply.', 'If you responded "YES" to the question above, with whom did you share or discuss your personal microbiome results? Please select all that apply.'),
(200, 'PM_SHARED_PCP', 'If you shared or discussed your personal microbiome results with your primary care physician or another health professional, how willing was s/he to discuss your results with you?', 'If you shared or discussed your personal microbiome results with your primary care physician or another health professional, how willing was s/he to discuss your results with you?'),
(201, 'PM_SHARED_PCP_CHANGES', 'If you shared your personal microbiome results with your primary care physician or another health professional, did s/he make any changes to your healthcare?', 'If you shared your personal microbiome results with your primary care physician or another health professional, did s/he make any changes to your healthcare?'),
(202, 'PM_SHARED_PCP_CHANGES_WHAT', 'If you responded "YES" to the question above, what changes did your healthcare provider make to your healthcare? Please select all that apply.', 'If you responded "YES" to the question above, what changes did your healthcare provider make to your healthcare? Please select all that apply.'),
(203, 'PM_EXPERIENCE_WORTH_IT', 'Overall, was your experience participating in American Gut and receiving your personal microbiome results worth the payment/donation you provided?', 'Overall, was your experience participating in American Gut and receiving your personal microbiome results worth the payment/donation you provided?'),
(204, 'PM_RECONTACT', 'As part of our research, we may conduct follow-up interviews to better understand the impact of participation in the American Gut Project. Would you like to be contacted in the future?', 'As part of our research, we may conduct follow-up interviews to better understand the impact of participation in the American Gut Project. Would you like to be contacted in the future?'),
(205, 'PM_NAME', 'Please provide your name', 'Please provide your name'),
(206, 'PM_PHONE', 'Please provide your phone number', 'Please provide your phone number'),
(207, 'PM_EMAIL', 'Please provide your email', 'Please provide your email'),
(208, 'PM_OTHER', 'Please provide any additional information you think is relevant.', 'Please provide any additional information you think is relevant.');

----------------------------------------------------------
-- group_questions
----------------------------------------------------------
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 186, 0);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 187, 1);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 188, 2);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 189, 3);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 190, 4);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 191, 5);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 192, 6);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 193, 7);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 194, 8);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 195, 9);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 196, 10);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 197, 11);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 198, 12);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 199, 13);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 200, 14);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 201, 15);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 202, 16);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 203, 17);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 204, 18);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 205, 19);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 206, 20);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 207, 21);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-5, 208, 22);

----------------------------------------------------------
-- survey_question_response_type
----------------------------------------------------------
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (186, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (187, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (188, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (189, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (190, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (191, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (192, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (193, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (194, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (195, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (196, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (197, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (198, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (199, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (200, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (201, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (202, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (203, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (204, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (205, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (206, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (207, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (208, 'TEXT');

----------------------------------------------------------
-- survey_response
----------------------------------------------------------
INSERT INTO survey_response (american, british) VALUES
('18-24', '18-24'),
('25-34', '25-34'),
('35-44', '35-44'),
('45-54', '45-54'),
('55-64', '55-64'),
('65+', '65+');

INSERT INTO survey_response (american, british) VALUES
('American Indian/Alaskan Native', 'American Indian/Alaskan Native'),
('Black', 'Black'),
('White', 'White');

INSERT INTO survey_response (american, british) VALUES
('Less than a high school diploma/GED', 'Less than a high school diploma/GED'),
('High school diploma/GED', 'High school diploma/GED'),
('Associate''s degree (i.e. AA, AS)', 'Associate''s degree (i.e. AA, AS)'),
('Bachelor''s degree (i.e. BA, BS)', 'Bachelor''s degree (i.e. BA, BS)'),
('Graduate degree (i.e. MSW, MBA)', 'Graduate degree (i.e. MSW, MBA)'),
('Doctoral degree (i.e. PhD, EdD)', 'Doctoral degree (i.e. PhD, EdD)'),
('Professional degree (i.e. MD, DDS)', 'Professional degree (i.e. MD, DDS)');

INSERT INTO survey_response (american, british) VALUES
('Very good', 'Very good'),
('Good', 'Good'),
('Average', 'Average'),
('Poor', 'Poor'),
('Very Poor', 'Very Poor');

INSERT INTO survey_response (american, british) VALUES
('General curiosity/interest in learning about my microbiome', 'General curiosity/interest in learning about my microbiome'),
('Desire to improve my health', 'Desire to improve my health'),
('The study seemed fun and entertaining', 'The study seemed fun and entertaining'),
('People in my family or social network have done it', 'People in my family or social network have done it'),
('Professional interest in the microbiome', 'Professional interest in the microbiome'),
('Interest in contributing to science', 'Interest in contributing to science'),
('I have gastrointestinal problems', 'I have gastrointestinal problems'),
('I have other microbiome-relevant health problems', 'I have other microbiome-relevant health problems');

INSERT INTO survey_response (american, british) VALUES
('Crohn''s disease or Ulcerative Colitis', 'Crohn''s disease or Ulcerative Colitis'),
('Gastrointestinal cancer', 'Gastrointestinal cancer'),
('Frequent (more than once a week) diarrhea', 'Frequent (more than once a week) diarrhea'),
('Frequent (more than once a week) constipation', 'Frequent (more than once a week) constipation'),
('Irritable Bowel Syndrome (IBS)', 'Irritable Bowel Syndrome (IBS)'),
('I have had surgery on my intestines', 'I have had surgery on my intestines');

INSERT INTO survey_response (american, british) VALUES
('Somewhat', 'Somewhat'),
('No, but I plan to make changes in the future', 'No, but I plan to make changes in the future'),
('No, but I plan to discuss my results with someone else in the future', 'No, but I plan to discuss my results with someone else in the future');

INSERT INTO survey_response (american, british) VALUES
('Change in diet (i.e. taking a probiotic)', 'Change in diet (i.e. taking a probiotic)'),
('Change in exercise', 'Change in exercise'),
('Change in alcohol or tobacco use (i.e. starting, stopping, or changing amount consumed)', 'Change in alcohol or tobacco use (i.e. starting, stopping, or changing amount consumed)'),
('Change in use of nutritional supplements or vitamins', 'Change in use of nutritional supplements or vitamins'),
('Change in physical environment (i.e. adopting or getting rid of a pet, cleaning more or less often)', 'Change in physical environment (i.e. adopting or getting rid of a pet, cleaning more or less often)');

INSERT INTO survey_response (american, british) VALUES
('Significantly less concerned about your health', 'Significantly less concerned about your health'),
('Somewhat less concerned about your health', 'Somewhat less concerned about your health'),
('As concerned about your health now as you were prior to receiving your results (the results didn''t affect how I view my health)', 'As concerned about your health now as you were prior to receiving your results (the results didn''t affect how I view my health)'),
('Somewhat more concerned about your health', 'Somewhat more concerned about your health'),
('Significantly more concerned about your health', 'Significantly more concerned about your health');

INSERT INTO survey_response (american, british) VALUES
('Primary care physician', 'Primary care physician'),
('Specialty physician (e.g., gastroenterologist)', 'Specialty physician (e.g., gastroenterologist)'),
('Nutritionist/dietician', 'Nutritionist/dietician'),
('Other medical or health professional', 'Other medical or health professional'),
('Family member(s)', 'Family member(s)'),
('Friend(s)', 'Friend(s)'),
('Colleague(s)', 'Colleague(s)'),
('Posted/discussed on social networking site (i.e. Facebook)', 'Posted/discussed on social networking site (i.e. Facebook)'),
('Posted/discussed on an online patient/health platform (i.e. PatientsLikeMe)', 'Posted/discussed on an online patient/health platform (i.e. PatientsLikeMe)'),
('Posted/discussed on data sharing platform (i.e. Open Humans)', 'Posted/discussed on data sharing platform (i.e. Open Humans)');

INSERT INTO survey_response (american, british) VALUES
('Very willing/enthusiastic', 'Very willing/enthusiastic'),
('Willing', 'Willing'),
('Neutral', 'Neutral'),
('Not willing', 'Not willing'),
('Very unwilling', 'Very unwilling');

INSERT INTO survey_response (american, british) VALUES
('Ordered additional labs, tests, or procedures', 'Ordered additional labs, tests, or procedures'),
('Change in medication (i.e. starting, stopping, or changing the dose of a prescription)', 'Change in medication (i.e. starting, stopping, or changing the dose of a prescription)'),
('Change in behavioral/lifestyle recommendations (e.g., start probiotic)', 'Change in behavioral/lifestyle recommendations (e.g., start probiotic)'),
('Referral to a specialist (e.g., gastroenterologist)', 'Referral to a specialist (e.g., gastroenterologist)');

----------------------------------------------------------
-- survey_question_response
----------------------------------------------------------

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(186, 'Unspecified', 0),
(186, 'Male', 1),
(186, 'Female', 2);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(187, 'Unspecified', 0),
(187, '18-24', 1),
(187, '25-34', 2),
(187, '35-44', 3),
(187, '45-54', 4),
(187, '55-64', 5),
(187, '65+', 6);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(188, 'Unspecified', 0),
(188, 'American Indian/Alaskan Native', 1),
(188, 'Asian or Pacific Islander', 2),
(188, 'Black', 3),
(188, 'Hispanic', 4),
(188, 'White', 5),
(188, 'Other', 6);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(189, 'Unspecified', 0),
(189, 'Less than a high school diploma/GED', 1),
(189, 'High school diploma/GED', 2),
(189, 'Associate''s degree (i.e. AA, AS)', 3),
(189, 'Bachelor''s degree (i.e. BA, BS)', 4),
(189, 'Graduate degree (i.e. MSW, MBA)', 5),
(189, 'Doctoral degree (i.e. PhD, EdD)', 6),
(189, 'Professional degree (i.e. MD, DDS)', 7);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(190, 'Unspecified', 0),
(190, 'Very good', 1),
(190, 'Good', 2),
(190, 'Average', 3),
(190, 'Poor', 4),
(190, 'Very Poor', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(191, 'Unspecified', 0),
(191, 'General curiosity/interest in learning about my microbiome', 1),
(191, 'Desire to improve my health', 2),
(191, 'The study seemed fun and entertaining', 3),
(191, 'People in my family or social network have done it', 4),
(191, 'Professional interest in the microbiome', 5),
(191, 'Interest in contributing to science', 6),
(191, 'I have gastrointestinal problems', 7),
(191, 'I have other microbiome-relevant health problems', 8),
(191, 'Other', 9);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(192, 'Unspecified', 0),
(192, 'Crohn''s disease or Ulcerative Colitis', 1),
(192, 'Gastrointestinal cancer', 2),
(192, 'Frequent (more than once a week) diarrhea', 3),
(192, 'Frequent (more than once a week) constipation', 4),
(192, 'Irritable Bowel Syndrome (IBS)', 5),
(192, 'I have had surgery on my intestines', 6),
(192, 'Other', 7);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(193, 'Unspecified', 0),
(193, 'Yes', 1),
(193, 'Somewhat', 2),
(193, 'No', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(194, 'Unspecified', 0),
(194, 'Yes', 1),
(194, 'Somewhat', 2),
(194, 'No', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(195, 'Unspecified', 0),
(195, 'Yes', 1),
(195, 'No', 2),
(195, 'No, but I plan to make changes in the future', 3);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(196, 'Unspecified', 0),
(196, 'Change in diet (i.e. taking a probiotic)', 1),
(196, 'Change in exercise', 2),
(196, 'Change in alcohol or tobacco use (i.e. starting, stopping, or changing amount consumed)', 3),
(196, 'Change in use of nutritional supplements or vitamins', 4),
(196, 'Change in physical environment (i.e. adopting or getting rid of a pet, cleaning more or less often)', 5),
(196, 'Other', 6);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(197, 'Unspecified', 0),
(197, 'Significantly less concerned about your health', 1),
(197, 'Somewhat less concerned about your health', 2),
(197, 'As concerned about your health now as you were prior to receiving your results (the results didn''t affect how I view my health)', 3),
(197, 'Somewhat more concerned about your health', 4),
(197, 'Significantly more concerned about your health', 5);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(198, 'Unspecified', 0),
(198, 'Yes', 1),
(198, 'No', 2),
(198, 'No, but I plan to discuss my results with someone else in the future', 3);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(199, 'Unspecified', 0),
(199, 'Primary care physician', 1),
(199, 'Specialty physician (e.g., gastroenterologist)', 2),
(199, 'Nutritionist/dietician', 3),
(199, 'Other medical or health professional', 4),
(199, 'Family member(s)', 5),
(199, 'Friend(s)', 6),
(199, 'Colleague(s)', 7),
(199, 'Posted/discussed on social networking site (i.e. Facebook)', 8),
(199, 'Posted/discussed on an online patient/health platform (i.e. PatientsLikeMe)', 9),
(199, 'Posted/discussed on data sharing platform (i.e. Open Humans)', 10),
(199, 'Other', 11);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(200, 'Unspecified', 0),
(200, 'Very willing/enthusiastic', 1),
(200, 'Willing', 2),
(200, 'Neutral', 3),
(200, 'Not willing', 4),
(200, 'Very unwilling', 5);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(201, 'Unspecified', 0),
(201, 'Yes', 1),
(201, 'No', 2);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(202, 'Unspecified', 0),
(202, 'Ordered additional labs, tests, or procedures', 1),
(202, 'Change in medication (i.e. starting, stopping, or changing the dose of a prescription)', 2),
(202, 'Change in behavioral/lifestyle recommendations (e.g., start probiotic)', 3),
(202, 'Referral to a specialist (e.g., gastroenterologist)', 4),
(202, 'Other', 5);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(203, 'Unspecified', 0),
(203, 'Yes', 1),
(203, 'Somewhat', 2),
(203, 'No', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(204, 'Unspecified', 0),
(204, 'Yes', 1),
(204, 'No', 2);

----------------------------------------------------------
-- survey_question_triggers
----------------------------------------------------------
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (195, 196, 'Yes');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (198, 199, 'Yes');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (201, 202, 'Yes');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (204, 205, 'Yes');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (204, 206, 'Yes');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (204, 207, 'Yes');
