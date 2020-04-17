CREATE TABLE barcodes.kit (
    kit_uuid uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    kit_id VARCHAR NOT NULL CONSTRAINT unq_kit_id UNIQUE,
    fedex_tracking VARCHAR NULL,
    address VARCHAR NULL
);

--ALTER TABLE barcodes.barcode ADD COLUMN kit_id VARCHAR;
ALTER TABLE barcodes.barcode ADD CONSTRAINT fk_barcode_kit_id
    FOREIGN KEY (kit_id) REFERENCES barcodes.kit (kit_id);
