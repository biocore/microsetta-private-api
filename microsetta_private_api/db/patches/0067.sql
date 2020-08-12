-- Break out barcode scans into separate table to allow
-- recording each scan individually.

-- for each sample samples with a non-null scan_date
-- but a null sample_status, deduce the best sample_status to
-- put into barcode
--
-- case 1: (happy path) scanned barcode belongs to AGP, is linked to an
-- account by way of a source, and has collection info.
UPDATE barcodes.barcode
SET sample_status = 'valid'
FROM ag.ag_kit_barcodes, ag.source, ag.account
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND ag_kit_barcodes.source_id = ag.source.id 
AND ag.source.account_id = account.id
AND site_sampled IS NOT null
AND sample_status IS null AND scan_date IS NOT null;

-- case 2: barcode is part of AGP and linked to an account
-- by way of a source but is missing (at least some) collection info
UPDATE barcodes.barcode
SET sample_status = 'no-collection-info'
FROM ag.ag_kit_barcodes, ag.source, ag.account
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND ag_kit_barcodes.source_id = ag.source.id 
AND ag.source.account_id = account.id
AND site_sampled IS null
AND sample_status IS null AND scan_date IS NOT null;

-- case 3: barcode is part of AGP and is linked to an account
-- (by being part of a kit used to create the account)
-- but is NOT linked to a source; collection info not checked.
UPDATE barcodes.barcode
SET sample_status = 'no-associated-consent'
FROM ag.ag_kit_barcodes, ag.account
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND barcodes.barcode.kit_id = ag.account.created_with_kit_id
AND source_id IS null
AND sample_status IS null AND scan_date IS NOT null;

-- case 4: barcode is part of AGP but not linked to an account
-- nor a source; collection info not checked.
UPDATE barcodes.barcode
SET sample_status = 'no-registered-account'
FROM ag.ag_kit_barcodes
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND source_id IS null
AND kit_id IS NOT null
AND kit_id NOT IN (
	SELECT created_with_kit_id
	FROM ag.account
)
AND sample_status IS null AND scan_date IS NOT null;

-- case 5: barcode ISN'T part of AGP project, so we can't
-- deduce anything about its validity, only that we received it
UPDATE barcodes.barcode
SET sample_status = 'received-unknown-validity'
WHERE barcode NOT IN (
	SELECT barcode FROM ag.ag_kit_barcodes
)
AND sample_status IS null AND scan_date IS NOT null;

-- now put in a temporary sample_status for anything that does NOT have a
-- scan date (or sample_status)
UPDATE barcodes.barcode
SET sample_status = 'temp'
WHERE sample_status IS null
AND scan_date IS null;

-- by now we should have set the sample_status for every record in
-- barcodes.barcode. To verify this, alter the table to forbid nulls;
-- if this errors out, it means we missed a case and
-- therefore shouldn't proceed.
ALTER TABLE barcodes.barcode
ALTER COLUMN sample_status DROP NOT NULL;

-- update any past versions of the sample_status strings to the current versions
UPDATE barcodes.barcode
SET sample_status = null
WHERE sample_status = 'not-received';

UPDATE barcodes.barcode
SET sample_status = 'no-associated-source'
WHERE sample_status = 'no-associated-consent';

-- create table barcodes.barcode_scans
CREATE TABLE barcodes.barcode_scans
(
    barcode_scan_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    barcode varchar  NOT NULL,
    scan_timestamp timestamptz NOT NULL,
    sample_status VARCHAR(100) NOT NULL,
    technician_notes VARCHAR,
    CONSTRAINT scans_barcode_pkey PRIMARY KEY (barcode_scan_id),
    CONSTRAINT fk_barcode_scan_to_barcode FOREIGN KEY (barcode)
        REFERENCES barcodes.barcode (barcode)
);

-- copy scan_date, sample_status, and technician_notes
-- from barcode to new barcode_scans for record with
-- a non-null scan date
INSERT into barcodes.barcode_scans
(barcode, scan_timestamp, sample_status, technician_notes) (
	SELECT barcode, scan_date, sample_status, technician_notes
	FROM barcodes.barcode
	WHERE scan_date is not null
);

-- remove scan_date, sample_status, and technician_notes from barcode
ALTER TABLE barcodes.barcode
DROP COLUMN scan_date,
DROP COLUMN sample_status,
DROP COLUMN technician_notes;
