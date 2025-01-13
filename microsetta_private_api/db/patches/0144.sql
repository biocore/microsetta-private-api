-- Beginning with cheek samples, we're collecting metadata that are explicitly
-- linked to sample collection (unlike surveys, which are implicitly linked
-- to samples via sources), but not globally collected, and therefore don't
-- belong in the ag.ag_kit_barcodes table. A new table will store these
-- fields and could eventually be extended to a much more robust framework.

-- First, we're going to set up a table to enforce validation. Specifically,
-- we want to ensure that we don't receive any unexpected field names, and
-- the values we receive are conformant to either an expected format or a set
-- of pre-defined values.
CREATE TYPE BARCODE_METADATA_VALIDATION_TYPE AS ENUM ('date_or_time', 'set_value');
CREATE TABLE ag.ag_kit_barcodes_metadata_validation (
    field_name VARCHAR NOT NULL PRIMARY KEY,
    validation_type BARCODE_METADATA_VALIDATION_TYPE NOT NULL,
    validation_value TEXT NOT NULL
);

-- Sets of pre-defined values will use | as delimiter, as that is unlikely to
-- appear in any foreseeable string we'll be using.
INSERT INTO ag.ag_kit_barcodes_metadata_validation (field_name, validation_type, validation_value) VALUES
    ('sample_site_last_washed_date', 'date_or_time', '%m/%d/%Y'), -- MM/DD/YYYY format, e.g. '01/15/2024'
    ('sample_site_last_washed_time', 'date_or_time', '%I:%M %p'), -- H:MM AM/PM format, e.g. '3:05 PM'
    ('sample_site_last_washed_product', 'set_value', 'Soap (includes bar and liquid soap)|Foaming face wash|Face cleanser|Just water|Other (e.g. shampoo, body wash, all-in-one or all-over wash)|Not sure');

-- Then, create the table to store the data
CREATE TABLE ag.ag_kit_barcodes_metadata (
    ag_kit_barcode_id UUID NOT NULL,
    field_name VARCHAR NOT NULL,
    field_value VARCHAR NOT NULL,

    -- Foreign key relationship on ag_kit_barcode_id
    CONSTRAINT fk_ag_kit_barcode_id FOREIGN KEY (ag_kit_barcode_id) REFERENCES ag.ag_kit_barcodes (ag_kit_barcode_id),

    -- Foreign key relationship on ag_kit_barcodes_metadata_validation
    CONSTRAINT fk_ag_kit_barcodes_metadata_field_name FOREIGN KEY (field_name) REFERENCES ag.ag_kit_barcodes_metadata_validation(field_name),

    -- Unique key on the combination of ag_kit_barcode_id and field_name
    CONSTRAINT uk_ag_kit_barcode_id_field_name UNIQUE (ag_kit_barcode_id, field_name)
);
