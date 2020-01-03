-- June 21, 2016
-- Remove legacy participant_name column and centralize on proper one.
ALTER TABLE ag.ag_kit_barcodes DROP COLUMN participant_name;