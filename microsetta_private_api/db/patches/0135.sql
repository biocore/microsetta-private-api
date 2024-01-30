-- Jan 26, 2024
-- Add sample information update timestamp
-- For UI enhancement. 
-- We are not nulling the field out, though it may become necessary if used outside of the UI.
ALTER TABLE ag.ag_kit_barcodes
    ADD COLUMN latest_sample_information_update timestamp with time zone;

COMMENT ON COLUMN ag.ag_kit_barcodes.latest_sample_information_update
    IS 'Sample information update timestamp.';