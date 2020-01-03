ALTER TABLE ag.ag_handout_kits ALTER COLUMN kit_id SET NOT NULL;

ALTER TABLE ag.ag_handout_kits ALTER COLUMN barcode SET NOT NULL;

ALTER TABLE ag.barcode_exceptions ALTER COLUMN barcode SET NOT NULL;

ALTER TABLE ag.ag_handout_kits ADD CONSTRAINT pk_ag_handout_kits PRIMARY KEY ( kit_id, barcode ) ;

ALTER TABLE ag.ag_handout_kits ADD CONSTRAINT idx_ag_handout_kits UNIQUE ( barcode ) ;

ALTER TABLE ag.ag_handout_kits ADD CONSTRAINT fk_ag_handout_kits FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode )    ;

ALTER TABLE ag.barcode_exceptions ADD CONSTRAINT pk_barcode_exceptions PRIMARY KEY ( barcode ) ;

ALTER TABLE ag.barcode_exceptions ADD CONSTRAINT fk_barcode_exceptions FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode )    ;

