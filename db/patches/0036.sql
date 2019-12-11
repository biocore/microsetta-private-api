-- May 21, 2016
-- Update the main AG survey with new changes from IRB ammendment

-- Retire the original specialized diet question
UPDATE ag.survey_question SET retired = TRUE WHERE survey_question_id = 10;

-- Make ordering of questions a float for ease of reordering
ALTER TABLE group_questions ALTER COLUMN display_index SET DATA TYPE float(10);


-- Add new specialized diet question
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(162, 'SPECIALIZED_DIET', 'Do you eat a specialized diet ? (select all that apply)', 'Do you eat a specialized diet ? (select all that apply)');

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (0, 162, 5.5);

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (162, 'MULTIPLE');

INSERT INTO survey_response (american, british) VALUES
('paleo-diet or primal diet', 'paleo-diet or primal diet'),
('modified paleo diet', 'modified paleo diet'),
('raw food diet', 'raw food diet'),
('FODMAP', 'FODMAP'),
('Westen-Price, or other low-grain, low processed food diet', 'Westen-Price, or other low-grain, low processed food diet'),
('Kosher', 'Kosher'),
('Halaal', 'Halaal'),
('Exclude nightshades', 'Exclude nightshades'),
('Exclude dairy', 'Exclude dairy'),
('Exclude refined sugars', 'Exclude refined sugars'),
('Other restrictions not described here', 'Other restrictions not described here'),
('I do not eat a specialized diet', 'I do not eat a specialized diet');


INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(162, 'Unspecified', 0),
(162, 'paleo-diet or primal diet', 1),
(162, 'modified paleo diet', 2),
(162, 'raw food diet', 3),
(162, 'FODMAP', 4),
(162, 'Westen-Price, or other low-grain, low processed food diet', 5),
(162, 'Kosher', 6),
(162, 'Halaal', 7),
(162, 'Exclude nightshades', 8),
(162, 'Exclude dairy', 9),
(162, 'Exclude refined sugars', 10),
(162, 'Other restrictions not described here', 11),
(162, 'I do not eat a specialized diet', 12);

-- Add new question for number of drinks
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(163, 'DRINKS_PER_SESSION','How many alcoholic drinks do you usually have when you do drink?', 'How many alcoholic drinks do you usually have when you do drink?');

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (2, 163, 6.5);

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (163, 'SINGLE');

INSERT INTO survey_response (american, british) VALUES
('1', '1'),
('1-2', '1-2'),
('2-3', '2-3'),
('3-4', '3-4'),
('4+', '4+'),
('I don''t drink', 'I don''t drink');

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(163, 'Unspecified', 0),
(163, '1', 1),
(163, '1-2', 2),
(163, '2-3', 3),
(163, '3-4', 4),
(163, '4+', 5),
(163, 'I don''t drink', 6);

-- Add new question for more fine-grained IBD (question 161 only asks chron's, no illeal or colonic distinction)
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES
(164, 'IBD_DIAGNOSIS_REFINED', 'Which type of IBD do you have?', 'Which type of IBD do you have?');

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (3, 164, 31.5);

INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (164, 'SINGLE');

INSERT INTO survey_response (american, british) VALUES
('Ileal Crohn''s Disease', 'Ileal Crohn''s Disease'),
('Colonic Crohn''s Disease', 'Colonic Crohn''s Disease'),
('Ileal and Colonic Crohn''s Disease', 'Ileal and Colonic Crohn''s Disease'),
('Microcolitis','Microcolitis');

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES
(164, 'Unspecified', 0),
(164, 'Ileal Crohn''s Disease', 1),
(164, 'Colonic Crohn''s Disease', 2),
(164, 'Ileal and Colonic Crohn''s Disease', 3),
(164, 'Ulcerative colitis', 4),
(164, 'Microcolitis', 5);

INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES
(83, 164, 'Diagnosed by a medical professional (doctor, physician assistant)'),
(83, 164, 'Diagnosed by an alternative medicine practitioner'),
(83, 164, 'Self-diagnosed');
