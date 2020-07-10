-- create table barcodes.barcode_scans
CREATE TABLE barcodes.barcode_scans
(
    barcode_scan_id uuid DEFAULT uuid_generate_v4(),
    barcode character(9) COLLATE pg_catalog."default" NOT NULL,
    scan_timestamp timestamptz,
    sample_status character varying(100) COLLATE pg_catalog."default",
    technician_notes character varying COLLATE pg_catalog."default",
    CONSTRAINT scans_barcode_pkey PRIMARY KEY (barcode_scan_id),
    CONSTRAINT fk_barcode_scan_to_barcode FOREIGN KEY (barcode)
        REFERENCES barcodes.barcode (barcode) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE barcodes.barcode_scans
    OWNER to postgres;

GRANT ALL ON TABLE barcodes.barcode_scans TO postgres;

-- for each sample samples with a non-null scan_date
-- but a null sample_status, deduce the best sample_status to
-- put into barcode
--
-- case 1: barcode ISN'T part of AGP project, so we can't
-- deduce anything about its validity, only that we received it
UPDATE barcodes.barcode
SET sample_status = 'received-unknown-validity'
WHERE scan_date IS NOT null
AND sample_status IS null
AND barcode NOT IN (
	SELECT barcode FROM ag.ag_kit_barcodes
)
AND barcode NOT IN (
	SELECT barcode FROM ag.ag_handout_barcodes
);

-- case 2: barcode is part of AGP but not linked to an account
-- (nor a source)
UPDATE barcodes.barcode
SET sample_status = 'invalid-no-account'
FROM ag.ag_kit_barcodes
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND scan_date IS NOT null
AND sample_status IS null
AND source_id IS null
AND kit_id IS NOT null
AND kit_id NOT IN (
	SELECT created_with_kit_id
	FROM ag.account
);

-- case 3: barcode is part of AGP and is linked to an account
-- (inferred because its sample_status was not set by in case 2)
-- but is not linked to a source
UPDATE barcodes.barcode
SET sample_status = 'invalid-no-source'
FROM ag.ag_kit_barcodes
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND scan_date IS NOT null
AND sample_status IS null
AND source_id IS null;

-- case 4: barcode is part of AGP and linked to an account
-- and a source but is missing (at least some) collection
-- info; collection date is used as a proxy for collection info
-- because all kinds of sources require collection_date for
-- a sample (whereas, e.g., environmental sources don't require
-- site_sampled, etc).
UPDATE barcodes.barcode
SET sample_status = 'invalid-no-collection-info'
FROM ag.ag_kit_barcodes
WHERE barcode.barcode = ag_kit_barcodes.barcode
AND scan_date IS NOT null
AND sample_status IS null
AND source_id IS NOT null
AND site_sampled IS null;

-- case 5: (happy path) barcode has all the info it needs
-- (inferred because its sample status was not set by any
-- of the error cases above) so it is valid
UPDATE barcodes.barcode
SET sample_status = 'valid'
WHERE scan_date is not null
and sample_status is null;

-- update any past versions of the sample_status strings to the current versions
update barcodes.barcode
set sample_status = null
where sample_status = 'not-received';

update barcodes.barcode
set sample_status = 'valid'
where sample_status = 'sample-is-valid';

update barcodes.barcode
set sample_status = 'invalid-no-account'
where sample_status = 'no-registered-account';

update barcodes.barcode
set sample_status = 'invalid-no-source'
where sample_status = 'no-associated-consent';

update barcodes.barcode
set sample_status = 'invalid-inconsistencies'
where sample_status = 'sample-has-inconsistencies';

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
