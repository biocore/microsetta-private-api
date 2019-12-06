--Create pet survey in database
----------------------------------------------------------
-- survey_group
----------------------------------------------------------
INSERT INTO survey_group (group_order, american, british) VALUES (-2, 'Pet Information', 'Pet Information');

----------------------------------------------------------
-- surveys
----------------------------------------------------------
INSERT INTO surveys (survey_id, survey_group) VALUES (2, -2);

----------------------------------------------------------
-- survey_question
----------------------------------------------------------
ALTER TABLE survey_question ADD UNIQUE (question_shortname);
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (127, 'NAME', 'Name', 'Name');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (128, 'ANIMAL_TYPE', 'Animal type', 'Animal type');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (129, 'ANIMAL_ORIGIN', 'Origin', 'Origin');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (130, 'ANIMAL_AGE', 'Age', 'Age');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (131, 'ANIMAL_GENDER','Gender', 'Gender');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (132, 'SETTING', 'Setting', 'Setting');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (133, 'WEIGHT_CAT', 'Weight category', 'Weight category');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (134, 'DIET', 'Diet classification', 'Diet classification');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (135, 'FOOD_SOURCE', 'Food source', 'Food source');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (136, 'FOOD_TYPE', 'Food type', 'Food type');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (137, 'FOOD_SPECIAL', 'Food special attributes', 'Food special attributes');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (138, 'LIVING_STATUS', 'Living status', 'Living status');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (139, 'HOURS_OUTSIDE', 'Hours spent outside', 'Hours spent outside');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (140, 'TOILET_WATER_ACCESS', 'Toilet water access', 'Toilet water access');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (141, 'COPROPHAGE', 'Coprophage', 'Coprophage');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (142, 'ANIMAL_FREE_TEXT', 'Please write anything else about this animal that you think might affect its microorganisms.', 'Please write anything else about this animal that you think might affect its microorganisms.');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (143, 'ANIMAL_TYPE_FREE_TEXT', 'Please enter the animal type', 'Please enter the animal type');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (144, 'OTHER_ANIMALS_FREE_TEXT', 'Please enter the other animal types', 'Please enter the other animal types');
INSERT INTO survey_question (survey_question_id, question_shortname, american, british) VALUES (145, 'HUMANS_FREE_TEXT', 'Please enter the age (in years) and gender of any humans that the current animal lives with', 'Please enter the age (in years) and gender of any humans that the current animal lives with');

----------------------------------------------------------
-- group_questions
----------------------------------------------------------

INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 127, 0);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 128, 1);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 129, 2);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 130, 3);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 131, 4);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 132, 5);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 133, 6);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 134, 7);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 135, 8);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 136, 9);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 137, 10);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 138, 11);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 139, 12);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 140, 13);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 141, 14);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 142, 15);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 143, 16);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 144, 17);
INSERT INTO group_questions (survey_group, survey_question_id, display_index) VALUES (-2, 145, 18);


----------------------------------------------------------
-- survey_question_response_type
----------------------------------------------------------
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (127, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (128, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (129, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (130, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (131, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (132, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (133, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (134, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (135, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (136, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (137, 'MULTIPLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (138, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (139, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (140, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (141, 'SINGLE');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (142, 'TEXT');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (143, 'STRING');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (144, 'TEXT');
INSERT INTO survey_question_response_type (survey_question_id, survey_response_type) VALUES (145, 'TEXT');

----------------------------------------------------------
-- survey_response
----------------------------------------------------------
-- animal types
INSERT INTO survey_response (american, british) VALUES ('Dog', 'Dog');
INSERT INTO survey_response (american, british) VALUES ('Cat', 'Cat');
INSERT INTO survey_response (american, british) VALUES ('Small Mammal', 'Small Mammal');
INSERT INTO survey_response (american, british) VALUES ('Large Mammal', 'Large Mammal');
INSERT INTO survey_response (american, british) VALUES ('Fish', 'Fish');
INSERT INTO survey_response (american, british) VALUES ('Bird', 'Bird');
INSERT INTO survey_response (american, british) VALUES ('Reptile', 'Reptile');
INSERT INTO survey_response (american, british) VALUES ('Amphibian', 'Amphibian');
-- animal origin
INSERT INTO survey_response (american, british) VALUES ('Breeder', 'Breeder');
INSERT INTO survey_response (american, british) VALUES ('Shelter', 'Shelter');
INSERT INTO survey_response (american, british) VALUES ('Home', 'Home');
INSERT INTO survey_response (american, british) VALUES ('Wild', 'Wild');
-- living settings
INSERT INTO survey_response (american, british) VALUES ('Urban', 'Urban');
INSERT INTO survey_response (american, british) VALUES ('Suburban', 'Suburban');
INSERT INTO survey_response (american, british) VALUES ('Rural', 'Rural');
-- size of animal
INSERT INTO survey_response (american, british) VALUES ('Underweight', 'Underweight');
INSERT INTO survey_response (american, british) VALUES ('Skinny', 'Skinny');
INSERT INTO survey_response (american, british) VALUES ('Normal', 'Normal');
INSERT INTO survey_response (american, british) VALUES ('Chubby', 'Chubby');
INSERT INTO survey_response (american, british) VALUES ('Overweight', 'Overweight');
-- Diet type
INSERT INTO survey_response (american, british) VALUES ('Carnivore', 'Carnivore');
INSERT INTO survey_response (american, british) VALUES ('Herbivore', 'Herbivore');
-- Food Source
INSERT INTO survey_response (american, british) VALUES ('Pet store food', 'Pet store food');
INSERT INTO survey_response (american, british) VALUES ('Human food', 'Human food');
INSERT INTO survey_response (american, british) VALUES ('Wild food', 'Wild food');
-- Food Type
INSERT INTO survey_response (american, british) VALUES ('Dry', 'Dry');
INSERT INTO survey_response (american, british) VALUES ('Wet', 'Wet');
-- Food special attributes
INSERT INTO survey_response (american, british) VALUES ('Organic', 'Organic');
INSERT INTO survey_response (american, british) VALUES ('Grain free', 'Grain free');
--Living Status
INSERT INTO survey_response (american, british) VALUES ('Lives alone with humans', 'Lives alone with humans');
INSERT INTO survey_response (american, british) VALUES ('Lives alone no/limited humans (shelter)', 'Lives alone no/limited humans (shelter)');
INSERT INTO survey_response (american, british) VALUES ('Lives with other animals and humans', 'Lives with other animals and humans');
INSERT INTO survey_response (american, british) VALUES ('Lives with other animals/limited humans', 'Lives with other animals/limited humans');
-- Outside time
INSERT INTO survey_response (american, british) VALUES ('Less than 2', 'Less than 2');
INSERT INTO survey_response (american, british) VALUES ('2-4', '2-4');
INSERT INTO survey_response (american, british) VALUES ('4-8', '4-8');
INSERT INTO survey_response (american, british) VALUES ('8+', '8+');

INSERT INTO survey_response (american, british) VALUES ('Regular', 'Regular');
INSERT INTO survey_response (american, british) VALUES ('Sometimes', 'Sometimes');

INSERT INTO survey_response (american, british) VALUES ('High', 'High');
INSERT INTO survey_response (american, british) VALUES ('Moderate', 'Moderate');
INSERT INTO survey_response (american, british) VALUES ('Low', 'Low');

----------------------------------------------------------
-- survey_question_response
----------------------------------------------------------
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Dog', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Cat', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Small Mammal', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Large Mammal', 4);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Fish', 5);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Bird', 6);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Reptile', 7);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Amphibian', 8);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (128, 'Other', 9);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (129, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (129, 'Breeder', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (129, 'Shelter', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (129, 'Home', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (129, 'Wild', 4);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (131, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (131, 'Male', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (131, 'Female', 2);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (132, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (132, 'Urban', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (132, 'Suburban', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (132, 'Rural', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Underweight', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Skinny', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Normal', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Chubby', 4);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (133, 'Overweight', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (134, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (134, 'Carnivore', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (134, 'Omnivore', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (134, 'Herbivore', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (135, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (135, 'Pet store food', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (135, 'Human food', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (135, 'Wild food', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (136, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (136, 'Dry', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (136, 'Wet', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (136, 'Both', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (137, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (137, 'Organic', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (137, 'Grain free', 2);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (138, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (138, 'Lives alone with humans', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (138, 'Lives alone no/limited humans (shelter)', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (138, 'Lives with other animals and humans', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (138, 'Lives with other animals/limited humans', 4);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, 'None', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, 'Less than 2', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, '2-4', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, '4-8', 4);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (139, '8+', 5);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (140, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (140, 'Regular', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (140, 'Sometimes', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (140, 'Never', 3);

INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (141, 'Unspecified', 0);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (141, 'High', 1);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (141, 'Moderate', 2);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (141, 'Low', 3);
INSERT INTO survey_question_response (survey_question_id, response, display_index) VALUES (141, 'Never', 4);
----------------------------------------------------------
-- survey_question_triggers
----------------------------------------------------------
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (128, 143, 'Other');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (138, 144, 'Lives with other animals and humans');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (138, 144, 'Lives with other animals/limited humans');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (138, 145, 'Lives alone with humans');
INSERT INTO survey_question_triggers (survey_question_id, triggered_question, triggering_response) VALUES (138, 145, 'Lives with other animals and humans');