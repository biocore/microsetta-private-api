-- create table to track vioscreen survey ids
CREATE TABLE ag.vioscreen_registry
(
    account_id uuid NOT NULL,
    source_id uuid NOT NULL,
    sample_id uuid,
    vio_id varchar NOT NULL,
    CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES ag.account( id ),
    CONSTRAINT fk_source FOREIGN KEY (source_id) REFERENCES ag.source( id ),
    CONSTRAINT fk_sample FOREIGN KEY (sample_id) REFERENCES ag.ag_kit_barcodes( ag_kit_barcode_id )
);

CREATE INDEX vio_reg_by_vio_id ON ag.vioscreen_registry (vio_id);
CREATE UNIQUE INDEX vio_reg_by_sample ON ag.vioscreen_registry (account_id, source_id, sample_id);
