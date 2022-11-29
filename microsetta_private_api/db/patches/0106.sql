CREATE TABLE barcodes.bulk_barcode_scans (
    bulk_barcode_scan_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    scan_date DATE,
    scan_time TIME,
    location_cell VARCHAR(10),
    location_column VARCHAR(10),
    location_row VARCHAR(10),
    barcode VARCHAR NOT NULL,
    rack_id VARCHAR,
    CONSTRAINT bulk_scans_barcode_pkey PRIMARY KEY (bulk_barcode_scan_id),
    CONSTRAINT fk_barcode_scan_to_barcode FOREIGN KEY (barcode)
        REFERENCES barcodes.barcode (barcode)
)
