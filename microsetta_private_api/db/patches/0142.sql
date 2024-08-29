-- August 26, 2024
-- Patching 0141 Sample Observation Project Association 
-- to add projects 118 and 160.

WITH all_observations AS (
    SELECT observation_id FROM barcodes.sample_observations
),
add_projects AS (
    SELECT project_id
    FROM (VALUES (118), (160)) AS np(project_id)
    WHERE EXISTS (
        SELECT 1 FROM barcodes.project WHERE project.project_id = np.project_id
    )
)
INSERT INTO barcodes.sample_observation_project_associations (observation_id, project_id)
SELECT observation_id, project_id
FROM all_observations
CROSS JOIN add_projects;
