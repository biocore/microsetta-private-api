-- Add an Address 2 field to the account table
ALTER TABLE ag.account ADD COLUMN street2 VARCHAR;

-- Add a column to store whether the user agreed to the privacy policy and terms upon signup.
ALTER TABLE ag.account ADD COLUMN consent_privacy_terms BOOLEAN DEFAULT FALSE NOT NULL;

-- Add an assent_id to the consent_audit table for the 7-12 and 13-17 age groups. It needs to remain nullable as not all age groups have an assent document.
ALTER TABLE ag.consent_audit ADD COLUMN assent_id UUID,
    ADD CONSTRAINT fk_assent_id FOREIGN KEY (assent_id) REFERENCES ag.consent_documents (consent_id);

-- Add a foreign key for vioscreen registration codes
ALTER TABLE ag.vioscreen_registry ADD CONSTRAINT fk_registration_code FOREIGN KEY (registration_code) REFERENCES campaign.ffq_registration_codes (ffq_registration_code);

-- Add date_revoked field to ag.consent_audit
ALTER TABLE ag.consent_audit ADD COLUMN date_revoked TIMESTAMP WITH TIME ZONE;

-- Create the Other survey
INSERT INTO ag.survey_group (group_order, american) VALUES (-22, 'Other');
INSERT INTO ag.surveys (survey_id, survey_group) VALUES (22, -22);

-- Move the "Tell us anything else" question into the Other category
UPDATE ag.group_questions SET survey_group = -22, display_index = 0 WHERE survey_group = -10 AND survey_question_id = 116;

-- Move the migraine-related questions from the Migraines survey into the Health Diagnoses survey as triggered questions
UPDATE ag.survey_question SET retired = TRUE WHERE survey_question_id = 486;
INSERT INTO ag.survey_question (survey_question_id, american, question_shortname, retired) VALUES
    (511, 'For questions 11b - 11i, rank the listed factor based on how likely it is to lead to your migraines, where "1" is most likely, "2" is second most likely, etc. If the factor does not cause migraines, choose N/A.<br /><br />Stress', 'MIGRAINE_FACTORS_STRESS', FALSE),
    (512, 'Caffeine', 'MIGRAINE_FACTORS_CAFFEINE', FALSE),
    (513, 'Depression', 'MIGRAINE_FACTORS_DEPRESSION', FALSE),
    (514, 'Lack of sleep', 'MIGRAINE_FACTORS_LACKOFSLEEP', FALSE),
    (515, 'Foods (wine, chocolate, strawberries)', 'MIGRAINE_FACTORS_FOODS', FALSE),
    (516, 'Medications that contain barbituates or opioids', 'MIGRAINE_FACTORS_MEDICATIONS', FALSE),
    (517, 'Nitrates', 'MIGRAINE_FACTORS_NITRATES', FALSE),
    (518, 'Hormones', 'MIGRAINE_FACTORS_HORMONES', FALSE);
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type) VALUES
    (511, 'SINGLE'),
    (512, 'SINGLE'),
    (513, 'SINGLE'),
    (514, 'SINGLE'),
    (515, 'SINGLE'),
    (516, 'SINGLE'),
    (517, 'SINGLE'),
    (518, 'SINGLE');
INSERT INTO ag.survey_response (american) VALUES ('N/A');

INSERT INTO ag.survey_question_response(survey_question_id, response, display_index) VALUES
    (511, 'Unspecified', 0),
    (511, '1', 1),
    (511, '2', 2),
    (511, '3', 3),
    (511, '4', 4),
    (511, '5', 5),
    (511, '6', 6),
    (511, '7', 7),
    (511, '8', 8),
    (511, 'N/A', 9),
    (512, 'Unspecified', 0),
    (512, '1', 1),
    (512, '2', 2),
    (512, '3', 3),
    (512, '4', 4),
    (512, '5', 5),
    (512, '6', 6),
    (512, '7', 7),
    (512, '8', 8),
    (512, 'N/A', 9),
    (513, 'Unspecified', 0),
    (513, '1', 1),
    (513, '2', 2),
    (513, '3', 3),
    (513, '4', 4),
    (513, '5', 5),
    (513, '6', 6),
    (513, '7', 7),
    (513, '8', 8),
    (513, 'N/A', 9),
    (514, 'Unspecified', 0),
    (514, '1', 1),
    (514, '2', 2),
    (514, '3', 3),
    (514, '4', 4),
    (514, '5', 5),
    (514, '6', 6),
    (514, '7', 7),
    (514, '8', 8),
    (514, 'N/A', 9),
    (515, 'Unspecified', 0),
    (515, '1', 1),
    (515, '2', 2),
    (515, '3', 3),
    (515, '4', 4),
    (515, '5', 5),
    (515, '6', 6),
    (515, '7', 7),
    (515, '8', 8),
    (515, 'N/A', 9),
    (516, 'Unspecified', 0),
    (516, '1', 1),
    (516, '2', 2),
    (516, '3', 3),
    (516, '4', 4),
    (516, '5', 5),
    (516, '6', 6),
    (516, '7', 7),
    (516, '8', 8),
    (516, 'N/A', 9),
    (517, 'Unspecified', 0),
    (517, '1', 1),
    (517, '2', 2),
    (517, '3', 3),
    (517, '4', 4),
    (517, '5', 5),
    (517, '6', 6),
    (517, '7', 7),
    (517, '8', 8),
    (517, 'N/A', 9),
    (518, 'Unspecified', 0),
    (518, '1', 1),
    (518, '2', 2),
    (518, '3', 3),
    (518, '4', 4),
    (518, '5', 5),
    (518, '6', 6),
    (518, '7', 7),
    (518, '8', 8),
    (518, 'N/A', 9);



UPDATE ag.group_questions SET display_index = 38 WHERE survey_group = -15 AND display_index = 25;
UPDATE ag.group_questions SET display_index = 37 WHERE survey_group = -15 AND display_index = 24;
UPDATE ag.group_questions SET display_index = 36 WHERE survey_group = -15 AND display_index = 23;
UPDATE ag.group_questions SET display_index = 35 WHERE survey_group = -15 AND display_index = 22;
UPDATE ag.group_questions SET display_index = 34 WHERE survey_group = -15 AND display_index = 21;
UPDATE ag.group_questions SET display_index = 33 WHERE survey_group = -15 AND display_index = 20;
UPDATE ag.group_questions SET display_index = 32 WHERE survey_group = -15 AND display_index = 19;
UPDATE ag.group_questions SET display_index = 31 WHERE survey_group = -15 AND display_index = 18;
UPDATE ag.group_questions SET display_index = 30 WHERE survey_group = -15 AND display_index = 17;
UPDATE ag.group_questions SET display_index = 29 WHERE survey_group = -15 AND display_index = 16;
UPDATE ag.group_questions SET display_index = 28 WHERE survey_group = -15 AND display_index = 15;
UPDATE ag.group_questions SET display_index = 27 WHERE survey_group = -15 AND display_index = 14;

UPDATE ag.group_questions SET display_index = 14, survey_group = -15 WHERE survey_group = -19 AND survey_question_id = 485;
-- Leave a gap for the sub-questions of 486
UPDATE ag.group_questions SET display_index = 23, survey_group = -15 WHERE survey_group = -19 AND survey_question_id = 487;
UPDATE ag.group_questions SET display_index = 24, survey_group = -15 WHERE survey_group = -19 AND survey_question_id = 488;
UPDATE ag.group_questions SET display_index = 25, survey_group = -15 WHERE survey_group = -19 AND survey_question_id = 489;
UPDATE ag.group_questions SET display_index = 26, survey_group = -15 WHERE survey_group = -19 AND survey_question_id = 490;

INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES
    (-15, 511, 15),
    (-15, 512, 16),
    (-15, 513, 17),
    (-15, 514, 18),
    (-15, 515, 19),
    (-15, 516, 20),
    (-15, 517, 21),
    (-15, 518, 22);

INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 485),
    (92, 'Diagnosed by an alternative medicine practitioner', 485),
    (92, 'Self-diagnosed', 485),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 487),
    (92, 'Diagnosed by an alternative medicine practitioner', 487),
    (92, 'Self-diagnosed', 487),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 488),
    (92, 'Diagnosed by an alternative medicine practitioner', 488),
    (92, 'Self-diagnosed', 488),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 489),
    (92, 'Diagnosed by an alternative medicine practitioner', 489),
    (92, 'Self-diagnosed', 489),
    (489, 'Yes', 490),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 511),
    (92, 'Diagnosed by an alternative medicine practitioner', 511),
    (92, 'Self-diagnosed', 511),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 512),
    (92, 'Diagnosed by an alternative medicine practitioner', 512),
    (92, 'Self-diagnosed', 512),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 513),
    (92, 'Diagnosed by an alternative medicine practitioner', 513),
    (92, 'Self-diagnosed', 513),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 514),
    (92, 'Diagnosed by an alternative medicine practitioner', 514),
    (92, 'Self-diagnosed', 514),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 515),
    (92, 'Diagnosed by an alternative medicine practitioner', 515),
    (92, 'Self-diagnosed', 515),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 516),
    (92, 'Diagnosed by an alternative medicine practitioner', 516),
    (92, 'Self-diagnosed', 516),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 517),
    (92, 'Diagnosed by an alternative medicine practitioner', 517),
    (92, 'Self-diagnosed', 517),
    (92, 'Diagnosed by a medical professional (doctor, physician assistant)', 518),
    (92, 'Diagnosed by an alternative medicine practitioner', 518),
    (92, 'Self-diagnosed', 518);

-- Retire the Migraines survey
UPDATE ag.surveys SET retired = TRUE where survey_id = 19;

-- Create a slot for the Weight Units question directly after Weight
UPDATE ag.group_questions SET display_index = 93 WHERE survey_group = -10 AND display_index = 92;
UPDATE ag.group_questions SET display_index = 92 WHERE survey_group = -10 AND display_index = 91;
UPDATE ag.group_questions SET display_index = 91 WHERE survey_group = -10 AND display_index = 90;
UPDATE ag.group_questions SET display_index = 90 WHERE survey_group = -10 AND display_index = 89;
UPDATE ag.group_questions SET display_index = 89 WHERE survey_group = -10 AND display_index = 88;
UPDATE ag.group_questions SET display_index = 88 WHERE survey_group = -10 AND display_index = 87;

-- Unretire the Weight Units question
UPDATE ag.group_questions SET display_index = 87 WHERE survey_group = -10 AND survey_question_id = 114;
UPDATE ag.survey_question SET retired = FALSE WHERE survey_question_id = 114;

-- Adjust various questions
DELETE FROM ag.survey_question_response WHERE survey_question_id = 502 AND response = 'Other';
UPDATE ag.survey_question_response SET display_index = 3 WHERE survey_question_id = 502 AND response = 'Not sure';
UPDATE ag.survey_question_response_type SET survey_response_type = 'STRING' WHERE survey_question_id = 150;
DELETE FROM ag.survey_question_response WHERE survey_question_id = 486;
UPDATE ag.survey_question SET american = 'What date were you diagnosed?' WHERE survey_question_id = 213;
UPDATE ag.survey_question SET retired = TRUE WHERE survey_question_id = 215;
UPDATE ag.survey_question SET american = 'At home, what is the main source of your plain, unflavored drinking water? This can include still or sparkling/carbonated water. *In the options below, "bottled" includes bottles, jugs, water coolers or water dispensers.' WHERE survey_question_id = 474;
UPDATE ag.survey_question SET american = 'When you''re outside the home, what is the main source of your plain unflavored drinking water? This can include still or sparkling/carbonated water. *In the options below, "bottled" includes bottles, jugs, water coolers or water dispensers.' WHERE survey_question_id = 476;
UPDATE ag.survey_question SET american = 'If you answered "yes" to consuming beverages and/or foods containing non-nutritive or low-calorie sweeteners, what type of non-nutritive or low-calorie sweetner(s) do you consume on a regular basis? Select all that apply.' WHERE survey_question_id = 464;
UPDATE ag.survey_question_response_type SET survey_response_type = 'MULTIPLE' WHERE survey_question_id = 505;
UPDATE ag.survey_question_response_type SET survey_response_type = 'MULTIPLE' WHERE survey_question_id = 487;
UPDATE ag.survey_question SET american = 'On nights before you have school or work, what time do you go to bed?' WHERE survey_question_id = 345;
UPDATE ag.survey_question_response SET response = 'Some college or technical school' WHERE survey_question_id = 493 AND response = 'College degree';
INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES (54, 'None of the above', 5);
UPDATE ag.survey_question SET american = 'On your days off (when you do not have school or work), what time do you get up in the morning?' WHERE survey_question_id = 346;
UPDATE ag.survey_question SET american = 'On your days off (when you do not have school or work), what time do you go to bed?' WHERE survey_question_id = 347;
UPDATE ag.survey_question_response SET response = 'Other' WHERE survey_question_id = 474 AND display_index = 9;
INSERT INTO ag.survey_question (survey_question_id, american, question_shortname, retired) VALUES
    (519, 'Please describe your main source of water at home:', 'WATER_AT_HOME_OTHER', FALSE),
    (520, 'Please describe your main source of water outside the home:', 'WATER_OUTSIDE_HOME_OTHER', FALSE);
INSERT INTO ag.survey_question_response_type (survey_question_id, survey_response_type) VALUES
    (519, 'STRING'),
    (520, 'STRING');

UPDATE ag.group_questions SET display_index = 48 WHERE survey_group = -18 AND display_index = 46;
UPDATE ag.group_questions SET display_index = 47 WHERE survey_group = -18 AND display_index = 45;
UPDATE ag.group_questions SET display_index = 46 WHERE survey_group = -18 AND display_index = 44;
UPDATE ag.group_questions SET display_index = 45 WHERE survey_group = -18 AND display_index = 43;
UPDATE ag.group_questions SET display_index = 44 WHERE survey_group = -18 AND display_index = 42;
UPDATE ag.group_questions SET display_index = 43 WHERE survey_group = -18 AND display_index = 41;
UPDATE ag.group_questions SET display_index = 42 WHERE survey_group = -18 AND display_index = 40;
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (-18, 520, 41);
UPDATE ag.group_questions SET display_index = 40 WHERE survey_group = -18 AND display_index = 39;
UPDATE ag.group_questions SET display_index = 39 WHERE survey_group = -18 AND display_index = 38;
INSERT INTO ag.group_questions (survey_group, survey_question_id, display_index) VALUES (-18, 519, 38);
UPDATE ag.survey_question SET american = 'Describe the consistency of your bowel movements:<br /><div class="bristol-img-container"><img src="/static/img/bristol_1.png" id="bristol-chart-1" /></div><span class="bristol-chart-text">Type 1: Separate hard lumps, like nuts (hard to pass).<br />Type 2: Sausage shaped but lumpy.</span><div class="bristol-img-container"><img src="/static/img/bristol_2.png" id="bristol-chart-2" /></div><span class="bristol-chart-text">Type 3: Like a sausage but with cracks on the surface.<br />Type 4: Like a sausage or snake - smooth and soft.</span><div class="bristol-img-container"><img src="/static/img/bristol_3.png" id="bristol-chart-3" /></div><span class="bristol-chart-text">Type 5: Soft blobs with clear-cut edges.<br />Type 6: Fluffy pieces with ragged edges; a mushy stool.<br />Type 7: Watery, no solid pieces. Entirely liquid.</span>' WHERE survey_question_id = 38;

-- Two of the responses for this question need to be reordered. Since there's a unique constraint on display_index, playing musical chairs with the entries (which requires updating one of the entries twice) is more expedient than dropping and recreating the index.
UPDATE ag.survey_question_response SET display_index = 5 WHERE survey_question_id = 38 AND response = 'I tend to have diarrhea (watery stool) - Type 5, 6 and 7';
UPDATE ag.survey_question_response SET display_index = 2 WHERE survey_question_id = 38 AND response = 'I tend to have normal formed stool - Type 3 and 4';
UPDATE ag.survey_question_response SET display_index = 3 WHERE survey_question_id = 38 AND response = 'I tend to have diarrhea (watery stool) - Type 5, 6 and 7';

-- Fix triggers for various questions
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (17, 'Two', 18);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (17, 'Three', 18);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (17, 'More than three', 18);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (20, 'Yes', 501);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (21, 'Yes', 503);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Regularly (3-5 times/week)', 25);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Regularly (3-5 times/week)', 331);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Regularly (3-5 times/week)', 332);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Occasionally (1-2 times/week)', 25);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Occasionally (1-2 times/week)', 331);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Occasionally (1-2 times/week)', 332);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Rarely (a few times/month)', 25);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Rarely (a few times/month)', 331);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (24, 'Rarely (a few times/month)', 332);
UPDATE ag.survey_question_triggers SET triggered_question = 494 WHERE triggered_question = 30;
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (29, 'Rarely (a few times/month)', 494);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (83, 'Diagnosed by a medical professional (doctor, physician assistant)', 360);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (83, 'Diagnosed by an alternative medicine practitioner', 360);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (83, 'Self-diagnosed', 360);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (42, 'Yes', 370);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (504, 'Yes, diagnosed by a licensed mental health professional', 505);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (504, 'Yes, diagnosed by an alternative or complementary practitioner', 505);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (504, 'Self-diagnosed', 505);
DELETE FROM ag.survey_question_triggers WHERE survey_question_id = 82;
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (82, 'Diagnosed by a medical professional (doctor, physician assistant)', 506);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (82, 'Diagnosed by an alternative medicine practitioner', 506);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (507, 'Yes, diagnosed by a medical professional (doctor, physician assistant)', 407);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (507, 'Yes, diagnosed by a medical professional (doctor, physician assistant)', 408);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (507, 'Yes, diagnosed by a medical professional (doctor, physician assistant)', 409);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (507, 'Yes, diagnosed by a medical professional (doctor, physician assistant)', 410);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Rarely (a few times/month)', 462);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Occasionally (1-2 times/week)', 462);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Regularly (3-5 times/week)', 462);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Daily', 462);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Rarely (a few times/month)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Occasionally (1-2 times/week)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Regularly (3-5 times/week)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (157, 'Daily', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (463, 'Rarely (a few times/month)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (463, 'Occasionally (1-2 times/week)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (463, 'Regularly (3-5 times/week)', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (463, 'Daily', 464);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Rarely (a few times/month)', 167);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Occasionally (1-2 times/week)', 167);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Regularly (3-5 times/week)', 167);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Daily', 167);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Rarely (a few times/month)', 169);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Occasionally (1-2 times/week)', 169);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Regularly (3-5 times/week)', 169);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Daily', 169);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Rarely (a few times/month)', 171);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Occasionally (1-2 times/week)', 171);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Regularly (3-5 times/week)', 171);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (165, 'Daily', 171);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (212, 'Yes, with a positive test', 213);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (212, 'Yes, medical diagnosis, but no test', 213);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (474, 'Other', 519);
INSERT INTO ag.survey_question_triggers (survey_question_id, triggering_response, triggered_question) VALUES (476, 'Other', 520);


-- Add column for CSS classes to survey questions table
ALTER TABLE ag.survey_question ADD COLUMN css_classes VARCHAR;

-- Set the CSS classes for questions
-- Basic Info survey
UPDATE ag.survey_question SET css_classes = 'tmi-survey-select col-12 col-md-3' WHERE survey_question_id IN (111,112);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal col-12 col-md-6' WHERE survey_question_id IN (502);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text col-6 col-md-2' WHERE survey_question_id IN (108,113);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-switch col-6 col-md-4' WHERE survey_question_id IN (109,114);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-select col-12 col-md-4' WHERE survey_question_id IN (110, 148);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text col-12 col-md-4' WHERE survey_question_id IN (115);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (22, 492, 493);

-- At Home survey
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (313, 15, 17);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (19, 20, 21, 149, 326);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (316, 508, 319, 150);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal tmi-survey-triggered-question' WHERE survey_question_id IN (509, 510, 18);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (501, 503);


-- Lifestyle survey
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (16, 495, 34, 35, 350);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox' WHERE survey_question_id IN (328);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (24, 333, 334, 28, 29, 32, 33, 27);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (25, 163);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox tmi-survey-triggered-question' WHERE survey_question_id IN (331, 332, 494);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-select' WHERE survey_question_id IN (344, 345, 346, 347);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (348, 349, 36, 26, 354);

-- Gut survey
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (37, 38);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-buttons' WHERE survey_question_id IN (95, 79, 83, 78);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (360);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (362, 363, 364, 365);

-- General health survey
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (50, 42, 500, 47, 48, 49, 44, 45, 46);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (51, 497, 43, 39, 40);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (374, 375);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (370);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (156);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-textarea tmi-survey-triggered-question' WHERE survey_question_id IN (99, 124, 126);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal-stacked' WHERE survey_question_id IN (387);

-- Health Diagnosis
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-buttons' WHERE survey_question_id IN (85, 84, 93, 77, 87, 80, 89, 504, 82, 90, 92, 60, 86, 94, 96);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox tmi-survey-triggered-question' WHERE survey_question_id IN (505, 487, 409, 410);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (506, 485, 413);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal tmi-survey-triggered-question' WHERE survey_question_id IN (488, 489, 408);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis tmi-survey-triggered-question' WHERE survey_question_id IN (511, 512, 513, 514, 515, 516, 517, 518);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (490, 407);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (507, 499);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-textarea tmi-survey-triggered-question' WHERE survey_question_id IN (106);

-- Allergies
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (53, 7);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (8);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (415);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox' WHERE survey_question_id IN (54, 9);

-- Diet
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (1, 423, 425, 426, 427);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox' WHERE survey_question_id IN (162, 433);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (11, 2, 6, 498);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-textarea' WHERE survey_question_id IN (424);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-select' WHERE survey_question_id IN (428);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (3, 4, 5);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis tmi-survey-triggered-question' WHERE survey_question_id IN (434);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-textarea tmi-survey-triggered-question' WHERE survey_question_id IN (104);

-- Detailed Diet
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (56, 57, 58, 59, 91, 443, 61, 62, 236, 237, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 157, 463, 239, 240, 241, 242, 243, 244, 76, 165);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (146, 474, 476, 478, 166);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical tmi-survey-triggered-question' WHERE survey_question_id IN (462);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox tmi-survey-triggered-question' WHERE survey_question_id IN (464, 466, 167, 169, 171);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal tmi-survey-triggered-question' WHERE survey_question_id IN (465);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (475, 477);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (519, 520);

-- COVID-19
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text' WHERE survey_question_id IN (209);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-axis' WHERE survey_question_id IN (210, 221, 222, 223, 224, 229, 230, 231, 232, 233, 234, 235);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-checkbox' WHERE survey_question_id IN (211, 214, 217, 238, 220);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-vertical' WHERE survey_question_id IN (212, 218, 228);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-text tmi-survey-triggered-question' WHERE survey_question_id IN (213);
UPDATE ag.survey_question SET css_classes = 'tmi-survey-radio-horizontal' WHERE survey_question_id IN (216, 219, 225, 226, 227);

-- Other
UPDATE ag.survey_question SET css_classes = 'tmi-survey-textarea' WHERE survey_question_id IN (116);

-- Fix consent documents
-- No one has actually agreed to the new docs yet, so we can safely update rather than creating a new version
UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
  You do not have to participate. Your participation in this study is completely voluntary. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  You can refuse to participate or withdraw at any time by withdrawing your consent and deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you.
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
  What about your confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law.  As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
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
</p>' WHERE consent_type = 'adolescent_biospecimen' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
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
  Participation in this study can involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
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
  The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in our <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Privacy Statement</a>.
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
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>' WHERE consent_type = 'adolescent_data' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Consent to Act as a Research Subject
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative</strong><br />
  Biospecimen and Future Use Research
</p>
<p class="consent_header">
  Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
  Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called your microbiome) that live in and on your body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You have been asked to participate in this study because your microbiome is unique - not the same as anyone else''s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
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
  You do not have to participate. Your participation in this study is completely voluntary. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  You can refuse to participate or withdraw at any time by withdrawing your consent and deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you.
</p>
<p class="consent_content">
  You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no monetary or direct benefit for participating in this study. You will receive a report detailing the results of our analysis on your biospecimen(s), as well as facts and figures comparing your microbiome''s composition to that of other study participants.
</p>
<p class="consent_header">
  Are there any costs associated with participating in the collection of your biospecimen(s)?
</p>
<p class="consent_content">
  There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure.
</p>
<p class="consent_header">
  What about your confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law. As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  How we will use your Sample
</p>
<p class="consent_content">
  Information from analyses of your data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
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
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research and have your sample(s) processed.
</p>' WHERE consent_type = 'adult_biospecimen' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
  You are being invited to participate in a research study titled The Microsetta Initiative. This study is being done by Dr. Rob Knight from the University of California - San Diego (UCSD). You were selected to participate in this study because you are unique and your microbiome is unique - not the same as anyone else''s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
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
  Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
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
  The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in our <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Privacy Statement</a>.
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
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>' WHERE consent_type = 'adult_data' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
  (Ages 7-12 years)
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative (a study about microbes)</strong>
</p>
<p class="consent_content">
  Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something (like the virus that causes COVID-19) but we can''t tell you that because we are not allowed to do that.
</p>
<p class="consent_content">
  If you decide you want to be in this research study, this is what will happen to you:
</p>
<p class="consent_content">
  We will ask you or your mom or dad to sample some place on your body (like skin or mouth) or your poop (from toilet paper) with something that looks like 2 Q-tips.  Sometimes we need more poop for our research and then we will ask you to poop into a plastic bowl that is under the seat of the toilet and catches the poop as it comes out.  Your mom or dad will send it to us in the bowl. We may also ask your mom or dad to prick your finger so that we can get a little bit of your blood.
</p>
<p class="consent_content">
  Sometimes kids don''t feel good while being in this study. You might feel a little bit sore if your skin is rubbed with the Q-tip and temporary pain if they prick your finger to get blood. Most people don''t mind these feelings.
</p>
<p class="consent_content">
  If you feel any of these things, or other things, be sure to tell your mom or dad.
</p>
<p class="consent_content">
  You don''t have to be in this research study if you don''t want to. Nobody will be mad at you if you say no. Even if you say yes now and change your mind after you start doing this study, you can stop and no one will be mad.
</p>
<p class="consent_content">
  Be sure to ask your parents if you have questions.  You can also ask them to call Dr. Knight or his research team so they can tell you more about anything you don''t understand.
</p>' WHERE consent_type = 'child_biospecimen' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego</strong><br />
  Assent to Act as a Research Subject<br />
  (Ages 7-12 years)
</p>
<p class="consent_title">
  The Microsetta Initiative (a study about microbes)
</p>
<p class="consent_content">
  Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something (like the virus that causes COVID-19) but we can''t tell you that because we are not allowed to do that.
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
  Sometimes kids don''t feel good while being in this study. You might feel a little tired, bored, or uncomfortable. Most people don''t mind these feelings.
</p>
<p class="consent_content">
  If you feel any of these things, or other things, be sure to tell your mom or dad.
</p>
<p class="consent_content">
  You don''t have to be in this research study if you don''t want to. Nobody will be mad at you if you say no. Even if you say yes now and change your mind after you start doing this study, you can stop and no one will be mad.
</p>
<p class="consent_content">
  Be sure to ask your parents if you have questions.  You can also ask them to call Dr. Knight or his research team so they can tell you more about anything you don''t understand.
</p>' WHERE consent_type = 'child_data' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
  The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your child''s information and biospecimens for the purpose of processing your child''s biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about the child participant supplying the sample. Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What will happen to your child in this study?
</p>
<p class="consent_content">
  If you agree to the collection and processing of your child''s biospecimen(s), the following will happen to your child:
</p>
<p class="consent_content">
  You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.
</p>
<p class="consent_content">
  You will sample a part of your child''s body (e.g. feces, skin, mouth, nostril, ear, vagina) as described in the kit instructions. You will also be asked to provide general collection information such as the date and time your child''s sample was collected. All samples should be returned to us in the included containers according to the instructions provided.
</p>
<p class="consent_content">
  If collecting from your child''s stool, you will be asked to sample in one of a variety of ways, such as the following:
  <ol>
    <li>By inserting swab tips into used toilet tissue or diaper and returning the sample in the provided plastic container;</li>
    <li>By inserting swab tips into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
    <li>By using a scooper device to scoop a part of the fecal material into the provided tube;</li>
    <li>Depositing soiled toilet paper into the provided receptacle;</li>
    <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celcius/-4 degrees Fahrenheit.</li>
  </ol>
</p>
<p class="consent_content">
  If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your child''s finger.
</p>
<p class="consent_content">
  Once your child''s sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them. We estimate that it can take 1-3 months for you to learn the results of your child''s microbiome analysis. If your child is a part of a specific sub-study, it may take longer, depending on the duration of the study.
</p>
<p class="consent_header">
  How much time will each study procedure take, what is your child''s total time commitment, and how long will the study last?
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
  Participation in research is entirely voluntary. You may refuse to have your child participate or withdraw your child at any time without penalty or loss of benefits to which you or your child are entitled. If you decide that you no longer wish your child to continue in this study, you may withdraw your consent by requesting the deletion of your child''s profile through your online account. We will inform you and your child if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
  Your child may be withdrawn from the study if the instructions given to you by the study personnel are not followed.
</p>
<p class="consent_header">
  What benefits can be reasonably expected?
</p>
<p class="consent_content">
  There is no direct benefit to your child for participating in this study. You will receive a report detailing the results of our analysis on your child''s sample, as well as facts and figures comparing your child''s microbial composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
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
  What about your or your child''s confidentiality?
</p>
<p class="consent_content">
  Research records will be kept confidential to the extent allowed by law. As part of your child''s participation in the study, you or your child will provide personal and/or sensitive information that could allow your child to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you or your child provide are stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
  How we will use your child''s Sample
</p>
<p class="consent_content">
  Information from analyses of your child''s data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including your child''s) may be analyzed and published in scientific articles. We may save some of your child''s sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your child''s data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your child''s sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
  Biospecimens (such as stool, skin, urine, or blood) collected from your child for this study and information obtained from your child''s biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your child''s biospecimens and/or information obtained from them.
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
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your child''s ability to participate in this research and have your child''s sample(s) processed.
</p>' WHERE consent_type = 'parent_biospecimen' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
  There is no direct benefit to your child for participating in this study.  If you complete one of the questionnaires called Food Frequency Questionnaire (FFQ) for your child, you may receive a nutritional report evaluating your child''s eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.
</p>
<p class="consent_header">
  What risks are associated with this study?
</p>
<p class="consent_content">
  Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you or your child may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you or your child provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The code will be destroyed by deletion from the server at the end of the study or if you withdraw from the study. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
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
  Participation in this study is completely voluntary and you or your child can withdraw at any time by simply exiting the survey, withdrawing consent and deleting your child''s online profile, or by requesting the deletion of your online account. You are free to skip any question that you choose.
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
  As part of this research study, we will create and obtain information related to you or your child''s participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
  How we will use your child''s Personal Data
</p>
<p class="consent_content">
  The Personal Data you provide will be used for the following purposes:
  <ul>
    <li>To share with members of the research team so they can properly conduct the research.</li>
    <li>For future research studies or additional research by other researchers.</li>
    <li>To contact you for the purpose of receiving alerts of your child''s participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
    <li>To confirm proper conduct of the study and research integrity.</li>
  </ul>
</p>
<p class="consent_header">
  Retention of your child''s Personal Data
</p>
<p class="consent_content">
  We may retain the Personal Data you provide for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your child''s Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your child''s information will be retained as necessary to comply with legal or regulatory requirements.
</p>
<p class="consent_header">
  Your Privacy Rights
</p>
<p class="consent_content">
  The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your child''s Personal Data, including the right to access, correct, restrict, and withdraw your child''s personal information.
</p>
<p class="consent_content">
  The research team will store and process your child''s Personal Data at our research site in the United States. The United States does not have the same laws to protect your child''s Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your child''s Study Data. Additional information about the protections we will use is included in our <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Privacy Statement</a>.
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
  You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
  Your consent is entirely voluntary, but declining to provide it may impede your child''s ability to participate in this research.
</p>' WHERE consent_type = 'parent_data' AND locale = 'en_US';

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespecímenes e investigación de uso futuro</strong>
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
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué le sucederá en este estudio y qué procedimientos son el estándar de atención y cuáles son experimentales?
</p>
<p class="consent_content">
  Si usted acepta participar en este estudio, le ocurrirá lo siguiente:
</p>
<p class="consent_content">
  Usted mismo tomará la muestra usando el kit que se le proporcionó. Las instrucciones están incluidas en el kit para que sepa qué hacer. La muestra más común es de heces (fecal) donde se recoge una pequeña muestra insertando las puntas de un hisopo en el papel higiénico usado o en una tarjeta (tarjeta llamada FOBT). También se le puede pedir que saque un trozo de materia fecal con una pequeña herramienta similar a una cuchara, que coloque papel higiénico usado en un receptáculo especial que le proporcionaremos o que defeque en un recipiente de plástico que se coloca debajo del asiento del baño. También es posible que deba tomar muestras de una pequeña área de la piel, la lengua o la boca, las fosas nasales, la cera del oído o la vagina. También podemos pedirle a alguien (como su mamá o papá) que tome una pequeña muestra de sangre pinchando su dedo y luego recolectando la sangre en 2 hisopos pequeños. Ninguna de estas muestras o investigaciones nos permitirá hacer un diagnóstico de enfermedad y no estamos buscando nada en su propio ADN que también se pueda encontrar en sus heces, piel o saliva.
</p>
<p class="consent_header">
  ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
  Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
    <li>Existe el riesgo de pérdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ningún beneficio directo para usted por participar en este estudio. Usted tendrá acceso a sus datos que le darán a usted y a sus padres una idea de lo que hay en su muestra y cómo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
  ¿Se le pagará por participar en este estudio?
</p>
<p class="consent_content">
  Usted  no recibirá ninguna remuneración económica por participar en este estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo vinculado con la participación en la colección de su(s) muestra(s) biológica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  ¿Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. El código (que vincula los datos personales del participante con los códigos de barras de la muestras) se guarda en otro servidor protegido con contraseña, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  Cómo usaremos su Muestra
</p>
<p class="consent_content">
  La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong><br />
  Tenga en cuenta que <strong>no se analizará ADN humano</strong> como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
</p>
<p class="consent_header">
  ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
  Si tiene alguna duda o problemas relacionados con la investigación, usted puede comunicarse con nosotros enviando un correo electrónico a nuestra cuenta de ayuda microsetta@ucsd.edu o  llamando a Rob Knight al 858-246-1184.
</p>
<p class="consent_content">
  Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar  problemas relacionados con la investigación.
</p>
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>' WHERE consent_type = 'adolescent_biospecimen' AND locale IN ('es_MX', 'es_ES');

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
  <strong>University of California, San Diego<br />
    Consentimiento para participar como sujeto de investigación</strong>
</p>
<p class="consent_title">
  <strong>The Microsetta Initiative<br />
    Bioespecímenes e investigación de uso futuro</strong>
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
  El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
  ¿Qué le sucederá durante el estudio?
</p>
<p class="consent_content">
  Si acepta la recolección y el procesamiento de su(s) muestra(s) biológica(s), le ocurrirá lo siguiente:
</p>
<p class="consent_content">
  Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa. Luego, recolectará una muestra de usted mismo (por ejemplo, heces, piel, boca, orificio nasal, oído, vagina), mascota o entorno, como se describe en las instrucciones del kit o en las instrucciones que le proporcionaron los coordinadores del estudio. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó su muestra. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
  Si se recolecta muestra de heces, se le pedirá que tome muestras en una variedad de formas, como las siguientes:
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
  Una vez que se haya analizado su muestra, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Calculamos que puede tardar de 1 a 3 meses en conocer los resultados de su análisis del microbioma. Si forma parte de un subestudio específico, puede llevar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
  ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
  Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
  ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
  La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
  <ol>
    <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
    <li>Existe el riesgo de pérdida de confidencialidad.</li>
  </ol>
</p>
<p class="consent_content">
  Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
  ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
  No tiene que participar. Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento retirando su consentimiento y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
  Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
  ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
  No hay ningún beneficio monetario o directo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis en su(s) muestra(s) biológica(s), así como datos y cifras que comparan la composición de su microbioma con la de otros participantes del estudio.
</p>
<p class="consent_header">
  ¿Hay algún costo vinculado con la participación en la colección de su(s) muestra(s) biológica(s)?
</p>
<p class="consent_content">
  Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
  ¿Y su confidencialidad?
</p>
<p class="consent_content">
  Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. El código (que vincula los datos personales del participante con los códigos de barras de la muestras) se guarda en otro servidor protegido con contraseña, al que solo pueden acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y muestras, el administrador de TI y los programadores de la base de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
  Cómo usaremos su Muestra
</p>
<p class="consent_content">
  La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
  Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
  <strong><u>Tenga en cuenta:</u></strong> <br />
  Tenga en cuenta que <strong>no se analizará ADN humano</strong> como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra <strong>no pueden usarse para diagnosticar enfermedades o infecciones</strong>.
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
<p class="consent_header">
  Firma y Consentimiento
</p>
<p class="consent_content">
  Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
  Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación y procesar su(s) muestra(s).
</p>' WHERE consent_type = 'adult_biospecimen' AND locale IN ('es_MX', 'es_ES');

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
</p>' WHERE consent_type = 'adult_data' AND locale IN ('es_MX', 'es_ES');

UPDATE ag.consent_documents SET consent_content = '<p class="consent_title">
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
</p>' WHERE consent_type = 'parent_biospecimen' AND locale IN ('es_MX', 'es_ES');
