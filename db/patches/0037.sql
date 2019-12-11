-- May 31, 2016
-- Add surfer and fermeted foods questionnaires

----------------------------------------------------------
-- survey_group
----------------------------------------------------------
INSERT INTO survey_group (group_order, american, british) VALUES (-3, 'Fermented Foods', 'Fermented Foods');
INSERT INTO survey_group (group_order, american, british) VALUES (-4, 'Surfers', 'Surfers');

----------------------------------------------------------
-- surveys
----------------------------------------------------------
INSERT INTO surveys (survey_id, survey_group) VALUES (3, -3);
INSERT INTO surveys (survey_id, survey_group) VALUES (4, -4);

----------------------------------------------------------
-- survey_question
----------------------------------------------------------
-- Fermented
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(165, 'FERMENTED_FREQUENCY', 'How often do you consume one or more servings of fermented vegetables or plant products a day in an average week? (1 serving = 1/2 cup sauerkraut, kimchi or fermented vegetable or 1 cup of kombucha)', 'How often do you consume one or more servings of fermented vegetables or plant products a day in an average week? (1 serving = 1/2 cup sauerkraut, kimchi or fermented vegetable or 1 cup of kombucha)'),
(166, 'FERMENTED_INCREASED', 'Excluding beer, wine, and alcohol, I have significantly increased (i.e. more than doubled) my intake of fermented foods in frequency or quantity within the last ____.', 'Excluding beer, wine, and alcohol, I have significantly increased (i.e. more than doubled) my intake of fermented foods in frequency or quantity within the last ____.'),
(167, 'FERMENTED_CONSUMED', 'Which of the following fermented foods/beverages do you consume more than once a week? Check all that apply.', 'Which of the following fermented foods/beverages do you consume more than once a week? Check all that apply.'),
(168, 'FERMENTED_CONSUMED_OTHER', 'Write in any consumed foods that are not listed under "Other"', 'Write in any consumed foods that are not listed under "Other"'),
(169, 'FERMENTED_PRODUCE_PERSONAL', 'Do you produce any of the following fermented foods/beverages at home for personal consumption? Check all that apply.', 'Do you produce any of the following fermented foods/beverages at home for personal consumption? Check all that apply.'),
(170, 'FERMENTED_PRODUCE_PERSONAL_OTHER', 'Write in any presonally produced foods that are not listed under "Other"', 'Write in any presonally produced foods that are not listed under "Other"'),
(171, 'FERMENTED_PRODUCE_COMMERCIAL', 'Do you produce any of the following fermented foods/beverages for commercial purposes? Check all that apply.', 'Do you produce any of the following fermented foods/beverages for commercial purposes? Check all that apply.'),
(172, 'FERMENTED_PRODUCE_COMMERCIAL_OTHER', 'Write in any commercially produced foods that are not listed under "Other"', 'Write in any commercially produced foods that are not listed under "Other"'),
(173, 'FERMENTED_OTHER', 'Volunteer more information about this activity.', 'Volunteer more information about this activity.');
-- Surfers
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(174, 'SURF_LOCAL_BREAK', 'Where is your local surf break?', 'Where is your local surf break?'),
(175, 'SURF_LOAL_BREAK_FREQUENCY', 'How often do you surf your local wave?', 'How often do you surf your local wave?'),
(176, 'SURF_FREQUENCY', 'How often do you surf?', 'How often do you surf?'),
(177, 'SURF_TRAVEL_FREQUENCY', 'How often do you travel to other surf breaks?', 'How often do you travel to other surf breaks?'),
(178, 'SURF_TRAVEL_DISTANCE', 'How far do you travel away from this beach between sessions (home/work/travel)?', 'How far do you travel away from this beach between sessions (home/work/travel)?'),
(179, 'SURF_WEETSUIT', 'What type of wetsuit do you use?', 'What type of wetsuit do you use?'),
(180, 'SURF_SUNSCREEN', 'What type of sunscreen do you use?', 'What type of sunscreen do you use?'),
(181, 'SURF_SUNSCREEN_FREQUENCY', 'How often do you use sunscreen?', 'How often do you use sunscreen?'),
(182, 'SURF_SHOWER_FREQUENCY', 'How often do you shower after surfing?', 'How often do you shower after surfing?'),
(183, 'SURF_STANCE', 'What stance are you?', 'What stance are you?'),
(184, 'SURF_BOARD_TYPE', 'What type of surfboard do you prefer?', 'What type of surfboard do you prefer?'),
(185, 'SURF_WAX', 'What type of wax do you use?', 'What type of wax do you use?');

----------------------------------------------------------
-- group_questions
----------------------------------------------------------
--Fermented
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 165, 0);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 166, 1);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 167, 2);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 168, 3);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 169, 4);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 170, 5);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 171, 6);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 172, 7);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-3, 173, 8);
--Surfers
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 174, 0);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 175, 1);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 176, 2);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 177, 3);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 178, 4);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 179, 5);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 180, 6);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 181, 7);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 182, 8);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 183, 9);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 184, 10);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-4, 185, 11);

----------------------------------------------------------
-- survey_question_response_type
----------------------------------------------------------
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (165, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (166, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (167, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (168, 'TEXT');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (169, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (170, 'TEXT');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (171, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (172, 'TEXT');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (173, 'TEXT');

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (174, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (175, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (176, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (177, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (178, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (179, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (180, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (181, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (182, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (183, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (184, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (185, 'SINGLE');

----------------------------------------------------------
-- survey_response
----------------------------------------------------------
INSERT INTO survey_response (american, british) VALUES
('I have not increased my intake', 'I have not increased my intake'),
('Kimchi', 'Kimchi'),
('Sauerkraut', 'Sauerkraut'),
('Fermented beans/Miso/Natto', 'Fermented beans/Miso/Natto'),
('Pickled vegetables', 'Pickled vegetables'),
('Tempeh', 'Tempeh'),
('Fermented tofu', 'Fermented tofu'),
('Kefir (water)', 'Kefir (water)'),
('Kefir (milk)', 'Kefir (milk)'),
('Cottage cheese', 'Cottage cheese'),
('Yogurt/lassi', 'Yogurt/lassi'),
('Sour cream/creme fraiche', 'Sour cream/creme fraiche'),
('Fermented fish', 'Fermented fish'),
('Fish sauce', 'Fish sauce'),
('Fermented bread/sourdough/injera', 'Fermented bread/sourdough/injera'),
('Kombucha', 'Kombucha'),
('Chicha', 'Chicha'),
('Beer', 'Beer'),
('Cider', 'Cider'),
('Wine', 'Wine'),
('Mead', 'Mead');

INSERT INTO survey_response (american, british) VALUES
('Point Loma/Ocean Beach, San Diego, California, USA', 'Point Loma/Ocean Beach, San Diego, California, USA'),
('La Jolla, San Diego, California, USA', 'La Jolla, San Diego, California, USA'),
('Encinitas, California, USA', 'Encinitas, California, USA'),
('Southern California, USA', 'Southern California, USA'),
('Central California, USA', 'Central California, USA'),
('Northern, California', 'Northern, California'),
('Pacific Northwest, USA', 'Pacific Northwest, USA'),
('Hawaii, USA', 'Hawaii, USA'),
('Northeast, USA', 'Northeast, USA'),
('Southeast, USA', 'Southeast, USA'),
('South America', 'South America'),
('Europe', 'Europe'),
('Africa', 'Africa'),
('Southeast Asia', 'Southeast Asia'),
('Asia', 'Asia');

INSERT INTO survey_response (american, british) VALUES
('Multiple times a day', 'Multiple times a day'),
('Multiple times a week', 'Multiple times a week'),
('Once a week', 'Once a week'),
('Multiple times a month', 'Multiple times a month');

INSERT INTO survey_response (american, british) VALUES
('<1 km', '<1 km'),
('5-10km', '5-10km'),
('>10km', '>10km');

INSERT INTO survey_response (american, british) VALUES
('<1mm', '<1mm'),
('2-3mm', '2-3mm'),
('3-4mm', '3-4mm'),
('4-5mm', '4-5mm');

INSERT INTO survey_response (american, british) VALUES
('<SPF25', '<SPF25'),
('SPF 25-50', 'SPF 25-50'),
('SPF 50+', 'SPF 50+');

INSERT INTO survey_response (american, british) VALUES
('Every time I surf', 'Every time I surf'),
('Frequently', 'Frequently'),
('Rarely', 'Rarely');

INSERT INTO survey_response (american, british) VALUES
('Natural', 'Natural'),
('Goofy Foot', 'Goofy Foot'),
('Prone', 'Prone');

INSERT INTO survey_response (american, british) VALUES
('Longboard', 'Longboard'),
('Shortboard', 'Shortboard'),
('Bodyboard', 'Bodyboard'),
('No Board', 'No Board'),
('No preference', 'No preference');

INSERT INTO survey_response (american, british) VALUES
('Sex Wax', 'Sex Wax'),
('Sticky Bumps', 'Sticky Bumps'),
('Mrs. Palmers', 'Mrs. Palmers'),
('Bubble Gum', 'Bubble Gum'),
('Famous', 'Famous');

----------------------------------------------------------
-- survey_question_response
----------------------------------------------------------
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(165, 'Unspecified', 0),
(165, 'Never', 1),
(165, 'Rarely (a few times/month)', 2),
(165, 'Occasionally (1-2 times/week)', 3),
(165, 'Regularly (3-5 times/week)', 4),
(165, 'Daily', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(166, 'Unspecified', 0),
(166, 'Week', 1),
(166, 'Month', 2),
(166, '6 months', 3),
(166, 'Year', 4),
(166, 'I have not increased my intake', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(167, 'Unspecified', 0),
(167, 'Kimchi', 1),
(167, 'Sauerkraut', 2),
(167, 'Fermented beans/Miso/Natto', 3),
(167, 'Pickled vegetables', 4),
(167, 'Tempeh', 5),
(167, 'Fermented tofu', 6),
(167, 'Kefir (water)', 7),
(167, 'Kefir (milk)', 8),
(167, 'Cottage cheese', 9),
(167, 'Yogurt/lassi', 10),
(167, 'Sour cream/creme fraiche', 11),
(167, 'Fermented fish', 12),
(167, 'Fish sauce', 13),
(167, 'Fermented bread/sourdough/injera', 14),
(167, 'Kombucha', 15),
(167, 'Chicha', 16),
(167, 'Beer', 17),
(167, 'Cider', 18),
(167, 'Wine', 19),
(167, 'Mead', 20),
(167, 'Other', 21);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(169, 'Unspecified', 0),
(169, 'Kimchi', 1),
(169, 'Sauerkraut', 2),
(169, 'Fermented beans/Miso/Natto', 3),
(169, 'Pickled vegetables', 4),
(169, 'Tempeh', 5),
(169, 'Fermented tofu', 6),
(169, 'Kefir (water)', 7),
(169, 'Kefir (milk)', 8),
(169, 'Cottage cheese', 9),
(169, 'Yogurt/lassi', 10),
(169, 'Sour cream/creme fraiche', 11),
(169, 'Fermented fish', 12),
(169, 'Fish sauce', 13),
(169, 'Fermented bread/sourdough/injera', 14),
(169, 'Kombucha', 15),
(169, 'Chicha', 16),
(169, 'Beer', 17),
(169, 'Cider', 18),
(169, 'Wine', 19),
(169, 'Mead', 20),
(169, 'Other', 21);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(171, 'Unspecified', 0),
(171, 'Kimchi', 1),
(171, 'Sauerkraut', 2),
(171, 'Fermented beans/Miso/Natto', 3),
(171, 'Pickled vegetables', 4),
(171, 'Tempeh', 5),
(171, 'Fermented tofu', 6),
(171, 'Kefir (water)', 7),
(171, 'Kefir (milk)', 8),
(171, 'Cottage cheese', 9),
(171, 'Yogurt/lassi', 10),
(171, 'Sour cream/creme fraiche', 11),
(171, 'Fermented fish', 12),
(171, 'Fish sauce', 13),
(171, 'Fermented bread/sourdough/injera', 14),
(171, 'Kombucha', 15),
(171, 'Chicha', 16),
(171, 'Beer', 17),
(171, 'Cider', 18),
(171, 'Wine', 19),
(171, 'Mead', 20),
(171, 'Other', 21);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(174, 'Unspecified', 0),
(174, 'Point Loma/Ocean Beach, San Diego, California, USA', 1),
(174, 'La Jolla, San Diego, California, USA', 2),
(174, 'Encinitas, California, USA', 3),
(174, 'Southern California, USA', 4),
(174, 'Central California, USA', 5),
(174, 'Northern, California', 6),
(174, 'Pacific Northwest, USA', 7),
(174, 'Hawaii, USA', 8),
(174, 'Northeast, USA', 9),
(174, 'Southeast, USA', 10),
(174, 'South America', 11),
(174, 'Europe', 12),
(174, 'Africa', 13),
(174, 'Australia', 14),
(174, 'New Zealand', 15),
(174, 'Southeast Asia', 16),
(174, 'Asia', 17),
(174, 'Other', 18);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(175, 'Unspecified', 0),
(175, 'Multiple times a day', 1),
(175, 'Once a day', 2),
(175, 'Multiple times a week', 3),
(175, 'Once a week', 4),
(175, 'Multiple times a month', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(176, 'Unspecified', 0),
(176, 'Multiple times a day', 1),
(176, 'Once a day', 2),
(176, 'Multiple times a week', 3),
(176, 'Once a week', 4),
(176, 'Multiple times a month', 5);


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(177, 'Unspecified', 0),
(177, 'Multiple times a day', 1),
(177, 'Once a day', 2),
(177, 'Multiple times a week', 3),
(177, 'Once a week', 4),
(177, 'Multiple times a month', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(178, 'Unspecified', 0),
(178, '<1 km', 1),
(178, '5-10km', 2),
(178, '>10km', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(179, 'Unspecified', 0),
(179, 'None', 1),
(179, '<1mm', 2),
(179, '2-3mm', 3),
(179, '3-4mm', 4),
(179, '4-5mm', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(180, 'Unspecified', 0),
(180, '<SPF25', 1),
(180, 'SPF 25-50', 2),
(180, 'SPF 50+', 3),
(180, 'Other', 4);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(181, 'Unspecified', 0),
(181, 'Every time I surf', 1),
(181, 'Frequently', 2),
(181, 'Rarely', 3),
(181, 'Never', 4);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(182, 'Unspecified', 0),
(182, 'Every time I surf', 1),
(182, 'Frequently', 2),
(182, 'Rarely', 3),
(182, 'Never', 4);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(183, 'Unspecified', 0),
(183, 'Natural', 1),
(183, 'Goofy Foot', 2),
(183, 'Prone', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(184, 'Unspecified', 0),
(184, 'Longboard', 1),
(184, 'Shortboard', 2),
(184, 'Bodyboard', 3),
(184, 'No Board', 4),
(184, 'No preference', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(185, 'Unspecified', 0),
(185, 'Sex Wax', 1),
(185, 'Sticky Bumps', 2),
(185, 'Mrs. Palmers', 3),
(185, 'Bubble Gum', 4),
(185, 'Famous', 5),
(185, 'Other', 6);

----------------------------------------------------------
-- survey_question_triggers
----------------------------------------------------------
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (167, 168, 'Other');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (169, 170, 'Other');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (171, 172, 'Other');
