-- May 13, 2024
-- Create table to store observation categories
CREATE TABLE barcodes.sample_observation_categories (
    category VARCHAR(255) PRIMARY KEY
);

-- Insert predefined observation categories
INSERT INTO barcodes.sample_observation_categories (category)
VALUES ('Sample'), ('Swab'), ('Tube');

-- Create table to store sample observations
CREATE TABLE barcodes.sample_observations (
    observation_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category VARCHAR(255) NOT NULL,
    observation VARCHAR(255) NOT NULL,
    FOREIGN KEY (category) REFERENCES barcodes.sample_observation_categories(category),
    UNIQUE (category, observation)
);

-- Create table to store associations between observations and projects
CREATE TABLE barcodes.sample_observation_project_associations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    observation_id UUID NOT NULL,
    project_id INT NOT NULL,
    FOREIGN KEY (observation_id) REFERENCES barcodes.sample_observations(observation_id),
    FOREIGN KEY (project_id) REFERENCES barcodes.project(project_id),
    UNIQUE (observation_id, project_id)
);

-- Insert predefined observations and associate them with a project
WITH inserted_observations AS (
    INSERT INTO barcodes.sample_observations (category, observation)
    VALUES
    ('Tube', 'Tube is not intact'),
    ('Tube', 'Screw cap is loose'),
    ('Tube', 'Insufficient ethanol'),
    ('Tube', 'No ethanol'),
    ('Swab', 'No swab in tube'),
    ('Swab', 'Multiple swabs in tube'),
    ('Swab', 'Incorrect swab type'),
    ('Sample', 'No visible sample'),
    ('Sample', 'Excess sample on swab')
    RETURNING observation_id, category, observation
)
INSERT INTO barcodes.sample_observation_project_associations (observation_id, project_id)
SELECT observation_id, 1
FROM inserted_observations;

-- Create table to store observation ids associated with barcode scans ids
CREATE TABLE barcodes.sample_barcode_scan_observations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    barcode_scan_id UUID NOT NULL,
    observation_id UUID NOT NULL,
    FOREIGN KEY (barcode_scan_id) REFERENCES barcodes.barcode_scans(barcode_scan_id),
    FOREIGN KEY (observation_id) REFERENCES barcodes.sample_observations(observation_id),
    UNIQUE (barcode_scan_id, observation_id)
);
