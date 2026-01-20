-- This patch extends the existing sample observations for fecal samples to project 166.
-- It follows the structure of patch 0142.sql, with some minor streamlining.

WITH all_observations AS (
    SELECT observation_id FROM barcodes.sample_observations
),
add_projects AS (
    SELECT project_id
    FROM barcodes.project
    WHERE project_id = 166
)
INSERT INTO barcodes.sample_observation_project_associations (observation_id, project_id)
SELECT observation_id, project_id
FROM all_observations
CROSS JOIN add_projects;