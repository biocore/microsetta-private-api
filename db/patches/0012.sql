CREATE SCHEMA barcodes;

ALTER TABLE ag.barcode SET SCHEMA barcodes;
ALTER TABLE ag.project SET SCHEMA barcodes;
ALTER TABLE ag.project_barcode SET SCHEMA barcodes;
ALTER TABLE ag.plate SET SCHEMA barcodes;
ALTER TABLE ag.barcode_exceptions SET SCHEMA barcodes;
ALTER TABLE ag.plate_barcode SET SCHEMA barcodes;

--Do not allow null participant names
ALTER TABLE ag.ag_login_surveys ALTER COLUMN participant_name SET NOT NULL;