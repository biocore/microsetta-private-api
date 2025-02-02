-- Beginning with cheek samples, we're collecting metadata that are explicitly
-- linked to sample collection (unlike surveys, which are implicitly linked
-- to samples via sources), but not globally collected, and therefore don't
-- belong in the ag.ag_kit_barcodes table. A new table will store these
-- fields and could eventually be extended to a much more robust framework.

-- First, we need to set up an ENUM type to enforce values for the type of
-- product used to last wash their face
CREATE TYPE SAMPLE_SITE_LAST_WASHED_PRODUCT_TYPE AS ENUM ('Soap (includes bar and liquid soap)', 'Foaming face wash', 'Face cleanser', 'Just water', 'Other (e.g. shampoo, body wash, all-in-one or all-over wash)', 'Not sure');

-- Then, create the table to store the data
-- Note: the date and time are stored separately because we're not enforcing
-- either as a required field. As such, using a timestamp type would not be
-- appropriate since it forces us into a both or neither paradigm.
CREATE TABLE ag.ag_kit_barcodes_cheek (
    ag_kit_barcode_id UUID NOT NULL PRIMARY KEY,
    sample_site_last_washed_date DATE,
    sample_site_last_washed_time TIME,
    sample_site_last_washed_product SAMPLE_SITE_LAST_WASHED_PRODUCT_TYPE,

    -- Foreign key relationship on ag_kit_barcode_id
    CONSTRAINT fk_ag_kit_barcode_id FOREIGN KEY (ag_kit_barcode_id) REFERENCES ag.ag_kit_barcodes (ag_kit_barcode_id)
);
