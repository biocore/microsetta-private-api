-- Correct two problems in the population of barcode_scans in 0067.sql:

-- Problem 1: valid sample status should be 'sample-is-valid' rather than 'valid'
-- per request from wet lab to revert to original terminology.  Change ALL instances
-- of 'valid' to 'sample-is-valid'.
UPDATE barcodes.barcode_scans
SET sample_status = 'sample-is-valid'
WHERE sample_status = 'valid';

-- Problem 2: filled site_sampled was used as a proxy for having collection info,
-- but environmental sources don't have site_sampled filled in when they
-- are collected.  Identify all scans of barcodes that are part of American Gut,
-- are associated with a source, are for a sample of the type "environmental", and
-- have been collected by the participant (as evidenced by the sample_date field
-- being filled).  Additionally, look only at scans meeting the above criteria
-- that additionally were done AFTER the participant-reported sample_date (so after
-- the sample was collected) AND that have a sample_status of "no-collection-info".
-- Given the foregoing conditions, this status is incorrect as the sample is valid;
-- change sample_status in these cases to 'sample-is-valid'.
UPDATE barcodes.barcode_scans
SET sample_status = 'sample-is-valid'
FROM ag.ag_kit_barcodes, ag.source
WHERE barcode_scans.barcode = ag_kit_barcodes.barcode
AND ag_kit_barcodes.source_id = source.id
AND source.source_type = 'environmental'
AND ag_kit_barcodes.sample_date IS not null
AND barcode_scans.scan_timestamp >= ag_kit_barcodes.sample_date
AND barcode_scans.sample_status = 'no-collection-info';