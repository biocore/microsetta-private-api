-- Updates the link for the bristol stool chart
-- in surveys to point to localized directories

UPDATE ag.survey_question
SET
american = 'Describe the quality of your bowel movements. Use the chart below as a reference:<br/><img src="/static/img/en_us/bristol_stool.jpg" id="bristol-chart">',
british = 'Describe the quality of your bowel movements. Use the chart below as a reference:<br/><img src="/static/img/en_us/bristol_stool.jpg" id="bristol-chart">',
spanish = 'Describa la calidad de la evacuación. Utilice el siguiente cuadro a modo de referencia:<br/><img src="/static/img/es_mx/bristol_stool.jpg" id="bristol-chart">',
french = 'Veuillez décrire la qualité de vos selles. Vous pouvez utiliser le tableau ci-dessous comme référence:<br/><img src="/static/img/fr_fr/bristol_stool.jpg" id="bristol-chart">',
chinese = '描述您的排便质量。使用下面的图表作为参考：<br/><img src="/static/img/zh_cn/bristol_stool.jpg" id="bristol-chart">'
WHERE
survey_question_id = 38;
