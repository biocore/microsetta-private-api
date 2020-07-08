-- add columns to hold whether or not a project's samples should be banked and if so
-- when their plating should begin plated (optional)
ALTER TABLE barcodes.project ADD COLUMN bank_samples BOOLEAN;
UPDATE barcodes.project SET bank_samples=FALSE WHERE bank_samples IS NULL;
ALTER TABLE barcodes.project ALTER COLUMN bank_samples SET NOT NULL;

ALTER TABLE barcodes.project ADD COLUMN plating_start_date date;