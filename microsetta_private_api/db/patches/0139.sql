-- May 13, 2024
-- Create two tables for observation categories and observation errors list
-- Add observations column to barcode_scans table
CREATE TABLE observation_categories (
    categories VARCHAR(255) PRIMARY KEY
);

INSERT INTO observation_categories (categories) VALUES ('Sample'), ('Swab'), ('Tube');

CREATE TABLE observation_errors (
    category VARCHAR(255),
    error VARCHAR(255),
    project_id INT,
    FOREIGN KEY (category) REFERENCES observation_categories(categories)
);

INSERT INTO observation_errors (category, error, project_id) VALUES
('Tube', 'Tube is not intact', 118),
('Tube', 'Screw cap is loose', 118),
('Tube', 'Insufficient ethanol', 118),
('Tube', 'No ethanol', 118),
('Swab', 'No swab in tube', 118),
('Swab', 'Multiple swabs in tube', 118),
('Swab', 'Incorrect swab type', 118),
('Sample', 'No visible sample', 118),
('Sample', 'Excess sample on swab', 118);

ALTER TABLE barcodes.barcode_scans ADD COLUMN observations VARCHAR(255);
