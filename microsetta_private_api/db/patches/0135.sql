-- Jan 26, 2024
-- Add sample metadata update timestamp
ALTER TABLE ag.ag_kit_barcodes
    ADD COLUMN last_update timestamp with time zone;

COMMENT ON COLUMN ag.ag_kit_barcodes.last_update
    IS 'Sample metadata update timestamp';