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

-- set a stylizable ID for bristol images
UPDATE ag.survey_question
SET
american = 'Describe the quality of your bowel movements. Use the chart below as a reference:<br/><img src="/static/img/en_us/bristol_stool.jpg" id="bristol-chart">',
british = 'Describe the quality of your bowel movements. Use the chart below as a reference:<br/><img src="/static/img/en_us/bristol_stool.jpg" id="bristol-chart">',
spanish = 'Describa la calidad de la evacuación. Utilice el siguiente cuadro a modo de referencia:<br/><img src="/static/img/es_mx/bristol_stool.jpg" id="bristol-chart">',
french = 'Veuillez décrire la qualité de vos selles. Vous pouvez utiliser le tableau ci-dessous comme référence:<br/><img src="/static/img/fr_fr/bristol_stool.jpg" id="bristol-chart">',
chinese = '描述您的排便质量。使用下面的图表作为参考：<br/><img src="/static/img/zh_cn/bristol_stool.jpg" id="bristol-chart">'
WHERE
survey_question_id = 38;
