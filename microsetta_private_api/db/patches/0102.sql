-- BEGIN ADDRESS VERIFICATION CHANGES
-- Drop old indices that only include address_1 and address_2
DROP INDEX campaign.source_address_composite;
DROP INDEX campaign.result_address_composite;

-- Add address_3 columns
ALTER TABLE campaign.melissa_address_queries ADD COLUMN source_address_3 VARCHAR;
ALTER TABLE campaign.melissa_address_queries ADD COLUMN result_address_3 VARCHAR;

-- Create new indices that include address_3
CREATE INDEX idx_melissa_source_address ON campaign.melissa_address_queries (source_address_1, source_address_2, source_address_3, source_postal, source_country, result_processed);
CREATE INDEX idx_melissa_result_address ON campaign.melissa_address_queries (result_address_1, result_address_2, result_address_3, result_postal, result_country, result_processed);
-- END ADDRESS VERIFICATION CHANGES

-- BEGIN SURVEY CHANGES FOR SPAIN
-- Add columns for Spain to the three necessary survey tables
ALTER TABLE ag.survey_group ADD COLUMN spain VARCHAR;
ALTER TABLE ag.survey_question ADD COLUMN spain VARCHAR;
ALTER TABLE ag.survey_response ADD COLUMN spain VARCHAR;

-- Per Alejandra, the vast majority of the translations are the same for Spain as they were for Mexico.
-- Therefore, we're going to copy those values into the new columns, then update the exceptions by hand.
UPDATE ag.survey_group SET spain = spanish;
UPDATE ag.survey_question SET spain = spanish;
UPDATE ag.survey_response SET spain = spanish;

-- Changes to address specific questions/responses
UPDATE ag.survey_response SET spain = 'aumentó más de 10 libras (5kg)' WHERE american = 'Increased more than 10 pounds';
UPDATE ag.survey_response SET spain = 'se redujo más de 10 libras (5kg)' WHERE american = 'Decreased more than 10 pounds';
UPDATE ag.survey_response SET spain = 'Alubias fermentadas/miso/natto' WHERE american = 'Fermented beans/Miso/Natto';
UPDATE ag.survey_response SET spain = 'Pocos días a la semana' WHERE american = 'A few days per week';

UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana cocina y come comidas caseras? (Excluya las comidas listas para consumir, como la pizza, fideos instantaneos, croquetas, empanaillas)' WHERE survey_question_id = 57;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana come alimentos precocinados o listos para consumir (p. ej., pizzas, fideos instantaneos, croquetas, empanadillas)?' WHERE survey_question_id = 58;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume al menos 2-3 raciones de fruta al día? (1 ración = 1/2 taza de fruta; 1 fruta mediana; 120ml de jugo de frutas 100 % natural).' WHERE survey_question_id = 61;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume al menos 2-3 raciones de verdura al día (incluidas las papas)? (1 ración = 1/2 taza de verduras/papas; 1 taza de verduras de hoja crudas).' WHERE survey_question_id = 62;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume una o más raciones de verduras o productos vegetales fermentados al día? (1 ración = 1/2 taza de chucrut, kimchi o verduras fermentadas o 1 taza de kombucha).' WHERE survey_question_id = 63;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume al menos 2 raciones de leche o queso al día? (1 ración = 1 taza de leche o yogur; 50gr de queso).' WHERE survey_question_id = 64;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume productos sin lactosa (bebida de soja, bebida de almendras, y leche sin lactosa etc.)?' WHERE survey_question_id = 65;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántos días a la semana consume aperitivos salados (patatas chips, tortitas de maíz, galletas saladas, palomitas de maíz con mantequilla, patatas fritas, etc.)?' WHERE survey_question_id = 71;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántos días a la semana consume alimentos azucarados o reposteria comercial (tartas, galletas, bollos, rosquillas, pastelillos, chocolate, etc.) al menos una vez al día?' WHERE survey_question_id = 72;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántos días a la semana cocina con aceite de oliva (o usa aceite de oliva para aliñar ensaladas)?' WHERE survey_question_id = 73;
UPDATE ag.survey_question SET spain = '¿Consume huevos enteros (no huevo líquido envasado, ni solo claras de huevo)?' WHERE survey_question_id = 74;
UPDATE ag.survey_question SET spain = '¿Bebe 16 onzas (500 ml) o más de bebidas carbonatadas y/o azucaradas como refrescos, colas, bebidas carbonatadas bajas en calorías, o zumos de fruta (que no incluyan zumo 100 % natural) al día? (1 lata de refresco = 355ml).' WHERE survey_question_id = 75;
UPDATE ag.survey_question SET spain = '¿Consume bebidas carbonatadas bajas en calorías con endulzantes artificiales?' WHERE survey_question_id = 157;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿con qué frecuencia consume remolacha (cruda, enlatada, en escabeche o asada) a la semana? (1 ración = 1 taza cruda o cocida)' WHERE survey_question_id = 236;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿con qué frecuencia consume diferentes tipos de proteina vegetal incluyendo tofu, tempeh, edamame, lentejas, garbanzos, cacahuetes, almendras, nueces o quinua a la semana?' WHERE survey_question_id = 237;
UPDATE ag.survey_question SET spain = 'Indique cualquier otro dato sobre usted que cree que podría afectar a sus propios microorganismos.' WHERE survey_question_id = 116;
UPDATE ag.survey_question SET spain = 'Por lo general, ¿cuántas veces a la semana consume una o más raciones de verduras o alimentos fermentados de origen vegetal al día? (1 ración = 1/2 taza de chucrut, kimchi o verduras fermentadas o 1 taza de kombucha).' WHERE survey_question_id = 165;
UPDATE ag.survey_question SET spain = 'Por favor, piense en su nivel de bienestar actual. Cuando piense en su bienestar, piense en su salud física, en su salud emocional, en cualquier desafío que esté experimentando, en las personas de su vida y en las oportunidades o recursos que tiene a su disposición. ¿Cómo describiría su nivel de bienestar actual?' WHERE survey_question_id = 210;
UPDATE ag.survey_question SET spain = '¿Ha sospechado que pueda tener infección por coronavirus/COVID-19?' WHERE survey_question_id = 212;
UPDATE ag.survey_question SET spain = '¿Cuántas veces ha salido de su casa por cualquier razón, incluido el trabajo (por ejemplo, ha dejado su casa para ir a tiendas, parques, etc.)?' WHERE survey_question_id = 218;
UPDATE ag.survey_question SET spain = 'Durante las últimas 2 semanas, ¿con qué frecuencia le ha faltado interés o placer para hacer las cosas?' WHERE survey_question_id = 221;
UPDATE ag.survey_question SET spain = '¿Ha participado en la atención directa al paciente que involucre pacientes con COVID-19 confirmados en los últimos 7 días?' WHERE survey_question_id = 227;
UPDATE ag.survey_question SET spain = 'Describa la calidad de la evacuación. Utilice el siguiente cuadro a modo de referencia:<br/><img src="/static/img/es_es/bristol_stool.jpg" id="bristol-chart">' WHERE survey_question_id = 38;

-- END SURVEY CHANGES FOR SPAIN