-- the weston price response was for some reason missing from the migration in 0081?

UPDATE ag.survey_response 
SET spanish = 'Dieta Weston-Price o alguna otra dieta con bajo contenido de cereales y alimentos procesados',     
    french = 'Weston-Price ou tout autre régime comprenant peu de céréales et d’aliments transformés',     
    chinese = 'Weston-Price 或其他低谷物、低加工饮食' 
WHERE american = 'Weston-Price, or other low-grain, low processed food diet';
