-- August 26, 2024
-- Patching 0141 Sample Observation Project Association 
-- to add projects 118 and 160.

WITH all_observations AS (
    SELECT observation_id FROM barcodes.sample_observations
)
INSERT INTO barcodes.sample_observation_project_associations (observation_id, project_id)
SELECT observation_id, project_id
FROM all_observations
CROSS JOIN (VALUES (118), (160)) AS new_projects(project_id);
