-- spanish responses were not reflected in this table
ALTER TABLE ag.survey_response ADD COLUMN spanish VARCHAR;
UPDATE ag.survey_response
    SET spanish=survey_question_response.spanish
    FROM ag.survey_question_response
    WHERE survey_response.american=survey_question_response.response;

ALTER TABLE ag.survey_group ADD COLUMN spanish VARCHAR;
UPDATE ag.survey_group SET spanish='Información general sobre la dieta' WHERE group_order=0;
UPDATE ag.survey_group SET spanish='Información general' WHERE group_order=1;
UPDATE ag.survey_group SET spanish='Información general sobre higiene y estilo de vida' WHERE group_order=2;
UPDATE ag.survey_group SET spanish='Información general de salud' WHERE group_order=3;
UPDATE ag.survey_group SET spanish='Información dietética detallada' WHERE group_order=4;
UPDATE ag.survey_group SET spanish='¿Algo más?' WHERE group_order=5;
UPDATE ag.survey_group SET spanish='Información sobre mascotas' WHERE group_order=-2;
UPDATE ag.survey_group SET spanish='Comidas fermentadas' WHERE group_order=-3;
UPDATE ag.survey_group SET spanish='Surfistas' WHERE group_order=-4;
UPDATE ag.survey_group SET spanish='Microbioma personal' WHERE group_order=-5;
UPDATE ag.survey_group SET spanish='Cuestionario COVID19' WHERE group_order=-6;
UPDATE ag.survey_group SET spanish='Iniciativa Microsetta' WHERE group_order=-1;
