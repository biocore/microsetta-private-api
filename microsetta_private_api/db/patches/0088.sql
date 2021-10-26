-- normalize the datatype of the barcodes field. all other tables 
-- use varchar whereas project_barcodes and ag_handout_barcodes use 
-- a specific width
ALTER TABLE barcodes.project_barcode ALTER COLUMN barcode TYPE VARCHAR;
ALTER TABLE ag.ag_handout_barcodes ALTER COLUMN barcode TYPE VARCHAR;
COMMENT ON TABLE ag.ag_handout_barcodes 
    IS 'This table is deprecated, but retained to maintain historical data';
COMMENT ON TABLE ag.ag_handout_kits
    IS 'This table is deprecated, but retained to maintain historical data';

