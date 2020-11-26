-- create table to summarize sequencing results for each barcode+preparation pairing
CREATE TABLE barcodes.preparation
(
    barcode varchar NOT NULL,
    preparation_id int NOT NULL,
    preparation_type varchar NOT NULL,
    num_sequences bigint NOT NULL,
    CONSTRAINT fk_barcode FOREIGN KEY ( barcode ) REFERENCES barcodes.barcode( barcode )
);

CREATE UNIQUE INDEX preparation_barcode_prep_id ON barcodes.preparation (barcode, preparation_id);
CREATE UNIQUE INDEX preparation_prep_id_barcode ON barcodes.preparation (preparation_id, barcode);
