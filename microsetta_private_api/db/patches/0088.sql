-- normalize the datatype of the barcodes field. all other tables 
-- use varchar whereas project_barcodes uses a specific width
ALTER TABLE barcodes.project_barcode ALTER COLUMN barcode TYPE VARCHAR;
