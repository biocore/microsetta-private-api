-- Standardize the frequency-oriented questions to the legacy responses. The new, shorter responses have not actually been used so it's safe to change them.
-- However, we need to temporarily drop the constraint on ag.survey_question_triggers.
ALTER TABLE ag.survey_question_triggers DROP CONSTRAINT fk_survey_question_triggers0;
-- Update the triggers table
UPDATE ag.survey_question_triggers SET triggering_response = 'Rarely (a few times/month)' WHERE triggering_response = 'Few times/month';
UPDATE ag.survey_question_triggers SET triggering_response = 'Occasionally (1-2 times/week)' WHERE triggering_response = '1-2 times/week';
UPDATE ag.survey_question_triggers SET triggering_response = 'Regularly (3-5 times/week)' WHERE triggering_response = '3-5 times/week';
-- Update the association between questions and valid responses
UPDATE ag.survey_question_response SET response = 'Rarely (a few times/month)' WHERE response = 'Few times/month';
UPDATE ag.survey_question_response SET response = 'Occasionally (1-2 times/week)' WHERE response = '1-2 times/week';
UPDATE ag.survey_question_response SET response = 'Regularly (3-5 times/week)' WHERE response = '3-5 times/week';
-- Now we'll recreate the constraint
ALTER TABLE ag.survey_question_triggers ADD CONSTRAINT fk_survey_question_triggers0 FOREIGN KEY (survey_question_id, triggering_response)
    REFERENCES ag.survey_question_response(survey_question_id, response);

-- Adjust some questions/responses
UPDATE ag.survey_question SET american = 'Have you ever been diagnosed with irritable bowel syndrome (IBS)? Note: IBS should not be confused with IBD. IBS is defined by symptoms, usually recurrent abdominal pain and changes in bowel movements. IBD is marked by inflammation or damage to the lining of the gastrointestinal tract.' WHERE survey_question_id = 79;
UPDATE ag.survey_question SET american = 'Please rate the current (i.e. last 2 weeks) severity of any difficulty falling asleep.' WHERE survey_question_id = 229;
UPDATE ag.survey_question SET american = 'Please rate the current (i.e. last 2 weeks) severity of any difficulty staying asleep.' WHERE survey_question_id = 230;
UPDATE ag.survey_question SET american = 'Please rate the current (i.e. last 2 weeks) severity of any problems waking up too early.' WHERE survey_question_id = 231;
UPDATE ag.survey_question SET american = 'How satisfied/dissatisfied are you with your current sleep pattern?' WHERE survey_question_id = 232;
UPDATE ag.survey_question SET american = 'How noticeable to others do you think your sleep problem is in terms of impairing the quality of your life?' WHERE survey_question_id = 233;
UPDATE ag.survey_question SET american = 'How worried/distressed are you about your current sleep problem?' WHERE survey_question_id = 234;
UPDATE ag.survey_question SET american = 'To what extent do you consider your sleep problem to interfere with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) currently?' WHERE survey_question_id = 235;

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
    (428, '12:00AM', 25),
    (428, '12:30AM', 26),
    (428, '1:00AM', 27),
    (428, '1:30AM', 28),
    (428, '2:00AM', 29),
    (428, '2:30AM', 30),
    (428, '3:00AM', 31),
    (428, '3:30AM', 32),
    (428, '4:00AM', 33),
    (428, '4:30AM', 34),
    (428, '5:00AM', 35),
    (428, '5:30AM', 36),
    (428, '6:00AM', 37),
    (428, '6:30AM', 38),
    (428, '7:00AM', 39),
    (428, '7:30AM', 40),
    (428, '8:00AM', 41),
    (428, '8:30AM', 42),
    (428, '9:00AM', 43),
    (428, '9:30AM', 44),
    (428, '10:00AM', 45),
    (428, '10:30AM', 46),
    (428, '11:00AM', 47),
    (428, '11:30AM', 48);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
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
    (344, '11:30PM', 48);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
    (345, '12:00AM', 25),
    (345, '12:30AM', 26),
    (345, '1:00AM', 27),
    (345, '1:30AM', 28),
    (345, '2:00AM', 29),
    (345, '2:30AM', 30),
    (345, '3:00AM', 31),
    (345, '3:30AM', 32),
    (345, '4:00AM', 33),
    (345, '4:30AM', 34),
    (345, '5:00AM', 35),
    (345, '5:30AM', 36),
    (345, '6:00AM', 37),
    (345, '6:30AM', 38),
    (345, '7:00AM', 39),
    (345, '7:30AM', 40),
    (345, '8:00AM', 41),
    (345, '8:30AM', 42),
    (345, '9:00AM', 43),
    (345, '9:30AM', 44),
    (345, '10:00AM', 45),
    (345, '10:30AM', 46),
    (345, '11:00AM', 47),
    (345, '11:30AM', 48);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
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
    (346, '11:30PM', 48);

INSERT INTO ag.survey_question_response (survey_question_id, response, display_index) VALUES
    (347, '12:00AM', 25),
    (347, '12:30AM', 26),
    (347, '1:00AM', 27),
    (347, '1:30AM', 28),
    (347, '2:00AM', 29),
    (347, '2:30AM', 30),
    (347, '3:00AM', 31),
    (347, '3:30AM', 32),
    (347, '4:00AM', 33),
    (347, '4:30AM', 34),
    (347, '5:00AM', 35),
    (347, '5:30AM', 36),
    (347, '6:00AM', 37),
    (347, '6:30AM', 38),
    (347, '7:00AM', 39),
    (347, '7:30AM', 40),
    (347, '8:00AM', 41),
    (347, '8:30AM', 42),
    (347, '9:00AM', 43),
    (347, '9:30AM', 44),
    (347, '10:00AM', 45),
    (347, '10:30AM', 46),
    (347, '11:00AM', 47),
    (347, '11:30AM', 48);

-- All of the queries need to update two locales, for which we've determined there aren't any relevant differences
-- 1) Mexican Spanish (es_mx) - column suffix is _spanish
-- 2) Spanish Spanish (es_es) - column suffix is _spain_spanish

-- Update survey_group names
UPDATE ag.survey_group SET spanish = 'Información básica', spain_spanish = 'Información básica' WHERE group_order = -10; -- Basic Information
UPDATE ag.survey_group SET spanish = 'En casa', spain_spanish = 'En casa' WHERE group_order = -11; -- At Home
UPDATE ag.survey_group SET spanish = 'Estilo de vida', spain_spanish = 'Estilo de vida' WHERE group_order = -12; -- Lifestyle
UPDATE ag.survey_group SET spanish = 'Intestino', spain_spanish = 'Intestino' WHERE group_order = -13; -- Gut
UPDATE ag.survey_group SET spanish = 'Salud general', spain_spanish = 'Salud general' WHERE group_order = -14; -- General Health
UPDATE ag.survey_group SET spanish = 'Diagnóstico de Salud', spain_spanish = 'Diagnóstico de Salud' WHERE group_order = -15; -- Health Diagnosis
UPDATE ag.survey_group SET spanish = 'Alergias', spain_spanish = 'Alergias' WHERE group_order = -16; -- Allergies
UPDATE ag.survey_group SET spanish = 'Dieta', spain_spanish = 'Dieta' WHERE group_order = -17; -- Diet
UPDATE ag.survey_group SET spanish = 'Dieta detallada', spain_spanish = 'Dieta detallada' WHERE group_order = -18; -- Detailed Diet
UPDATE ag.survey_group SET spanish = 'Otro', spain_spanish = 'Otro' WHERE group_order = -22; -- Other

-- Update survey_question entries
UPDATE ag.survey_question SET spanish = 'Sexo biológico asignado al nacer', spain_spanish = 'Sexo biológico asignado al nacer' WHERE survey_question_id = 502;
UPDATE ag.survey_question SET spanish = '¿Cuál de las siguientes le describe mejor?', spain_spanish = '¿Cuál de las siguientes le describe mejor?' WHERE survey_question_id = 492;
UPDATE ag.survey_question SET spanish = '¿Cuál es su nivel de educación más alto?', spain_spanish = '¿Cuál es su nivel de educación más alto?' WHERE survey_question_id = 493;
UPDATE ag.survey_question SET spanish = '¿Cuál de las siguientes opciones describe mejor el área en la que vive?', spain_spanish = '¿Cuál de las siguientes opciones describe mejor el área en la que vive?' WHERE survey_question_id = 313;
UPDATE ag.survey_question SET spanish = '¿Tiene contacto frecuente y regular con animales de granja?', spain_spanish = '¿Tiene contacto frecuente y regular con animales de granja?' WHERE survey_question_id = 326;
UPDATE ag.survey_question SET spanish = '¿Cuál es su relación con las personas de este estudio que voluntariamente le informaron de su participación (por ejemplo, pareja, hijos)? Tenga en cuenta que solo utilizaremos la información que ambas partes proporcionen. Esta información es útil porque los estudios han demostrado que nuestros genes afectan nuestro microbioma.', spain_spanish = '¿Cuál es su relación con las personas de este estudio que voluntariamente le informaron de su participación (por ejemplo, pareja, hijos)? Tenga en cuenta que solo utilizaremos la información que ambas partes proporcionen. Esta información es útil porque los estudios han demostrado que nuestros genes afectan nuestro microbioma.' WHERE survey_question_id = 316;
UPDATE ag.survey_question SET spanish = 'En las noches antes de ir a la escuela o al trabajo, ¿a qué hora se acuesta?', spain_spanish = 'En las noches antes de ir a la escuela o al trabajo, ¿a qué hora se acuesta?' WHERE survey_question_id = 345;
UPDATE ag.survey_question SET spanish = 'Tipo/marca', spain_spanish = 'Tipo/marca' WHERE survey_question_id = 490;
UPDATE ag.survey_question SET spanish = '¿Quiénes son sus compañeros de cuarto que voluntariamente le han informado de su participación en este estudio? Tenga en cuenta que solo utilizaremos la información que ambas partes proporcionen. Esta información es útil porque los estudios han demostrado que las personas con las que vivimos afectan nuestro microbioma.', spain_spanish = '¿Quiénes son sus compañeros de cuarto que voluntariamente le han informado de su participación en este estudio? Tenga en cuenta que solo utilizaremos la información que ambas partes proporcionen. Esta información es útil porque los estudios han demostrado que las personas con las que vivimos afectan nuestro microbioma.' WHERE survey_question_id = 319;
UPDATE ag.survey_question SET spanish = 'Nombre del participante', spain_spanish = 'Nombre del participante' WHERE survey_question_id = 508;
UPDATE ag.survey_question SET spanish = '¿Están genéticamente relacionados?', spain_spanish = '¿Están genéticamente relacionados?' WHERE survey_question_id = 509;
UPDATE ag.survey_question SET spanish = '¿Esta persona vive con usted?', spain_spanish = '¿Esta persona vive con usted?' WHERE survey_question_id = 510;
UPDATE ag.survey_question SET spanish = '¿Dónde se quedan principalmente su(s) perro(s)?', spain_spanish = '¿Dónde se quedan principalmente su(s) perro(s)?' WHERE survey_question_id = 501;
UPDATE ag.survey_question SET spanish = '¿Dónde se quedan principalmente su(s) gatos(s)?', spain_spanish = '¿Dónde se quedan principalmente su(s) gatos(s)?' WHERE survey_question_id = 503;
UPDATE ag.survey_question SET spanish = 'Durante la última semana, ¿cómo calificaría la calidad de su sueño?', spain_spanish = 'Durante la última semana, ¿cómo calificaría la calidad de su sueño?' WHERE survey_question_id = 350;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia se cepilla los dientes?', spain_spanish = '¿Con qué frecuencia se cepilla los dientes?' WHERE survey_question_id = 495;
UPDATE ag.survey_question SET spanish = '¿Hace un seguimiento de cualquiera de las siguientes opciones mediante el uso de una(s) aplicación(es)? Seleccione todas las que correspondan.', spain_spanish = '¿Hace un seguimiento de cualquiera de las siguientes opciones mediante el uso de una(s) aplicación(es)? Seleccione todas las que correspondan.' WHERE survey_question_id = 328;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia participa en deportes de equipo?', spain_spanish = '¿Con qué frecuencia participa en deportes de equipo?' WHERE survey_question_id = 333;
UPDATE ag.survey_question SET spanish = 'Cuando el clima lo permite, ¿con qué frecuencia hace jardinería ?', spain_spanish = 'Cuando el clima lo permite, ¿con qué frecuencia hace jardinería ?' WHERE survey_question_id = 334;
UPDATE ag.survey_question SET spanish = '¿Qué tipo de ejercicio suele hacer? Seleccione todas las que correspondan.', spain_spanish = '¿Qué tipo de ejercicio suele hacer? Seleccione todas las que correspondan.' WHERE survey_question_id = 331;
UPDATE ag.survey_question SET spanish = '¿Qué nivel de intensidad de ejercicio suele hacer? Seleccione todas las que correspondan.', spain_spanish = '¿Qué nivel de intensidad de ejercicio suele hacer? Seleccione todas las que correspondan.' WHERE survey_question_id = 332;
UPDATE ag.survey_question SET spanish = '¿Qué tipo(s) de alcohol consume normalmente? Seleccione todas las que correspondan.', spain_spanish = '¿Qué tipo(s) de alcohol consume normalmente? Seleccione todas las que correspondan.' WHERE survey_question_id = 494;
UPDATE ag.survey_question SET spanish = 'En los días que tiene escuela o trabajo, ¿a qué hora se levanta por la mañana?', spain_spanish = 'En los días que tiene escuela o trabajo, ¿a qué hora se levanta por la mañana?' WHERE survey_question_id = 344;
UPDATE ag.survey_question SET spanish = 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se levanta por la mañana?', spain_spanish = 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se levanta por la mañana?' WHERE survey_question_id = 346;
UPDATE ag.survey_question SET spanish = 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se acuesta?', spain_spanish = 'En sus días libres (cuando no tiene escuela ni trabajo), ¿a qué hora se acuesta?' WHERE survey_question_id = 347;
UPDATE ag.survey_question SET spanish = 'Nitratos', spain_spanish = 'Nitratos' WHERE survey_question_id = 517;
UPDATE ag.survey_question SET spanish = '¿Tiene un trabajo o alguna otra situación que requiera que trabaje y duerma en horarios atípicos (por ejemplo, trabaje entre las 10 pm y las 6 am y duerma entre las 9 am y las 5 pm)?', spain_spanish = '¿Tiene un trabajo o alguna otra situación que requiera que trabaje y duerma en horarios atípicos (por ejemplo, trabaje entre las 10 pm y las 6 am y duerma entre las 9 am y las 5 pm)?' WHERE survey_question_id = 348;
UPDATE ag.survey_question SET spanish = 'Si usa dispositivos electrónicos que emiten luz, como un teléfono o una computadora portátil, justo antes de acostarse, ¿los usa en modo nocturno u oscuro?', spain_spanish = 'Si usa dispositivos electrónicos que emiten luz, como un teléfono o una computadora portátil, justo antes de acostarse, ¿los usa en modo nocturno u oscuro?' WHERE survey_question_id = 349;
UPDATE ag.survey_question SET spanish = '¿Usted surfea en el mar regularmente?', spain_spanish = '¿Usted surfea en el mar regularmente?' WHERE survey_question_id = 354;
UPDATE ag.survey_question SET spanish = 'Si respondió "sí", ¿qué tipo de EII tiene?', spain_spanish = 'Si respondió "sí", ¿qué tipo de EII tiene?' WHERE survey_question_id = 360;
UPDATE ag.survey_question SET spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido dolor abdominal o malestar abdominal?', spain_spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido dolor abdominal o malestar abdominal?' WHERE survey_question_id = 362;
UPDATE ag.survey_question SET spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido distensión abdominal?', spain_spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido distensión abdominal?' WHERE survey_question_id = 363;
UPDATE ag.survey_question SET spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido flatulencias (expulsión de gases)?', spain_spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido flatulencias (expulsión de gases)?' WHERE survey_question_id = 364;
UPDATE ag.survey_question SET spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido borborigmos/ruidos estomacales?', spain_spanish = 'Durante la última semana, ¿con qué frecuencia ha tenido borborigmos/ruidos estomacales?' WHERE survey_question_id = 365;
UPDATE ag.survey_question SET spanish = 'Hormonas', spain_spanish = 'Hormonas' WHERE survey_question_id = 518;
UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado una afección de la piel?', spain_spanish = '¿Alguna vez le han diagnosticado una afección de la piel?' WHERE survey_question_id = 500;
UPDATE ag.survey_question SET spanish = '¿Está utilizando actualmente algún tipo de anticonceptivo?', spain_spanish = '¿Está utilizando actualmente algún tipo de anticonceptivo?' WHERE survey_question_id = 497;
UPDATE ag.survey_question SET spanish = '¿Qué tipo de afección de la piel le han diagnosticado?', spain_spanish = '¿Qué tipo de afección de la piel le han diagnosticado?' WHERE survey_question_id = 374;
UPDATE ag.survey_question SET spanish = '¿Quién diagnosticó su condición de la piel?', spain_spanish = '¿Quién diagnosticó su condición de la piel?' WHERE survey_question_id = 375;
UPDATE ag.survey_question SET spanish = 'Fecha estimada de parto:', spain_spanish = 'Fecha estimada de parto:' WHERE survey_question_id = 370;
UPDATE ag.survey_question SET spanish = 'En una escala del 1 al 10, donde 1 significa que tiene poco o nada de estrés y 10 significa que tiene mucho estrés, ¿cómo calificaría su nivel promedio de estrés durante el último mes?', spain_spanish = 'En una escala del 1 al 10, donde 1 significa que tiene poco o nada de estrés y 10 significa que tiene mucho estrés, ¿cómo calificaría su nivel promedio de estrés durante el último mes?' WHERE survey_question_id = 387;
UPDATE ag.survey_question SET spanish = '¿Aproximadamente cuándo le diagnosticaron?', spain_spanish = '¿Aproximadamente cuándo le diagnosticaron?' WHERE survey_question_id = 407;
UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado una enfermedad de salud mental?', spain_spanish = '¿Alguna vez le han diagnosticado una enfermedad de salud mental?' WHERE survey_question_id = 504;
UPDATE ag.survey_question SET spanish = '¿Qué tipo de cáncer(es) tuvo/tiene? Seleccione todas las que correspondan.', spain_spanish = '¿Qué tipo de cáncer(es) tuvo/tiene? Seleccione todas las que correspondan.' WHERE survey_question_id = 409;
UPDATE ag.survey_question SET spanish = '¿Qué tipo de tratamiento(s) tomó/toma? Seleccione todas las que correspondan.', spain_spanish = '¿Qué tipo de tratamiento(s) tomó/toma? Seleccione todas las que correspondan.' WHERE survey_question_id = 410;
UPDATE ag.survey_question SET spanish = 'De los siguientes, marque todos los síntomas que presenta con una migraña:', spain_spanish = 'De los siguientes, marque todos los síntomas que presenta con una migraña:' WHERE survey_question_id = 487;
UPDATE ag.survey_question SET spanish = 'Si respondió "sí", por favor seleccione qué trastorno(s) de la siguiente lista:', spain_spanish = 'Si respondió "sí", por favor seleccione qué trastorno(s) de la siguiente lista:' WHERE survey_question_id = 505;
UPDATE ag.survey_question SET spanish = '¿Quién le diagnosticó esto?', spain_spanish = '¿Quién le diagnosticó esto?' WHERE survey_question_id = 413;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia experimenta migrañas?', spain_spanish = '¿Con qué frecuencia experimenta migrañas?' WHERE survey_question_id = 485;
UPDATE ag.survey_question SET spanish = 'Si respondió "sí", seleccione qué tipo de diabetes:', spain_spanish = 'Si respondió "sí", seleccione qué tipo de diabetes:' WHERE survey_question_id = 506;
UPDATE ag.survey_question SET spanish = '¿Actualmente tiene cáncer?', spain_spanish = '¿Actualmente tiene cáncer?' WHERE survey_question_id = 408;
UPDATE ag.survey_question SET spanish = '¿Alguno de sus familiares de primer grado sufre de migraña?', spain_spanish = '¿Alguno de sus familiares de primer grado sufre de migraña?' WHERE survey_question_id = 488;
UPDATE ag.survey_question SET spanish = '¿Toma algún medicamento para la migraña?', spain_spanish = '¿Toma algún medicamento para la migraña?' WHERE survey_question_id = 489;
UPDATE ag.survey_question SET spanish = 'Para las preguntas 11b - 11i, clasifique el factor del listado basado en la probabilidad de que le provoque sus migrañas, donde "1" es el más probable, "2" es el segundo más probable, etc. Si el factor no causa migrañas, elija N /A', spain_spanish = 'Para las preguntas 11b - 11i, clasifique el factor del listado basado en la probabilidad de que le provoque sus migrañas, donde "1" es el más probable, "2" es el segundo más probable, etc. Si el factor no causa migrañas, elija N /A' WHERE survey_question_id = 511;
UPDATE ag.survey_question SET spanish = 'Cafeína', spain_spanish = 'Cafeína' WHERE survey_question_id = 512;
UPDATE ag.survey_question SET spanish = 'Depresión', spain_spanish = 'Depresión' WHERE survey_question_id = 513;
UPDATE ag.survey_question SET spanish = 'Falta de sueño', spain_spanish = 'Falta de sueño' WHERE survey_question_id = 514;
UPDATE ag.survey_question SET spanish = 'Alimentos (vino, chocolate, fresas)', spain_spanish = 'Alimentos (vino, chocolate, fresas)' WHERE survey_question_id = 515;
UPDATE ag.survey_question SET spanish = 'Medicamentos que contienen barbitúricos o opioides', spain_spanish = 'Medicamentos que contienen barbitúricos o opioides' WHERE survey_question_id = 516;
UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado alguna otra condición clínica relevante?', spain_spanish = '¿Alguna vez le han diagnosticado alguna otra condición clínica relevante?' WHERE survey_question_id = 499;
UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado cáncer?', spain_spanish = '¿Alguna vez le han diagnosticado cáncer?' WHERE survey_question_id = 507;
UPDATE ag.survey_question SET spanish = '¿Toma medicamentos para aliviar sus síntomas?', spain_spanish = '¿Toma medicamentos para aliviar sus síntomas?' WHERE survey_question_id = 415;
UPDATE ag.survey_question SET spanish = 'Si practicas el ayuno intermitente, ¿qué tipo sigues?', spain_spanish = 'Si practicas el ayuno intermitente, ¿qué tipo sigues?' WHERE survey_question_id = 423;
UPDATE ag.survey_question SET spanish = '¿Cuántas comidas sueles comer al día?', spain_spanish = '¿Cuántas comidas sueles comer al día?' WHERE survey_question_id = 425;
UPDATE ag.survey_question SET spanish = '¿Cuántas meriendas/snacks comes típicamente al día?', spain_spanish = '¿Cuántas meriendas/snacks comes típicamente al día?' WHERE survey_question_id = 426;
UPDATE ag.survey_question SET spanish = '¿Cuándo consume la mayor parte de sus calorías diarias?', spain_spanish = '¿Cuándo consume la mayor parte de sus calorías diarias?' WHERE survey_question_id = 427;
UPDATE ag.survey_question SET spanish = 'Si toma un suplemento de fibra, ¿qué tipo toma? Seleccione todas las que correspondan.', spain_spanish = 'Si toma un suplemento de fibra, ¿qué tipo toma? Seleccione todas las que correspondan.' WHERE survey_question_id = 433;
UPDATE ag.survey_question SET spanish = '¿Es usted un bebé que recibe la mayor parte de su nutrición de la leche materna o fórmula, o un adulto que recibe la mayor parte (más del 75 % de las calorías diarias) de su alimentación de batidos nutricionales para adultos (por ejemplo, Ensure)?', spain_spanish = '¿Es usted un bebé que recibe la mayor parte de su nutrición de la leche materna o fórmula, o un adulto que recibe la mayor parte (más del 75 % de las calorías diarias) de su alimentación de batidos nutricionales para adultos (por ejemplo, Ensure)?' WHERE survey_question_id = 498;
UPDATE ag.survey_question SET spanish = 'Enumere/describa cualquier otra restricción dietética especial que siga que no se haya indicado anteriormente.', spain_spanish = 'Enumere/describa cualquier otra restricción dietética especial que siga que no se haya indicado anteriormente.' WHERE survey_question_id = 424;
UPDATE ag.survey_question SET spanish = '¿A qué hora suele comer su última comida o merienda antes de irse a dormir?', spain_spanish = '¿A qué hora suele comer su última comida o merienda antes de irse a dormir?' WHERE survey_question_id = 428;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia toma un suplemento de fibra?', spain_spanish = '¿Con qué frecuencia toma un suplemento de fibra?' WHERE survey_question_id = 434;
UPDATE ag.survey_question SET spanish = 'En una semana promedio, ¿con qué frecuencia consume alimentos fortificados con alto contenido de fibra (por ejemplo, Fiber One)?', spain_spanish = 'En una semana promedio, ¿con qué frecuencia consume alimentos fortificados con alto contenido de fibra (por ejemplo, Fiber One)?' WHERE survey_question_id = 443;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume alimentos que contienen edulcorantes no nutritivos o bajos en calorías?', spain_spanish = '¿Con qué frecuencia consume alimentos que contienen edulcorantes no nutritivos o bajos en calorías?' WHERE survey_question_id = 463;
UPDATE ag.survey_question SET spanish = 'En casa, ¿cuál es la principal fuente de agua potable sin saborizantes? Esto puede incluir agua sin gas o con gas/carbonatada. *En las opciones a continuación, "embotellado" incluye botellas, jarras, enfriadores de agua o dispensadores de agua.', spain_spanish = 'En casa, ¿cuál es la principal fuente de agua potable sin saborizantes? Esto puede incluir agua sin gas o con gas/carbonatada. *En las opciones a continuación, "embotellado" incluye botellas, jarras, enfriadores de agua o dispensadores de agua.' WHERE survey_question_id = 474;
UPDATE ag.survey_question SET spanish = 'Cuando está fuera de casa, ¿cuál es la principal fuente de agua potable sin saborizantes? Esto puede incluir agua sin gas o con gas/carbonatada. *En las opciones a continuación, "embotellado" incluye botellas, jarras, enfriadores de agua o dispensadores de agua.', spain_spanish = 'Cuando está fuera de casa, ¿cuál es la principal fuente de agua potable sin saborizantes? Esto puede incluir agua sin gas o con gas/carbonatada. *En las opciones a continuación, "embotellado" incluye botellas, jarras, enfriadores de agua o dispensadores de agua.' WHERE survey_question_id = 476;
UPDATE ag.survey_question SET spanish = '¿Cuándo empezaste a consumir alimentos fermentados?', spain_spanish = '¿Cuándo empezaste a consumir alimentos fermentados?' WHERE survey_question_id = 478;
UPDATE ag.survey_question SET spanish = '¿Cuánto consume normalmente en una sentada?', spain_spanish = '¿Cuánto consume normalmente en una sentada?' WHERE survey_question_id = 462;
UPDATE ag.survey_question SET spanish = 'Si respondió "sí" a consumir bebidas y/o alimentos que contienen edulcorantes no nutritivos o bajos en calorías, ¿qué tipo de edulcorantes no nutritivos o bajos en calorías consume regularmente? Seleccione todas las que correspondan.', spain_spanish = 'Si respondió "sí" a consumir bebidas y/o alimentos que contienen edulcorantes no nutritivos o bajos en calorías, ¿qué tipo de edulcorantes no nutritivos o bajos en calorías consume regularmente? Seleccione todas las que correspondan.' WHERE survey_question_id = 464;
UPDATE ag.survey_question SET spanish = 'Si respondió "sí" a la pregunta anterior, ¿cuáles son los síntomas? Seleccione todas las que correspondan.', spain_spanish = 'Si respondió "sí" a la pregunta anterior, ¿cuáles son los síntomas? Seleccione todas las que correspondan.' WHERE survey_question_id = 466;
UPDATE ag.survey_question SET spanish = 'Cuando consume alimentos o bebidas que contienen edulcorantes no nutritivos o bajos en calorías, ¿tiende a experimentar sintomas gastrointestinales posteriores, como gases, inflamación y/o diarrea?', spain_spanish = 'Cuando consume alimentos o bebidas que contienen edulcorantes no nutritivos o bajos en calorías, ¿tiende a experimentar sintomas gastrointestinales posteriores, como gases, inflamación y/o diarrea?' WHERE survey_question_id = 465;
UPDATE ag.survey_question SET spanish = 'En casa, ¿aplica tratamiento adicional (sin incluir el filtrado) al agua que bebe antes de su consumo (p. ej., hervir, tabletas de purificación, cloro/lejía)?', spain_spanish = 'En casa, ¿aplica tratamiento adicional (sin incluir el filtrado) al agua que bebe antes de su consumo (p. ej., hervir, tabletas de purificación, cloro/lejía)?' WHERE survey_question_id = 475;
UPDATE ag.survey_question SET spanish = 'Cuando está fuera de casa, ¿aplica tratamiento adicional al agua que bebe antes de consumirla (p. ej., hervir, tabletas de purificación, cloro/lejía)?', spain_spanish = 'Cuando está fuera de casa, ¿aplica tratamiento adicional al agua que bebe antes de consumirla (p. ej., hervir, tabletas de purificación, cloro/lejía)?' WHERE survey_question_id = 477;
UPDATE ag.survey_question SET spanish = 'Por favor, describa su principal fuente de agua en el hogar:', spain_spanish = 'Por favor, describa su principal fuente de agua en el hogar:' WHERE survey_question_id = 519;
UPDATE ag.survey_question SET spanish = 'Por favor, describa su principal fuente de agua fuera del hogar:', spain_spanish = 'Por favor, describa su principal fuente de agua fuera del hogar:' WHERE survey_question_id = 520;
UPDATE ag.survey_question SET spanish = 'En el último mes, ¿ha estado expuesto a alguien que probablemente tenga coronavirus/COVID-19? (marque todas las que correspondan)', spain_spanish = 'En el último mes, ¿ha estado expuesto a alguien que probablemente tenga coronavirus/COVID-19? (marque todas las que correspondan)' WHERE survey_question_id = 211;
UPDATE ag.survey_question SET spanish = 'En el último mes, ¿ha sido sospechoso de tener una infección por Coronavirus/COVID-19?', spain_spanish = 'En el último mes, ¿ha sido sospechoso de tener una infección por Coronavirus/COVID-19?' WHERE survey_question_id = 212;
UPDATE ag.survey_question SET spanish = 'En las últimas 6 semanas, ¿ha tenido alguno de los siguientes síntomas? (marque todos los que correspondan)', spain_spanish = 'En las últimas 6 semanas, ¿ha tenido alguno de los siguientes síntomas? (marque todos los que correspondan)' WHERE survey_question_id = 214;
UPDATE ag.survey_question SET spanish = '¿Cuántas veces se has contagiado de Coronavirus/COVID-19?', spain_spanish = '¿Cuántas veces se has contagiado de Coronavirus/COVID-19?' WHERE survey_question_id = 521;
UPDATE ag.survey_question SET spanish = 'Describa la calidad de la evacuación:<br /><div class="bristol-img-container"><img src="/static/img/bristol_1.png" id="bristol-chart-1" /></div><span class="bristol-chart-text">Tipo 1: Heces en bolas duras y separadas. Como frutos secos.<br />Tipo 2: Heces con forma alargada como una salchicha pero con relieves como formada por bolas unidas.</span><div class="bristol-img-container"><img src="/static/img/bristol_2.png" id="bristol-chart-2" /></div><span class="bristol-chart-text">Tipo 3: Heces con forma alargada como una salchicha, con grietas en la superficie.<br />Tipo 4: Heces con forma alargada como una salchicha, lisa y blanda.</span><div class="bristol-img-container"><img src="/static/img/bristol_3.png" id="bristol-chart-3" /></div><span class="bristol-chart-text">Tipo 5: Heces blandas y a trozos separadas o con bordes definidos.<br />Tipo 6: Heces blandas y a trozos separadas o con bordes pegados como mermelada o puré.<br />Tipo 7: Heces líquidas sin trozos sólidos.</span>', spain_spanish = 'Describa la calidad de la evacuación:<br /><div class="bristol-img-container"><img src="/static/img/bristol_1.png" id="bristol-chart-1" /></div><span class="bristol-chart-text">Tipo 1: Heces en bolas duras y separadas. Como frutos secos.<br />Tipo 2: Heces con forma alargada como una salchicha pero con relieves como formada por bolas unidas.</span><div class="bristol-img-container"><img src="/static/img/bristol_2.png" id="bristol-chart-2" /></div><span class="bristol-chart-text">Tipo 3: Heces con forma alargada como una salchicha, con grietas en la superficie.<br />Tipo 4: Heces con forma alargada como una salchicha, lisa y blanda.</span><div class="bristol-img-container"><img src="/static/img/bristol_3.png" id="bristol-chart-3" /></div><span class="bristol-chart-text">Tipo 5: Heces blandas y a trozos separadas o con bordes definidos.<br />Tipo 6: Heces blandas y a trozos separadas o con bordes pegados como mermelada o puré.<br />Tipo 7: Heces líquidas sin trozos sólidos.</span>' WHERE survey_question_id = 38;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia usa cosméticos faciales (incluido el uso de productos para el cuidado de la piel como protector solar o humectante)?', spain_spanish = '¿Con qué frecuencia usa cosméticos faciales (incluido el uso de productos para el cuidado de la piel como protector solar o humectante)?' WHERE survey_question_id = 33;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia come al menos 2 porciones de cereales integrales en un día? (1 porción = 1 rebanada de pan 100% integral; 1 taza de cereal integral como Shredded Wheat, Wheaties, Grape Nuts, cereales con alto contenido de fibra o avena; 3-4 galletas integrales; 1/2 taza de arroz integral o pasta integral)', spain_spanish = '¿Con qué frecuencia come al menos 2 porciones de cereales integrales en un día? (1 porción = 1 rebanada de pan 100% integral; 1 taza de cereal integral como Shredded Wheat, Wheaties, Grape Nuts, cereales con alto contenido de fibra o avena; 3-4 galletas integrales; 1/2 taza de arroz integral o pasta integral)' WHERE survey_question_id = 91;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume al menos 2-3 porciones de fruta en un día? (1 porción = 1/2 taza (1 porción = 1/2 taza de jugo de fruta).', spain_spanish = '¿Con qué frecuencia consume al menos 2-3 porciones de fruta en un día? (1 porción = 1/2 taza (1 porción = 1/2 taza de jugo de fruta).' WHERE survey_question_id = 61;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume al menos 2-3 porciones de verduras con almidón y sin almidón? Ejemplos de vegetales con almidón incluyen papas blancas, maíz, guisantes y repollo. Ejemplos de verduras sin almidón incluyen verduras de hoja verde crudas, pepino, tomates, pimientos, brócoli y col rizada. (1 porción = 1/2 taza de vegetales/papas; 1 taza de vegetales de hoja crudos)', spain_spanish = '¿Con qué frecuencia consume al menos 2-3 porciones de verduras con almidón y sin almidón? Ejemplos de vegetales con almidón incluyen papas blancas, maíz, guisantes y repollo. Ejemplos de verduras sin almidón incluyen verduras de hoja verde crudas, pepino, tomates, pimientos, brócoli y col rizada. (1 porción = 1/2 taza de vegetales/papas; 1 taza de vegetales de hoja crudos)' WHERE survey_question_id = 62;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia come fuentes de proteínas de origen vegetal, como tofu, tempeh, edamame, lentejas, garbanzos, maní, almendras, nueces o quinua?', spain_spanish = '¿Con qué frecuencia come fuentes de proteínas de origen vegetal, como tofu, tempeh, edamame, lentejas, garbanzos, maní, almendras, nueces o quinua?' WHERE survey_question_id = 237;
UPDATE ag.survey_question SET spanish = 'En una semana promedio, ¿cuántas plantas diferentes come? Por ejemplo, si consume una lata de sopa que contiene zanahorias, papas y cebolla, puede contar esto como 3 plantas diferentes; Si consume pan multigrano, cada grano diferente cuenta como una planta. Incluya todas las frutas en el total.', spain_spanish = 'En una semana promedio, ¿cuántas plantas diferentes come? Por ejemplo, si consume una lata de sopa que contiene zanahorias, papas y cebolla, puede contar esto como 3 plantas diferentes; Si consume pan multigrano, cada grano diferente cuenta como una planta. Incluya todas las frutas en el total.' WHERE survey_question_id = 146;
UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume productos sin lactosa (leche de soja, leche sin lactosa, leche de almendras, etc.)?', spain_spanish = 'Por lo general, ¿cuántas veces a la semana consume productos sin lactosa (leche de soja, leche sin lactosa, leche de almendras, etc.)?' WHERE survey_question_id = 65;
UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume carne de ave (pollo, pavo, etc.)?', spain_spanish = 'Por lo general, ¿cuántos días a la semana consume carne de ave (pollo, pavo, etc.)?' WHERE survey_question_id = 69;
UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume cosas dulces (tartas, galletas, bollos, rosquillas, pastelillos, chocolate, etc.)?', spain_spanish = 'Por lo general, ¿cuántos días a la semana consume cosas dulces (tartas, galletas, bollos, rosquillas, pastelillos, chocolate, etc.)?' WHERE survey_question_id = 72;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia cocina con aceite de oliva?', spain_spanish = '¿Con qué frecuencia cocina con aceite de oliva?' WHERE survey_question_id = 73;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume bebidas con edulcorantes no nutritivos o bajos en calorías*?', spain_spanish = '¿Con qué frecuencia consume bebidas con edulcorantes no nutritivos o bajos en calorías*?' WHERE survey_question_id = 157;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha o hojas de remolacha, okra, quinua, amaranto, trigo sarraceno, salvado o germen de trigo, cereal de salvado, semillas de chía, ruibarbo, sandía, chocolate negro o cacao en polvo? (>70 %) y frutos secos como almendras, cacahuetes, nueces, anacardos y avellanas?', spain_spanish = '¿Con qué frecuencia consume alimentos ricos en oxalatos, como espinacas, acelgas, remolacha o hojas de remolacha, okra, quinua, amaranto, trigo sarraceno, salvado o germen de trigo, cereal de salvado, semillas de chía, ruibarbo, sandía, chocolate negro o cacao en polvo? (>70 %) y frutos secos como almendras, cacahuetes, nueces, anacardos y avellanas?' WHERE survey_question_id = 243;
UPDATE ag.survey_question SET spanish = 'Excluyendo la cerveza, el vino y el alcohol, he aumentado significativamente (es decir, más del doble) mi ingesta de alimentos fermentados en frecuencia o cantidad en los últimos ____.', spain_spanish = 'Excluyendo la cerveza, el vino y el alcohol, he aumentado significativamente (es decir, más del doble) mi ingesta de alimentos fermentados en frecuencia o cantidad en los últimos ____.' WHERE survey_question_id = 166;
UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume una o más porciones de vegetales o productos vegetales fermentados? (1 porción = 1/2 taza de chucrut, kimchi o vegetales fermentados o 1 taza de kombucha)', spain_spanish = '¿Con qué frecuencia consume una o más porciones de vegetales o productos vegetales fermentados? (1 porción = 1/2 taza de chucrut, kimchi o vegetales fermentados o 1 taza de kombucha)' WHERE survey_question_id = 165;

-- Update survey_response entries
UPDATE ag.survey_response SET spanish = 'Prediabetes', spain_spanish = 'Prediabetes' WHERE american = 'Prediabetes';
UPDATE ag.survey_response SET spanish = 'Blanco', spain_spanish = 'Blanco' WHERE american = 'White';
UPDATE ag.survey_response SET spanish = '0', spain_spanish = '0' WHERE american = '0';
UPDATE ag.survey_response SET spanish = '1-2 veces/semana', spain_spanish = '1-2 veces/semana' WHERE american = '1-2 times/week';
UPDATE ag.survey_response SET spanish = '10', spain_spanish = '10' WHERE american = '10';
UPDATE ag.survey_response SET spanish = '10:00AM', spain_spanish = '10:00AM' WHERE american = '10:00AM';
UPDATE ag.survey_response SET spanish = '10:00PM', spain_spanish = '10:00PM' WHERE american = '10:00PM';
UPDATE ag.survey_response SET spanish = '10:30AM', spain_spanish = '10:30AM' WHERE american = '10:30AM';
UPDATE ag.survey_response SET spanish = '10:30PM', spain_spanish = '10:30PM' WHERE american = '10:30PM';
UPDATE ag.survey_response SET spanish = '11:00AM', spain_spanish = '11:00AM' WHERE american = '11:00AM';
UPDATE ag.survey_response SET spanish = '11:00PM', spain_spanish = '11:00PM' WHERE american = '11:00PM';
UPDATE ag.survey_response SET spanish = '11:30AM', spain_spanish = '11:30AM' WHERE american = '11:30AM';
UPDATE ag.survey_response SET spanish = '11:30PM', spain_spanish = '11:30PM' WHERE american = '11:30PM';
UPDATE ag.survey_response SET spanish = '12-16 fl oz (355-473 ml)', spain_spanish = '12-16 fl oz (355-473 ml)' WHERE american = '12-16 fl oz (355-473 ml)';
UPDATE ag.survey_response SET spanish = '12:00AM', spain_spanish = '12:00AM' WHERE american = '12:00AM';
UPDATE ag.survey_response SET spanish = '12:00PM', spain_spanish = '12:00PM' WHERE american = '12:00PM';
UPDATE ag.survey_response SET spanish = '12:30AM', spain_spanish = '12:30AM' WHERE american = '12:30AM';
UPDATE ag.survey_response SET spanish = '12:30PM', spain_spanish = '12:30PM' WHERE american = '12:30PM';
UPDATE ag.survey_response SET spanish = '16-20 fl oz (473-591 ml)', spain_spanish = '16-20 fl oz (473-591 ml)' WHERE american = '16-20 fl oz (473-591 ml)';
UPDATE ag.survey_response SET spanish = '1:00AM', spain_spanish = '1:00AM' WHERE american = '1:00AM';
UPDATE ag.survey_response SET spanish = '1:00PM', spain_spanish = '1:00PM' WHERE american = '1:00PM';
UPDATE ag.survey_response SET spanish = '1:30AM', spain_spanish = '1:30AM' WHERE american = '1:30AM';
UPDATE ag.survey_response SET spanish = '1:30PM', spain_spanish = '1:30PM' WHERE american = '1:30PM';
UPDATE ag.survey_response SET spanish = '2', spain_spanish = '2' WHERE american = '2';
UPDATE ag.survey_response SET spanish = '2 veces al día', spain_spanish = '2 veces al día' WHERE american = '2 times a day';
UPDATE ag.survey_response SET spanish = '2-3 días por semana', spain_spanish = '2-3 días por semana' WHERE american = '2-3 days per week';
UPDATE ag.survey_response SET spanish = 'Ayuno de 24 horas ', spain_spanish = 'Ayuno de 24 horas ' WHERE american = '24 hour fast (aka eat-stop-eat method)';
UPDATE ag.survey_response SET spanish = '2:00AM', spain_spanish = '2:00AM' WHERE american = '2:00AM';
UPDATE ag.survey_response SET spanish = '2:00PM', spain_spanish = '2:00PM' WHERE american = '2:00PM';
UPDATE ag.survey_response SET spanish = '2:30AM', spain_spanish = '2:30AM' WHERE american = '2:30AM';
UPDATE ag.survey_response SET spanish = '2:30PM', spain_spanish = '2:30PM' WHERE american = '2:30PM';
UPDATE ag.survey_response SET spanish = '3', spain_spanish = '3' WHERE american = '3';
UPDATE ag.survey_response SET spanish = '3-5 veces/semana', spain_spanish = '3-5 veces/semana' WHERE american = '3-5 times/week';
UPDATE ag.survey_response SET spanish = '3:00AM', spain_spanish = '3:00AM' WHERE american = '3:00AM';
UPDATE ag.survey_response SET spanish = '3:00PM', spain_spanish = '3:00PM' WHERE american = '3:00PM';
UPDATE ag.survey_response SET spanish = '3:30AM', spain_spanish = '3:30AM' WHERE american = '3:30AM';
UPDATE ag.survey_response SET spanish = '3:30PM', spain_spanish = '3:30PM' WHERE american = '3:30PM';
UPDATE ag.survey_response SET spanish = '4', spain_spanish = '4' WHERE american = '4';
UPDATE ag.survey_response SET spanish = '4-6 días por semana', spain_spanish = '4-6 días por semana' WHERE american = '4-6 days per week';
UPDATE ag.survey_response SET spanish = '4-8 fl oz (118-237 ml)', spain_spanish = '4-8 fl oz (118-237 ml)' WHERE american = '4-8 fl oz (118-237 ml)';
UPDATE ag.survey_response SET spanish = '4:00AM', spain_spanish = '4:00AM' WHERE american = '4:00AM';
UPDATE ag.survey_response SET spanish = '4:00PM', spain_spanish = '4:00PM' WHERE american = '4:00PM';
UPDATE ag.survey_response SET spanish = '4:30AM', spain_spanish = '4:30AM' WHERE american = '4:30AM';
UPDATE ag.survey_response SET spanish = '4:30PM', spain_spanish = '4:30PM' WHERE american = '4:30PM';
UPDATE ag.survey_response SET spanish = '5', spain_spanish = '5' WHERE american = '5';
UPDATE ag.survey_response SET spanish = '5:00AM', spain_spanish = '5:00AM' WHERE american = '5:00AM';
UPDATE ag.survey_response SET spanish = '5:00PM', spain_spanish = '5:00PM' WHERE american = '5:00PM';
UPDATE ag.survey_response SET spanish = 'Método 5:2 ', spain_spanish = 'Método 5:2 ' WHERE american = '5:2 method';
UPDATE ag.survey_response SET spanish = '5:30AM', spain_spanish = '5:30AM' WHERE american = '5:30AM';
UPDATE ag.survey_response SET spanish = '5:30PM', spain_spanish = '5:30PM' WHERE american = '5:30PM';
UPDATE ag.survey_response SET spanish = '6', spain_spanish = '6' WHERE american = '6';
UPDATE ag.survey_response SET spanish = '6:00AM', spain_spanish = '6:00AM' WHERE american = '6:00AM';
UPDATE ag.survey_response SET spanish = '6:00PM', spain_spanish = '6:00PM' WHERE american = '6:00PM';
UPDATE ag.survey_response SET spanish = '6:30AM', spain_spanish = '6:30AM' WHERE american = '6:30AM';
UPDATE ag.survey_response SET spanish = '6:30PM', spain_spanish = '6:30PM' WHERE american = '6:30PM';
UPDATE ag.survey_response SET spanish = '7', spain_spanish = '7' WHERE american = '7';
UPDATE ag.survey_response SET spanish = '7:00AM', spain_spanish = '7:00AM' WHERE american = '7:00AM';
UPDATE ag.survey_response SET spanish = '7:00PM', spain_spanish = '7:00PM' WHERE american = '7:00PM';
UPDATE ag.survey_response SET spanish = '7:30AM', spain_spanish = '7:30AM' WHERE american = '7:30AM';
UPDATE ag.survey_response SET spanish = '7:30PM', spain_spanish = '7:30PM' WHERE american = '7:30PM';
UPDATE ag.survey_response SET spanish = '8', spain_spanish = '8' WHERE american = '8';
UPDATE ag.survey_response SET spanish = '8-12 fl oz (237-355 ml)', spain_spanish = '8-12 fl oz (237-355 ml)' WHERE american = '8-12 fl oz (237-355 ml)';
UPDATE ag.survey_response SET spanish = '8:00AM', spain_spanish = '8:00AM' WHERE american = '8:00AM';
UPDATE ag.survey_response SET spanish = '8:00PM', spain_spanish = '8:00PM' WHERE american = '8:00PM';
UPDATE ag.survey_response SET spanish = '8:30AM', spain_spanish = '8:30AM' WHERE american = '8:30AM';
UPDATE ag.survey_response SET spanish = '8:30PM', spain_spanish = '8:30PM' WHERE american = '8:30PM';
UPDATE ag.survey_response SET spanish = '9', spain_spanish = '9' WHERE american = '9';
UPDATE ag.survey_response SET spanish = '9:00AM', spain_spanish = '9:00AM' WHERE american = '9:00AM';
UPDATE ag.survey_response SET spanish = '9:00PM', spain_spanish = '9:00PM' WHERE american = '9:00PM';
UPDATE ag.survey_response SET spanish = '9:30AM', spain_spanish = '9:30AM' WHERE american = '9:30AM';
UPDATE ag.survey_response SET spanish = '9:30PM', spain_spanish = '9:30PM' WHERE american = '9:30PM';
UPDATE ag.survey_response SET spanish = '<4 fl oz (<118 ml)', spain_spanish = '<4 fl oz (<118 ml)' WHERE american = '<4 fl oz (<118 ml)';
UPDATE ag.survey_response SET spanish = '>20 fl oz (>591 ml)', spain_spanish = '>20 fl oz (>591 ml)' WHERE american = '>20 fl oz (>591 ml)';
UPDATE ag.survey_response SET spanish = 'Algunas veces al año', spain_spanish = 'Algunas veces al año' WHERE american = 'A few times a year';
UPDATE ag.survey_response SET spanish = 'Acesulfamo de potasio', spain_spanish = 'Acesulfamo de potasio' WHERE american = 'Acesulfame potassium';
UPDATE ag.survey_response SET spanish = 'Actividad/ejercicio', spain_spanish = 'Actividad/ejercicio' WHERE american = 'Activity/exercise';
UPDATE ag.survey_response SET spanish = 'Cáncer suprarrenal', spain_spanish = 'Cáncer suprarrenal' WHERE american = 'Adrenal cancer';
UPDATE ag.survey_response SET spanish = 'Entrenamiento aeróbico/cardio', spain_spanish = 'Entrenamiento aeróbico/cardio' WHERE american = 'Aerobic/cardio training';
UPDATE ag.survey_response SET spanish = 'Ayuno en días alternos', spain_spanish = 'Ayuno en días alternos' WHERE american = 'Alternate day fasting';
UPDATE ag.survey_response SET spanish = 'Fibra de manzana', spain_spanish = 'Fibra de manzana' WHERE american = 'Apple fiber';
UPDATE ag.survey_response SET spanish = 'Asiático', spain_spanish = 'Asiático' WHERE american = 'Asian';
UPDATE ag.survey_response SET spanish = 'Aspartame', spain_spanish = 'Aspartame' WHERE american = 'Aspartame';
UPDATE ag.survey_response SET spanish = 'Certificados de grado asociados (generalmente de 2 años)', spain_spanish = 'Certificados de grado asociados (generalmente de 2 años)' WHERE american = 'Associate''s degree (e.g. AA, AS))';
UPDATE ag.survey_response SET spanish = 'Aura', spain_spanish = 'Aura' WHERE american = 'Aura';
UPDATE ag.survey_response SET spanish = 'Título de licenciatura', spain_spanish = 'Título de licenciatura' WHERE american = 'Bachelor''s degree (e.g. BA, BS)';
UPDATE ag.survey_response SET spanish = 'Entrenamiento de equilibrio', spain_spanish = 'Entrenamiento de equilibrio' WHERE american = 'Balance training';
UPDATE ag.survey_response SET spanish = 'Negro o afroamericano', spain_spanish = 'Negro o afroamericano' WHERE american = 'Black or African American';
UPDATE ag.survey_response SET spanish = 'Cáncer de vejiga', spain_spanish = 'Cáncer de vejiga' WHERE american = 'Bladder cancer';
UPDATE ag.survey_response SET spanish = 'Dolor corporal donde no debería existir;', spain_spanish = 'Dolor corporal donde no debería existir;' WHERE american = 'Body pain where it shouldn''t exist;';
UPDATE ag.survey_response SET spanish = 'Agua purificada embotellada* (no indica "agua de manantial" o "agua mineral natural" en la etiqueta)', spain_spanish = 'Agua purificada embotellada* (no indica "agua de manantial" o "agua mineral natural" en la etiqueta)' WHERE american = 'Bottled* purified water (does not indicate "spring water" or "natural mineral water" on the label)';
UPDATE ag.survey_response SET spanish = 'Cáncer cerebral (incluye gliomas y glioblastomas)', spain_spanish = 'Cáncer cerebral (incluye gliomas y glioblastomas)' WHERE american = 'Brain cancer (includes gliomas and glioblastomas)';
UPDATE ag.survey_response SET spanish = 'Cáncer de mama', spain_spanish = 'Cáncer de mama' WHERE american = 'Breast cancer';
UPDATE ag.survey_response SET spanish = 'Las calorías son distribuidas uniformemente a lo largo del día.', spain_spanish = 'Las calorías son distribuidas uniformemente a lo largo del día.' WHERE american = 'Calories are evenly distributed throughout the day';
UPDATE ag.survey_response SET spanish = 'Cáncer de cuello uterino', spain_spanish = 'Cáncer de cuello uterino' WHERE american = 'Cervical cancer';
UPDATE ag.survey_response SET spanish = 'Colangiocarcinoma', spain_spanish = 'Colangiocarcinoma' WHERE american = 'Cholangiocarcinoma';
UPDATE ag.survey_response SET spanish = 'Cáncer de colon', spain_spanish = 'Cáncer de colon' WHERE american = 'Colon cancer';
UPDATE ag.survey_response SET spanish = 'Enfermedad de Crohn colónica', spain_spanish = 'Enfermedad de Crohn colónica' WHERE american = 'Colonic Crohn''s disease';
UPDATE ag.survey_response SET spanish = 'Estriñimiento', spain_spanish = 'Estriñimiento' WHERE american = 'Constipation';
UPDATE ag.survey_response SET spanish = 'Kinder a Secundaria', spain_spanish = 'Kinder a Secundaria' WHERE american = 'Currently in K-12';
UPDATE ag.survey_response SET spanish = 'Alimentación restringida en el tiempo (TRE)', spain_spanish = 'Alimentación restringida en el tiempo (TRE)' WHERE american = 'Daily time-restricted eating (TRE)';
UPDATE ag.survey_response SET spanish = 'Dieta', spain_spanish = 'Dieta' WHERE american = 'Diet';
UPDATE ag.survey_response SET spanish = 'Título de Doctor', spain_spanish = 'Título de Doctor' WHERE american = 'Doctorate (eg. PhD, EdD)';
UPDATE ag.survey_response SET spanish = 'No sé', spain_spanish = 'No sé' WHERE american = 'Don''t know';
UPDATE ag.survey_response SET spanish = 'Cáncer de esófago', spain_spanish = 'Cáncer de esófago' WHERE american = 'Esophageal cancer';
UPDATE ag.survey_response SET spanish = 'Pocas veces/mes', spain_spanish = 'Pocas veces/mes' WHERE american = 'Few times/month';
UPDATE ag.survey_response SET spanish = 'Pocas veces/año', spain_spanish = 'Pocas veces/año' WHERE american = 'Few times/year';
UPDATE ag.survey_response SET spanish = 'Agua del grifo filtrada (jarra con filtro, grifo o purificadores de agua debajo del fregadero, sistemas de ósmosis inversa, ablandador de agua)', spain_spanish = 'Agua del grifo filtrada (jarra con filtro, grifo o purificadores de agua debajo del fregadero, sistemas de ósmosis inversa, ablandador de agua)' WHERE american = 'Filtered tap water (pitcher, faucet or under the sink water purifiers, reverse osmosis systems, water softener)';
UPDATE ag.survey_response SET spanish = 'Entrenamiento de flexibilidad', spain_spanish = 'Entrenamiento de flexibilidad' WHERE american = 'Flexibility training';
UPDATE ag.survey_response SET spanish = 'Vino fortificado', spain_spanish = 'Vino fortificado' WHERE american = 'Fortified wine';
UPDATE ag.survey_response SET spanish = 'Alimentos funcionales (por ejemplo, semillas de chía, salvado de trigo)', spain_spanish = 'Alimentos funcionales (por ejemplo, semillas de chía, salvado de trigo)' WHERE american = 'Functional food (e.g. chia seeds, wheat bran)';
UPDATE ag.survey_response SET spanish = 'Trastorno de ansiedad generalizada', spain_spanish = 'Trastorno de ansiedad generalizada' WHERE american = 'Generalized anxiety disorder';
UPDATE ag.survey_response SET spanish = 'Hard cider', spain_spanish = 'Hard cider' WHERE american = 'Hard cider';
UPDATE ag.survey_response SET spanish = 'Hard kombucha', spain_spanish = 'Hard kombucha' WHERE american = 'Hard kombucha';
UPDATE ag.survey_response SET spanish = 'Hard seltzer', spain_spanish = 'Hard seltzer' WHERE american = 'Hard seltzer';
UPDATE ag.survey_response SET spanish = 'Hard tea', spain_spanish = 'Hard tea' WHERE american = 'Hard tea';
UPDATE ag.survey_response SET spanish = 'Cáncer de cabeza y cuello', spain_spanish = 'Cáncer de cabeza y cuello' WHERE american = 'Head and Neck cancer';
UPDATE ag.survey_response SET spanish = 'Preparatoria', spain_spanish = 'Preparatoria' WHERE american = 'High school diploma or GED equivalent';
UPDATE ag.survey_response SET spanish = 'Hispano o latino', spain_spanish = 'Hispano o latino' WHERE american = 'Hispanic or Latino';
UPDATE ag.survey_response SET spanish = 'Medicamentos homeopáticos', spain_spanish = 'Medicamentos homeopáticos' WHERE american = 'Homeopathic medicines';
UPDATE ag.survey_response SET spanish = 'Terapia hormonal', spain_spanish = 'Terapia hormonal' WHERE american = 'Hormone therapy';
UPDATE ag.survey_response SET spanish = 'Hipertermia', spain_spanish = 'Hipertermia' WHERE american = 'Hyperthermia';
UPDATE ag.survey_response SET spanish = 'No como alimentos fermentados', spain_spanish = 'No como alimentos fermentados' WHERE american = 'I do not eat fermented foods';
UPDATE ag.survey_response SET spanish = 'No practico el ayuno intermitente', spain_spanish = 'No practico el ayuno intermitente' WHERE american = 'I do not practice intermittent fasting';
UPDATE ag.survey_response SET spanish = 'No tomo suplementos de fibra', spain_spanish = 'No tomo suplementos de fibra' WHERE american = 'I do not take fiber supplements';
UPDATE ag.survey_response SET spanish = 'No registro ninguna de mis actividades.', spain_spanish = 'No registro ninguna de mis actividades.' WHERE american = 'I do not track any of my activities';
UPDATE ag.survey_response SET spanish = 'No uso estos dispositivos antes de acostarme.', spain_spanish = 'No uso estos dispositivos antes de acostarme.' WHERE american = 'I do not use these devices before bed';
UPDATE ag.survey_response SET spanish = 'No bebo agua natural, sin sabor', spain_spanish = 'No bebo agua natural, sin sabor' WHERE american = 'I don''t drink plain, unflavored water';
UPDATE ag.survey_response SET spanish = 'Tomo un suplemento, pero no sé de qué tipo.', spain_spanish = 'Tomo un suplemento, pero no sé de qué tipo.' WHERE american = 'I take a supplement, but do not know what kind';
UPDATE ag.survey_response SET spanish = 'Enfermedad de Crohn ileal', spain_spanish = 'Enfermedad de Crohn ileal' WHERE american = 'Ileal Crohn''s disease';
UPDATE ag.survey_response SET spanish = 'Enfermedad de Crohn ileal y colónica', spain_spanish = 'Enfermedad de Crohn ileal y colónica' WHERE american = 'Ileal and Colonic Crohn''s disease';
UPDATE ag.survey_response SET spanish = 'Inmunoterapia', spain_spanish = 'Inmunoterapia' WHERE american = 'Immunotherapy';
UPDATE ag.survey_response SET spanish = 'Por la tarde', spain_spanish = 'Por la tarde' WHERE american = 'In the afternoon';
UPDATE ag.survey_response SET spanish = 'Por la noche', spain_spanish = 'Por la noche' WHERE american = 'In the evening';
UPDATE ag.survey_response SET spanish = 'Por la mañana', spain_spanish = 'Por la mañana' WHERE american = 'In the morning';
UPDATE ag.survey_response SET spanish = 'Inulina (por ejemplo, fiber choice)', spain_spanish = 'Inulina (por ejemplo, fiber choice)' WHERE american = 'Inulin (e.g. Fiber Choice)';
UPDATE ag.survey_response SET spanish = 'Irritabilidad o evitación de la rutina;', spain_spanish = 'Irritabilidad o evitación de la rutina;' WHERE american = 'Irritability or avoidance of routine;';
UPDATE ag.survey_response SET spanish = 'Casa/propiedad aislada (la población es inferior a 100)', spain_spanish = 'Casa/propiedad aislada (la población es inferior a 100)' WHERE american = 'Isolated house/farm (population is less than 100)';
UPDATE ag.survey_response SET spanish = 'Cáncer de riñon', spain_spanish = 'Cáncer de riñon' WHERE american = 'Kidney cancer';
UPDATE ag.survey_response SET spanish = 'Leucemia', spain_spanish = 'Leucemia' WHERE american = 'Leukemia';
UPDATE ag.survey_response SET spanish = 'Cáncer de hígado', spain_spanish = 'Cáncer de hígado' WHERE american = 'Liver cancer';
UPDATE ag.survey_response SET spanish = 'Cáncer de pulmón', spain_spanish = 'Cáncer de pulmón' WHERE american = 'Lung cancer';
UPDATE ag.survey_response SET spanish = 'Linfoma', spain_spanish = 'Linfoma' WHERE american = 'Lymphoma';
UPDATE ag.survey_response SET spanish = 'Licor de malta', spain_spanish = 'Licor de malta' WHERE american = 'Malt liquor';
UPDATE ag.survey_response SET spanish = 'Título de Maestría', spain_spanish = 'Título de Maestría' WHERE american = 'Master''s degree (e.g. MS, MA)';
UPDATE ag.survey_response SET spanish = 'Melanoma (piel)', spain_spanish = 'Melanoma (piel)' WHERE american = 'Melanoma (skin)';
UPDATE ag.survey_response SET spanish = 'Metilcelulosa (por ejemplo, Citrucel)', spain_spanish = 'Metilcelulosa (por ejemplo, Citrucel)' WHERE american = 'Methylcellulose (e.g. Citrucel)';
UPDATE ag.survey_response SET spanish = 'Metrópolis (la población es más de 1 millón)', spain_spanish = 'Metrópolis (la población es más de 1 millón)' WHERE american = 'Metropolis (population is more than 1 million)';
UPDATE ag.survey_response SET spanish = 'Fruta del monje', spain_spanish = 'Fruta del monje' WHERE american = 'Monk fruit';
UPDATE ag.survey_response SET spanish = 'Mensual', spain_spanish = 'Mensual' WHERE american = 'Monthly';
UPDATE ag.survey_response SET spanish = 'Más de 2 veces al día', spain_spanish = 'Más de 2 veces al día' WHERE american = 'More than 2 times a day';
UPDATE ag.survey_response SET spanish = 'Más de 4', spain_spanish = 'Más de 4' WHERE american = 'More than 4';
UPDATE ag.survey_response SET spanish = 'Multirracial', spain_spanish = 'Multirracial' WHERE american = 'Multiracial';
UPDATE ag.survey_response SET spanish = 'Nativo Americano o Nativo de Alaska', spain_spanish = 'Nativo Americano o Nativo de Alaska' WHERE american = 'Native American or Alaska Native';
UPDATE ag.survey_response SET spanish = 'Nativo Hawaiano u otro Isleño del Pacífico', spain_spanish = 'Nativo Hawaiano u otro Isleño del Pacífico' WHERE american = 'Native Hawaiian or Other Pacific Islander';
UPDATE ag.survey_response SET spanish = 'Agua mineral natural o de manantial embotellada* en otro país de la Unión Europea o del Reino Unido', spain_spanish = 'Agua mineral natural o de manantial embotellada* en otro país de la Unión Europea o del Reino Unido' WHERE american = 'Natural mineral or spring water bottled* in another country in the European Union or the UK';
UPDATE ag.survey_response SET spanish = 'Agua mineral natural o de manantial embotellada* en otro país fuera de la Unión Europea o el Reino Unido', spain_spanish = 'Agua mineral natural o de manantial embotellada* en otro país fuera de la Unión Europea o el Reino Unido' WHERE american = 'Natural mineral or spring water bottled* in another country not in the European Union or the UK';
UPDATE ag.survey_response SET spanish = 'Agua mineral natural o de manantial embotellada* localmente (es decir, en su país de residencia)', spain_spanish = 'Agua mineral natural o de manantial embotellada* localmente (es decir, en su país de residencia)' WHERE american = 'Natural mineral or spring water bottled* locally (i.e. in your country of residence)';
UPDATE ag.survey_response SET spanish = 'Náuseas y/o vómitos;', spain_spanish = 'Náuseas y/o vómitos;' WHERE american = 'Nausea and/or vomiting;';
UPDATE ag.survey_response SET spanish = 'Sin estudios formales', spain_spanish = 'Sin estudios formales' WHERE american = 'No formal education';
UPDATE ag.survey_response SET spanish = 'No, no tengo esta condición', spain_spanish = 'No, no tengo esta condición' WHERE american = 'No, I do not have this condition';
UPDATE ag.survey_response SET spanish = 'No, no tomo ningún medicamento para mis alergias', spain_spanish = 'No, no tomo ningún medicamento para mis alergias' WHERE american = 'No, I do not take any medications for my allergies';
UPDATE ag.survey_response SET spanish = 'No, ya no tengo cáncer', spain_spanish = 'No, ya no tengo cáncer' WHERE american = 'No, I no longer have cancer';
UPDATE ag.survey_response SET spanish = 'Fibra de avena', spain_spanish = 'Fibra de avena' WHERE american = 'Oat fiber';
UPDATE ag.survey_response SET spanish = 'Una vez por semana', spain_spanish = 'Una vez por semana' WHERE american = 'Once per week';
UPDATE ag.survey_response SET spanish = 'Solo durante el Ramadán', spain_spanish = 'Solo durante el Ramadán' WHERE american = 'Only during Ramadan';
UPDATE ag.survey_response SET spanish = 'Cáncer de ovarios', spain_spanish = 'Cáncer de ovarios' WHERE american = 'Ovarian cancer';
UPDATE ag.survey_response SET spanish = 'Cáncer de páncreas', spain_spanish = 'Cáncer de páncreas' WHERE american = 'Pancreatic cancer';
UPDATE ag.survey_response SET spanish = 'Ayuno periódico', spain_spanish = 'Ayuno periódico' WHERE american = 'Periodic fasting';
UPDATE ag.survey_response SET spanish = 'Cáncer de feocromocitoma y paraganglioma', spain_spanish = 'Cáncer de feocromocitoma y paraganglioma' WHERE american = 'Pheochromocytoma and paraganglioma cancer';
UPDATE ag.survey_response SET spanish = 'Fonofobia (sensibilidad al sonido);', spain_spanish = 'Fonofobia (sensibilidad al sonido);' WHERE american = 'Phonophobia (sensitivity to sound);';
UPDATE ag.survey_response SET spanish = 'Terapia fotodinámica', spain_spanish = 'Terapia fotodinámica' WHERE american = 'Photodynamic therapy';
UPDATE ag.survey_response SET spanish = 'Fotofobia (sensibilidad a la luz);', spain_spanish = 'Fotofobia (sensibilidad a la luz);' WHERE american = 'Photophobia (sensitivity to light);';
UPDATE ag.survey_response SET spanish = 'Título professional (quiropractico, veterinario)', spain_spanish = 'Título professional (quiropractico, veterinario)' WHERE american = 'Professional degree (e.g. MD,DDS, DVM)';
UPDATE ag.survey_response SET spanish = 'Cáncer de prostata', spain_spanish = 'Cáncer de prostata' WHERE american = 'Prostate cancer';
UPDATE ag.survey_response SET spanish = 'Psyllium (por ejemplo, Metamucil)', spain_spanish = 'Psyllium (por ejemplo, Metamucil)' WHERE american = 'Psyllium (e.g. Metamucil)';
UPDATE ag.survey_response SET spanish = 'Radioterapia', spain_spanish = 'Radioterapia' WHERE american = 'Radiotherapy';
UPDATE ag.survey_response SET spanish = 'Cáncer de recto', spain_spanish = 'Cáncer de recto' WHERE american = 'Rectal cancer';
UPDATE ag.survey_response SET spanish = 'Vino rosado', spain_spanish = 'Vino rosado' WHERE american = 'Rose wine';
UPDATE ag.survey_response SET spanish = 'Sacarina', spain_spanish = 'Sacarina' WHERE american = 'Saccharin';
UPDATE ag.survey_response SET spanish = 'Sake', spain_spanish = 'Sake' WHERE american = 'Sake';
UPDATE ag.survey_response SET spanish = 'Sarcoma', spain_spanish = 'Sarcoma' WHERE american = 'Sarcoma';
UPDATE ag.survey_response SET spanish = 'Desde la infancia/niñez', spain_spanish = 'Desde la infancia/niñez' WHERE american = 'Since infancy/childhood';
UPDATE ag.survey_response SET spanish = 'Dormir', spain_spanish = 'Dormir' WHERE american = 'Sleep';
UPDATE ag.survey_response SET spanish = 'Ciudad pequeña o pueblo (la población es de más de 100 y menos de 1000)', spain_spanish = 'Ciudad pequeña o pueblo (la población es de más de 100 y menos de 1000)' WHERE american = 'Small town or village (population is more than 100 and less than 1,000)';
UPDATE ag.survey_response SET spanish = 'Heces blandas', spain_spanish = 'Heces blandas' WHERE american = 'Soft stools';
UPDATE ag.survey_response SET spanish = 'Cerveza agria', spain_spanish = 'Cerveza agria' WHERE american = 'Sour beer';
UPDATE ag.survey_response SET spanish = 'Vino espumoso', spain_spanish = 'Vino espumoso' WHERE american = 'Sparkling wine';
UPDATE ag.survey_response SET spanish = 'Licores/cócteles', spain_spanish = 'Licores/cócteles' WHERE american = 'Spirits/liquors/hard alcohol';
UPDATE ag.survey_response SET spanish = 'Trasplante de células madre', spain_spanish = 'Trasplante de células madre' WHERE american = 'Stem cell transplant';
UPDATE ag.survey_response SET spanish = 'Stevia', spain_spanish = 'Stevia' WHERE american = 'Stevia';
UPDATE ag.survey_response SET spanish = 'Cáncer de estómago', spain_spanish = 'Cáncer de estómago' WHERE american = 'Stomach cancer';
UPDATE ag.survey_response SET spanish = 'Dolor de estómago', spain_spanish = 'Dolor de estómago' WHERE american = 'Stomachache';
UPDATE ag.survey_response SET spanish = 'Entrenamiento de fuerza', spain_spanish = 'Entrenamiento de fuerza' WHERE american = 'Strength training';
UPDATE ag.survey_response SET spanish = 'Sucralosa', spain_spanish = 'Sucralosa' WHERE american = 'Sucralose';
UPDATE ag.survey_response SET spanish = 'Alcoholes de azúcar (sorbitol, xilitol, lactitol, manitol, eritritol y maltitol)', spain_spanish = 'Alcoholes de azúcar (sorbitol, xilitol, lactitol, manitol, eritritol y maltitol)' WHERE american = 'Sugar alcohols (sorbitol, xylitol, lactitol, mannitol, erythritol, and maltitol)';
UPDATE ag.survey_response SET spanish = 'Cirugía', spain_spanish = 'Cirugía' WHERE american = 'Surgery';
UPDATE ag.survey_response SET spanish = 'Agua del grifo', spain_spanish = 'Agua del grifo' WHERE american = 'Tap water';
UPDATE ag.survey_response SET spanish = 'Terapia farmacológica dirigida ', spain_spanish = 'Terapia farmacológica dirigida ' WHERE american = 'Targeted (medication) therapy';
UPDATE ag.survey_response SET spanish = 'Cáncer testicular de células germinales', spain_spanish = 'Cáncer testicular de células germinales' WHERE american = 'Testicular germ cell cancer';
UPDATE ag.survey_response SET spanish = 'Cáncer de tiroides', spain_spanish = 'Cáncer de tiroides' WHERE american = 'Thyroid cancer';
UPDATE ag.survey_response SET spanish = 'Ciudad mediana (la población es de más de 1000 y menos de 100 000)', spain_spanish = 'Ciudad mediana (la población es de más de 1000 y menos de 100 000)' WHERE american = 'Town (population is more than 1,000 and less than 100,000)';
UPDATE ag.survey_response SET spanish = 'Colitis ulcerosa', spain_spanish = 'Colitis ulcerosa' WHERE american = 'Ulcerative Colitis';
UPDATE ag.survey_response SET spanish = 'Cáncer uterino', spain_spanish = 'Cáncer uterino' WHERE american = 'Uterine cancer';
UPDATE ag.survey_response SET spanish = 'Melanoma uveal', spain_spanish = 'Melanoma uveal' WHERE american = 'Uveal melanoma';
UPDATE ag.survey_response SET spanish = 'Vigoroso', spain_spanish = 'Vigoroso' WHERE american = 'Vigorous';
UPDATE ag.survey_response SET spanish = 'Especializaciones vocacionales', spain_spanish = 'Especializaciones vocacionales' WHERE american = 'Vocational training';
UPDATE ag.survey_response SET spanish = 'Semanalmente', spain_spanish = 'Semanalmente' WHERE american = 'Weekly';
UPDATE ag.survey_response SET spanish = 'Agua de pozo', spain_spanish = 'Agua de pozo' WHERE american = 'Well water';
UPDATE ag.survey_response SET spanish = 'Dextrina de trigo (por ejemplo, Benefiber)', spain_spanish = 'Dextrina de trigo (por ejemplo, Benefiber)' WHERE american = 'Wheat dextrin (e.g. Benefiber)';
UPDATE ag.survey_response SET spanish = 'En los últimos 10 años', spain_spanish = 'En los últimos 10 años' WHERE american = 'Within the last 10 years';
UPDATE ag.survey_response SET spanish = 'En los últimos 5 años', spain_spanish = 'En los últimos 5 años' WHERE american = 'Within the last 5 years';
UPDATE ag.survey_response SET spanish = 'En el último año', spain_spanish = 'En el último año' WHERE american = 'Within the last year';
UPDATE ag.survey_response SET spanish = 'Sí, actualmente tengo cáncer', spain_spanish = 'Sí, actualmente tengo cáncer' WHERE american = 'Yes, I currently have cancer';
UPDATE ag.survey_response SET spanish = 'Sí, tomo medicamentos homeopáticos', spain_spanish = 'Sí, tomo medicamentos homeopáticos' WHERE american = 'Yes, I take homeopathic medication';
UPDATE ag.survey_response SET spanish = 'Sí, tomo medicamentos de venta libre (sin receta)', spain_spanish = 'Sí, tomo medicamentos de venta libre (sin receta)' WHERE american = 'Yes, I take over-the-counter medication';
UPDATE ag.survey_response SET spanish = 'Sí, tomo medicamentos de venta con receta', spain_spanish = 'Sí, tomo medicamentos de venta con receta' WHERE american = 'Yes, I take prescription medication';
UPDATE ag.survey_response SET spanish = 'Sí, uso un parche anticonceptivo', spain_spanish = 'Sí, uso un parche anticonceptivo' WHERE american = 'Yes, I use a contraceptive patch';
UPDATE ag.survey_response SET spanish = 'Sí, uso un anillo vaginal anticonceptivo', spain_spanish = 'Sí, uso un anillo vaginal anticonceptivo' WHERE american = 'Yes, I use a contraceptive vaginal ring';
UPDATE ag.survey_response SET spanish = 'Sí, uso un DIU de cobre', spain_spanish = 'Sí, uso un DIU de cobre' WHERE american = 'Yes, I use a copper IUD';
UPDATE ag.survey_response SET spanish = 'Sí, uso un DIU hormonal/implante ', spain_spanish = 'Sí, uso un DIU hormonal/implante ' WHERE american = 'Yes, I use a hormonal IUD/implant';
UPDATE ag.survey_response SET spanish = 'Sí, uso un anticonceptivo inyectado', spain_spanish = 'Sí, uso un anticonceptivo inyectado' WHERE american = 'Yes, I use an injected contraceptive';
UPDATE ag.survey_response SET spanish = 'Sí, uso otros tipos de medicamentos que no son mencionados en esta lista', spain_spanish = 'Sí, uso otros tipos de medicamentos que no son mencionados en esta lista' WHERE american = 'Yes, I use other types of medication not listed here';
UPDATE ag.survey_response SET spanish = 'Sí, diagnosticado por un profesional médico especializado el área de la salud mental', spain_spanish = 'Sí, diagnosticado por un profesional médico especializado el área de la salud mental' WHERE american = 'Yes, diagnosed by a licensed mental health professional';
UPDATE ag.survey_response SET spanish = 'Sí, diagnosticado por un médico general o un asistente médico', spain_spanish = 'Sí, diagnosticado por un médico general o un asistente médico' WHERE american = 'Yes, diagnosed by a medical professional (doctor, physician assistant)';
UPDATE ag.survey_response SET spanish = 'Sí, diagnosticado por un médico alternativo o complementario', spain_spanish = 'Sí, diagnosticado por un médico alternativo o complementario' WHERE american = 'Yes, diagnosed by an alternative or complementary practitioner';
UPDATE ag.survey_response SET spanish = 'Ambos por igual', spain_spanish = 'Ambos por igual' WHERE american = 'Both equally';
UPDATE ag.survey_response SET spanish = 'Ciudad grande (la población es de más de 100.000 y menos de 1 millón)', spain_spanish = 'Ciudad grande (la población es de más de 100.000 y menos de 1 millón)' WHERE american = 'City (population is more than 100,000 and less than 1 million)';
UPDATE ag.survey_response SET spanish = '2021', spain_spanish = '2021' WHERE american = '2021';
UPDATE ag.survey_response SET spanish = '2022', spain_spanish = '2022' WHERE american = '2022';
UPDATE ag.survey_response SET spanish = 'N/A', spain_spanish = 'N/A' WHERE american = 'N/A';
UPDATE ag.survey_response SET spanish = 'Falta de aire o dificultad para respirar', spain_spanish = 'Falta de aire o dificultad para respirar' WHERE american = 'Shortness of breath or difficulty breathing';
UPDATE ag.survey_response SET spanish = 'Dolores de cabeza', spain_spanish = 'Dolores de cabeza' WHERE american = 'Headaches';
UPDATE ag.survey_response SET spanish = 'Dolores musculares', spain_spanish = 'Dolores musculares' WHERE american = 'Muscle aches';
UPDATE ag.survey_response SET spanish = 'Escurrimiento o congestión nasal', spain_spanish = 'Escurrimiento o congestión nasal' WHERE american = 'Runny or stuffy nose';
UPDATE ag.survey_response SET spanish = 'Sibilancias', spain_spanish = 'Sibilancias' WHERE american = 'Wheezing';
UPDATE ag.survey_response SET spanish = '3 o más', spain_spanish = '3 o más' WHERE american = '3 or more';
UPDATE ag.survey_response SET spanish = 'Escuela o carrera técnica', spain_spanish = 'Escuela o carrera técnica' WHERE american = 'Some college or technical school';
UPDATE ag.survey_response SET spanish = 'La diagnosticó un practicante de medicina alternativa', spain_spanish = 'La diagnosticó un practicante de medicina alternativa' WHERE american = 'Diagnosed by an alternative medicine practitioner';

-- Every consent/assent document was updated with varying degrees of minor changes since the last update.
-- Since none of them have been used in production yet, we can safely update in place rather than insert new versions.
-- This patch will include en_US, es_MX, and es_ES. ja_JP documents will be handled separately in the Japanese updates branch.
-- For any future maintainers, this practice should NOT be carried forward beyond the TMI relaunch - even minor verbiage updates should be inserted as new records in the table with reconsent = true
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
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
    Dr. Rob Knight from the University of California San Diego (UC San Diego) is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. You have been asked to participate in this study because you, and everyone else on earth, have a unique microbiome, and the more people we study of all ages, the more we will understand about how the microorganisms may help or harm us. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
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
    Participation in this study may involve some added risks or discomforts. These include the following:<br />
    <ol>
        <li>You may experience temporary pain or a bruise at the site of the needle-stick if you take the blood test.</li>
        <li>There is a risk of loss of confidentiality.</li>
    </ol>
</p>
<p class="consent_content">
    Because this is a research study, there may be some unknown risks that are currently unforeseeable. You and your parents will be informed of any significant new findings.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
    You do not have to participate. Your participation in this study is completely voluntary. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You can refuse to participate or withdraw at any time by requesting the deletion of your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you.<br />
    You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit to you for participating in this study. You will get access to your data that will give you and your parents an idea of what kinds of microorganisms are in your sample and how it compares with other people like you (age, sex).
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
    There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure.
</p>
<p class="consent_header">
    What about your confidentiality?
</p>
<p class="consent_content">
    Research records will be kept confidential to the extent allowed by law.  As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel.  The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    How we will use your Sample
</p>
<p class="consent_content">
    Information from analyses of your data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or sample(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong><u>Please Note</u></strong>:<br />
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
<p class="consent_header">
    Your Signature and Assent
</p>
<p class="consent_content">
    You may download a copy of this assent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>' WHERE locale = 'en_US' AND consent_type = 'adolescent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
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
    Dr. Rob Knight from the University of California San Diego (UC San Diego) is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. You have been asked to participate in this study because you, and everyone else on earth, have a unique microbiome, and the more people we study of all ages, the more we will understand about how the microorganisms may help or harm us. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
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
    Participation in this study can involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom. There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
    Your participation in this study is completely voluntary and you can refuse to participate or withdraw at any time by simply exiting the survey and deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you. You are free to skip any question that you choose.
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
    The Personal Data you provide will be used for the following purposes:<br />
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
    The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.
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
</p>' WHERE locale = 'en_US' AND consent_type = 'adolescent_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consent to Act as a Research Subject</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Biospecimen and Future Use Research
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called your microbiome) that live in and on your body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You have been asked to participate in this study because your microbiome is unique – not the same as anyone else''s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done?
</p>
<p class="consent_content">
    The purpose of this study is to assess more accurately the microbial differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your information and biospecimens for the purpose of processing your biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
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
    If collecting from stool, you will be asked to sample in one of a variety of ways, such as the following:<br />
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
    Once your sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them.  We estimate that it can take 1-3 months for you to learn the results of your microbiome analysis. If you are a part of a specific sub-study, it may take longer, depending on the duration of the study.
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
    Participation in this study may involve some added risks or discomforts. These include the following:<br />
    <ol>
        <li>If using the blood collection device, you may experience temporary pain or a bruise at the site of the needle-stick.</li>
        <li>There is a risk of loss of confidentiality.</li>
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
    You may refuse to participate or withdraw at any time without penalty or loss of benefits to which you are entitled. You can refuse to participate or withdraw at any time by requesting the deletion of your online profile. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you.
</p>
<p class="consent_content">
    You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no monetary or direct benefit for participating in this study. You will receive a report detailing the results of our analysis on your biospecimen(s), as well as facts and figures comparing your microbiome''s composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
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
    Research records will be kept confidential to the extent allowed by law. As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    How we will use your Sample
</p>
<p class="consent_content">
    Information from analyses of your data and biospecimen(s) will be used  to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use.We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong><u>Please Note</u></strong>:<br />
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
</p>' WHERE locale = 'en_US' AND consent_type = 'adult_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consent to Act as a Research Subject</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    You are being invited to participate in a research study titled The Microsetta Initiative. This study is being done by Dr. Rob Knight from the University of California San Diego (UC San Diego). You were selected to participate in this study because you are unique and your microbiome is unique – not the same as anyone else''s on earth. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
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
    Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
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
    Your participation in this study is completely voluntary and you can withdraw at any time by simply exiting the survey and deleting your online profile, or by requesting the deletion of your account through your online account. You are free to skip any question that you choose.
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
    The Personal Data you provide will be used for the following purposes:<br />
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
    The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.
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
</p>' WHERE locale = 'en_US' AND consent_type = 'adult_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Assent to Act as a Research Subject<br />
    (Ages 7-12 years)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative (a study about microbes)</strong>
</p>
<p class="consent_content">
    Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of  tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something but we can''t tell you that because we are not allowed to do that.
</p>
<p class="consent_content">
    If you decide you want to be in this research study, this is what will happen to you:<br />
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
</p>' WHERE locale = 'en_US' AND consent_type = 'child_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Assent to Act as a Research Subject<br />
    (Ages 7-12 years)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative (a study about microbes)</strong>
</p>
<p class="consent_content">
    Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something but we can''t tell you that because we are not allowed to do that.
</p>
<p class="consent_content">
    If you decide you want to be in this research study, this is what will happen to you:<br />
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
</p>' WHERE locale = 'en_US' AND consent_type = 'child_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
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
    If collecting from your child''s stool, you will be asked to sample in one of a variety of ways, such as the following:<br />
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
    Participation in this study may involve some added risks or discomforts. These include the following:<br />
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
<p class="consent_content">
    Participation in research is entirely voluntary. We will inform you and your child if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You may refuse to have your child participate or withdraw your child at any time without penalty or loss of benefits to which you or your child are entitled. You can withdraw your child at any time by requesting the deletion of your child''s online profile. Our researchers will still use the data about your child that was collected before they were withdrawn. After your child withdraws, no further data will be collected from them.
</p>
<p class="consent_content">
    Your child may be withdrawn from the study if the instructions given by the study personnel are not followed.
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
    Research records will be kept confidential to the extent allowed by law. As part of your child''s participation in the study, you or your child will provide personal and/or sensitive information that could allow your child to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you or your child provide are stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    How we will use your child''s Sample
</p>
<p class="consent_content">
    Information from analyses of your child''s data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including your child''s) may be analyzed and published in scientific articles. We may save some of your child''s sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your child''s data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your child''s sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from your child for this study and information obtained from your child''s biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your child''s biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong><u>Please Note</u></strong>:<br />
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
</p>' WHERE locale = 'en_US' AND consent_type = 'parent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
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
    Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you or your child may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you or your child provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
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
    Participation in this study is completely voluntary and you or your child can withdraw at any time by simply exiting the survey and deleting your child''s online profile, or by requesting the deletion of your online account. You are free to skip any question that you choose.
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
    The Personal Data you provide will be used for the following purposes:<br />
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
    The research team will store and process your child''s Personal Data at our research site in the United States. The United States does not have the same laws to protect your child''s Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your child''s Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.
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
</p>' WHERE locale = 'en_US' AND consent_type = 'parent_data';

UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500.000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    No tiene que participar. Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento solicitando la eliminación de su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para usted por participar en este estudio. Usted tendrá acceso a sus datos que le darán a usted y a sus padres una idea de qué tipos de microorganismos hay
 en su muestra y cómo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
    ¿Se le pagará por participar en este estudio?
</p>
<p class="consent_content">
    Usted  no recibirá ninguna remuneración económica por participar en este estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'adolescent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500.000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos personales. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'adolescent_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500.000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    No tiene que participar. Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento solicitando la eliminación  de su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio monetario o directo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis en su(s) muestra(s) biológica(s), así como datos y cifras que comparan la composición de su microbioma con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:<br />
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'adult_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_title">
    Usted ha sido invitado a participar en un estudio de investigación titulado The Microsetta Initiative. Este estudio está siendo realizado por el Dr. Rob Knight de la University of  California San Diego (UC San Diego). Usted fue seleccionado para participar en este estudio porque usted es único y su microbioma es único, no es el mismo que el de cualquier otra persona en la tierra. Habrá aproximadamente 500.000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico.  La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
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
    Su participación en este estudio es completamente voluntaria y puede retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando su perfil, o solicitando la eliminación de su cuenta a través de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'adult_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 7-12 años)</strong>
</p>
<p class="consent_title">
    The Microsetta Initiative (un estudio sobre los microbios)
</p>
<p class="consent_content">
    El Dr. Rob Knight y su equipo de investigación están realizando un estudio de investigación para obtener más información sobre los trillones de pequeños seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas pequeñas cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es único, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo, pero no podemos decírselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
    Si usted decide que quiere participar en este estudio de investigación, esto es lo que le sucederá:<br />
    Le pediremos a usted, a su mamá o a su papá que tomen muestras de algún lugar de su cuerpo (como la piel o la boca) o sus heces (del papel higiénico) con algo parecido a 2 hisopos. A veces necesitamos más heces para nuestra investigación y luego le pediremos que defeque en un recipiente de plástico que está debajo del asiento del inodoro y atrapa la materia fecal a medida que sale. Su mamá o papá nos lo enviará en el bol. También podemos pedirle a tu mamá o papá que te pinchen el dedo para que podamos obtener un poco de tu sangre.
</p>
<p class="consent_content">
    A veces, los niños no se sienten bien mientras participan en este estudio. Es posible que sienta un poco de dolor si le frotan la piel con el hisopo y un dolor temporal si le pinchan el dedo para sacar sangre. A la mayoría de las personas no les molesta esto.
</p>
<p class="consent_content">
    No tiene que participar en este estudio de investigación si no lo desea. Nadie se enfadará con usted si dice que no. Incluso si dice que sí ahora y cambia de opinión después de comenzar a hacer este estudio, puede detenerse y nadie se enojará.
</p>
<p class="consent_content">
    Asegúrese de preguntarle a sus padres si tiene preguntas. También puede pedirles que llamen al Dr. Knight o a su equipo de investigación para que puedan brindarle más información sobre cualquier cosa que no entienda.
</p>' WHERE locale = 'es_ES' AND consent_type = 'child_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 7-12 años)</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
    El Dr. Rob Knight y su equipo de investigación están realizando un estudio de investigación para obtener más información sobre los trillones de pequeños seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas pequeñas cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es único, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo, pero no podemos decírselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
    Si decide que quiere participar en este estudio de investigación, esto es lo que le sucederá:<br />
    Le pediremos que responda preguntas en forma de encuesta sobre usted, como su edad, peso, altura, su estilo de vida, lo que come, si ha tomado antibióticos, si tiene ciertas enfermedades y si toma suplementos como vitaminas. También hay otras encuestas que puede elegir completar si lo desea.
</p>
<p class="consent_content">
    Sus respuestas se mantendrán en privado. No compartiremos ninguna información sobre si participó o no en este estudio.
</p>
<p class="consent_content">
    A veces, los niños no se sienten bien mientras participan en este estudio. Es posible que se sienta un poco cansado, aburrido o incómodo. A la mayoría de las personas no les molesta esto.
</p>
<p class="consent_content">
    Si siente alguna de estas cosas u otras cosas, asegúrese de decírselo a su mamá o papá.
</p>
<p class="consent_content">
    No tiene que participar en este estudio de investigación si no lo desea. Nadie se enfadará con usted si dice que no. Incluso si dice que sí ahora y cambia de opinión después de comenzar este estudio, puede detenerse y nadie se enojará.
</p>
<p class="consent_content">
    Asegúrese de preguntarle a sus padres si tiene preguntas. También puede pedirles que llamen al Dr. Knight o a su equipo de investigación para que puedan brindarle más información sobre cualquier cosa que no entienda.
</p>' WHERE locale = 'es_ES' AND consent_type = 'child_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:<br />
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    La participación en la investigación es totalmente voluntaria. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento sin penalización ni pérdida de los beneficios a los que usted o su hijo tienen derecho. Usted puede retirar a su hijo del estudio en cualquier momento solicitando la eliminación del perfil en línea de su hijo. Nuestros investigadores seguirán utilizando los datos sobre su hijo que se recopilaron antes de que se retirara. Después de que su hijo se retire del estudio, no se recopilarán más datos.
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
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
    La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'parent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
    The Microsetta Initiative
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
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
    La participación en este estudio es completamente voluntaria y usted o su hijo pueden retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los Datos Personales de su hijo. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_ES' AND consent_type = 'parent_data';

UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    No tiene que participar. Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento solicitando la eliminación de su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para usted por participar en este estudio. Usted tendrá acceso a sus datos que le darán a usted y a sus padres una idea de qué tipos de microorganismos hay
 en su muestra y cómo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
    ¿Se le pagará por participar en este estudio?
</p>
<p class="consent_content">
    Usted  no recibirá ninguna remuneración económica por participar en este estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'adolescent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y puede negarse a participar o retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos personales. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'adolescent_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Se le ha pedido que participe en este estudio porque usted, y todos los demás en la tierra, tienen un microbioma único, y cuantas más personas estudiemos de todas las edades, más entenderemos acerca de cómo los microorganismos pueden ayudarnos o dañarnos. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    No tiene que participar. Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento solicitando la eliminación  de su perfil en línea. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio monetario o directo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis en su(s) muestra(s) biológica(s), así como datos y cifras que comparan la composición de su microbioma con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:<br />
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'adult_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_title">
    Usted ha sido invitado a participar en un estudio de investigación titulado The Microsetta Initiative. Este estudio está siendo realizado por el Dr. Rob Knight de la University of  California San Diego (UC San Diego). Usted fue seleccionado para participar en este estudio porque usted es único y su microbioma es único, no es el mismo que el de cualquier otra persona en la tierra. Habrá aproximadamente 500,000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico.  La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
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
    Su participación en este estudio es completamente voluntaria y puede retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando su perfil, o solicitando la eliminación de su cuenta a través de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'adult_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 7-12 años)</strong>
</p>
<p class="consent_title">
    The Microsetta Initiative (un estudio sobre los microbios)
</p>
<p class="consent_content">
    El Dr. Rob Knight y su equipo de investigación están realizando un estudio de investigación para obtener más información sobre los trillones de pequeños seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas pequeñas cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es único, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo, pero no podemos decírselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
    Si usted decide que quiere participar en este estudio de investigación, esto es lo que le sucederá:<br />
    Le pediremos a usted, a su mamá o a su papá que tomen muestras de algún lugar de su cuerpo (como la piel o la boca) o sus heces (del papel higiénico) con algo parecido a 2 hisopos. A veces necesitamos más heces para nuestra investigación y luego le pediremos que defeque en un recipiente de plástico que está debajo del asiento del inodoro y atrapa la materia fecal a medida que sale. Su mamá o papá nos lo enviará en el bol. También podemos pedirle a tu mamá o papá que te pinchen el dedo para que podamos obtener un poco de tu sangre.
</p>
<p class="consent_content">
    A veces, los niños no se sienten bien mientras participan en este estudio. Es posible que sienta un poco de dolor si le frotan la piel con el hisopo y un dolor temporal si le pinchan el dedo para sacar sangre. A la mayoría de las personas no les molesta esto.
</p>
<p class="consent_content">
    No tiene que participar en este estudio de investigación si no lo desea. Nadie se enfadará con usted si dice que no. Incluso si dice que sí ahora y cambia de opinión después de comenzar a hacer este estudio, puede detenerse y nadie se enojará.
</p>
<p class="consent_content">
    Asegúrese de preguntarle a sus padres si tiene preguntas. También puede pedirles que llamen al Dr. Knight o a su equipo de investigación para que puedan brindarle más información sobre cualquier cosa que no entienda.
</p>' WHERE locale = 'es_MX' AND consent_type = 'child_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 7-12 años)</strong>
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative (un estudio sobre los microbios)</strong>
</p>
<p class="consent_content">
    El Dr. Rob Knight y su equipo de investigación están realizando un estudio de investigación para obtener más información sobre los trillones de pequeños seres vivos, como bacterias y virus, que viven en usted o sobre usted. Estas pequeñas cosas se llaman microbios, y se le pregunta a usted si desea participar en este estudio porque el tipo de microbios que tiene es único, no es el mismo que cualquier otra persona en la tierra. Es posible que podamos saber si se ha infectado con algo, pero no podemos decírselo porque no tenemos permitido hacerlo.
</p>
<p class="consent_content">
    Si decide que quiere participar en este estudio de investigación, esto es lo que le sucederá:<br />
    Le pediremos que responda preguntas en forma de encuesta sobre usted, como su edad, peso, altura, su estilo de vida, lo que come, si ha tomado antibióticos, si tiene ciertas enfermedades y si toma suplementos como vitaminas. También hay otras encuestas que puede elegir completar si lo desea.
</p>
<p class="consent_content">
    Sus respuestas se mantendrán en privado. No compartiremos ninguna información sobre si participó o no en este estudio.
</p>
<p class="consent_content">
    A veces, los niños no se sienten bien mientras participan en este estudio. Es posible que se sienta un poco cansado, aburrido o incómodo. A la mayoría de las personas no les molesta esto.
</p>
<p class="consent_content">
    Si siente alguna de estas cosas u otras cosas, asegúrese de decírselo a su mamá o papá.
</p>
<p class="consent_content">
    No tiene que participar en este estudio de investigación si no lo desea. Nadie se enfadará con usted si dice que no. Incluso si dice que sí ahora y cambia de opinión después de comenzar este estudio, puede detenerse y nadie se enojará.
</p>
<p class="consent_content">
    Asegúrese de preguntarle a sus padres si tiene preguntas. También puede pedirles que llamen al Dr. Knight o a su equipo de investigación para que puedan brindarle más información sobre cualquier cosa que no entienda.
</p>' WHERE locale = 'es_MX' AND consent_type = 'child_data';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
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
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamado el microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y los virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500,000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:<br />
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
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
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
    La participación en la investigación es totalmente voluntaria. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento sin penalización ni pérdida de los beneficios a los que usted o su hijo tienen derecho. Usted puede retirar a su hijo del estudio en cualquier momento solicitando la eliminación del perfil en línea de su hijo. Nuestros investigadores seguirán utilizando los datos sobre su hijo que se recopilaron antes de que se retirara. Después de que su hijo se retire del estudio, no se recopilarán más datos.
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
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. El análisis de muestras se realiza utilizando datos de los que se ha eliminado la información de identificación directa, y todos los datos compartidos con los repositorios públicos también se someten a este tratamiento. Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
    La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, saliva, moco, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong><u>Tenga en cuenta</u></strong>:
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'parent_biospecimen';
UPDATE ag.consent_documents SET date_time = NOW(), consent_content = '<p class="consent_title">
    <strong>University of California San Diego<br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación</strong>
</p>
<p class="consent_title">
    The Microsetta Initiative
</p>
<p class="consent_header">
    ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamados microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y virus. Usted está ofreciendo a su hijo como voluntario para este estudio porque quiere saber más sobre el microbioma de su hijo. Los niños, como todos los humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Habrá aproximadamente 500,000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
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
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
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
    La participación en este estudio es completamente voluntaria y usted o su hijo pueden retirarse en cualquier momento simplemente saliendo de la encuesta y eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta en línea. Usted es libre de omitir cualquier pregunta que elija.
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
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
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
    El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los Datos Personales de su hijo. En este documento de consentimiento y en nuestra <a href="https://microsetta.ucsd.edu/privacy-statement/" target="_blank">Declaración de privacidad</a> se incluye información adicional sobre las protecciones que utilizaremos.
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
</p>' WHERE locale = 'es_MX' AND consent_type = 'parent_data';
