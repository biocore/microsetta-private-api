-- This script adds two columns to the barcodes.barcode table to enable
-- adding information when scanned by a technician

ALTER TABLE barcodes.barcode
ADD COLUMN sample_status VARCHAR(100),
ADD COLUMN technician_notes VARCHAR;
