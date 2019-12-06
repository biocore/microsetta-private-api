-- Add created_on timestamp for handout kits
ALTER TABLE ag.ag_handout_kits ADD created_on timestamp DEFAULT current_timestamp NOT NULL;

-- Create new ag_handout_barcodes table
CREATE TABLE ag.ag_handout_barcodes (
	kit_id               varchar  NOT NULL,
	barcode              varchar(9)  NOT NULL,
	sample_barcode_file  varchar(13),
	CONSTRAINT idx_ag_handout_barcodes PRIMARY KEY ( barcode )
 );

CREATE INDEX idx_ag_handout_barcodes_1 ON ag.ag_handout_barcodes ( kit_id );

ALTER TABLE ag.ag_handout_barcodes ADD CONSTRAINT fk_ag_handout_barcodes FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode );

-- Copy needed data to new table
INSERT INTO ag.ag_handout_barcodes (kit_id, barcode, sample_barcode_file)
SELECT kit_id, barcode, sample_barcode_file FROM ag.ag_handout_kits;

-- Delete duplicate handout rows and unneeded columns from handouts table
DELETE FROM ag.ag_handout_kits WHERE barcode NOT IN (SELECT max(barcode) FROM ag.ag_handout_kits GROUP BY kit_id);

ALTER TABLE ag.ag_handout_kits DROP COLUMN barcode, DROP COLUMN sample_barcode_file;

-- Add unique constraint to the kit_id column and the foreign key for new table
ALTER TABLE ag.ag_handout_kits ADD PRIMARY KEY (kit_id);
ALTER TABLE ag.ag_handout_barcodes ADD CONSTRAINT fk_ag_handout_barcodes_0 FOREIGN KEY ( kit_id ) REFERENCES ag.ag_handout_kits( kit_id ) ON DELETE CASCADE ON UPDATE CASCADE;