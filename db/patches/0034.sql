-- Feb 16, 2016
-- Add submitted to EBI tracking
ALTER TABLE ag.ag_kit_barcodes ADD deposited bool DEFAULT 'F' NOT NULL;
COMMENT ON COLUMN ag.ag_kit_barcodes.deposited IS 'Deposited to EBI';