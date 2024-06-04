-- This database patch copies two samples into new barcodes to reflect
-- adjustments that were necessary in the wet lab. We don't believe this
-- will be an ongoing need, but if it proves to be, check for new
-- barcode-related tables before using this as a template.

-- Begin copying X00236845 to 0364352596
INSERT INTO barcodes.barcode (barcode, assigned_on, status, sample_postmark_date, biomass_remaining, sequencing_status, obsolete, create_date_time, kit_id)
    SELECT '0364352596', assigned_on, status, sample_postmark_date, biomass_remaining, sequencing_status, obsolete, create_date_time, kit_id
    FROM barcodes.barcode
    WHERE barcode = 'X00236845';

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, '0364352596'
    FROM barcodes.project_barcode
    WHERE barcode = 'X00236845';

-- I'm omitting the sample_barcode_file and sample_barcode_file_md5 as they're
-- no longer used and it would be inappropriate to directly clone a different
-- barcode's associated file.
INSERT INTO ag.ag_kit_barcodes (ag_kit_id, barcode, site_sampled, sample_date, sample_time, notes, moldy, overloaded, other, other_text, date_of_last_email, results_ready, withdrawn, refunded, deposited, source_id, latest_sample_information_update)
    SELECT ag_kit_id, '0364352596', site_sampled, sample_date, sample_time, notes, moldy, overloaded, other, other_text, date_of_last_email, results_ready, withdrawn, refunded, deposited, source_id, latest_sample_information_update
    FROM ag.ag_kit_barcodes
    WHERE barcode = 'X00236845';

INSERT INTO ag.source_barcodes_surveys (barcode, survey_id)
    SELECT '0364352596', survey_id
    FROM ag.source_barcodes_surveys
    WHERE barcode = 'X00236845';

INSERT INTO barcodes.barcode_scans (barcode, scan_timestamp, sample_status, technician_notes)
    SELECT '0364352596', scan_timestamp, sample_status, technician_notes
    FROM barcodes.barcode_scans
    WHERE barcode = 'X00236845';

INSERT INTO ag.vioscreen_registry (account_id, source_id, sample_id, vio_id, deleted, registration_code)
    WITH temp_1 AS (
        SELECT vr.account_id, vr.source_id, vr.vio_id, vr.deleted, vr.registration_code
        FROM ag.vioscreen_registry vr
        INNER JOIN ag.ag_kit_barcodes akb ON vr.sample_id = akb.ag_kit_barcode_id
        WHERE akb.barcode = 'X00236845'
    ),
    temp_2 AS (
        SELECT ag_kit_barcode_id
        FROM ag.ag_kit_barcodes
        WHERE barcode = '0364352596'
    )
    SELECT temp_1.account_id, temp_1.source_id, temp_2.ag_kit_barcode_id, temp_1.vio_id, temp_1.deleted, temp_1.registration_code FROM temp_1, temp_2;
-- End copying X00236845 to 0364352596

-- Begin copying 000031307 to 0364406520
INSERT INTO barcodes.barcode (barcode, assigned_on, status, sample_postmark_date, biomass_remaining, sequencing_status, obsolete, create_date_time, kit_id)
    SELECT '0364406520', assigned_on, status, sample_postmark_date, biomass_remaining, sequencing_status, obsolete, create_date_time, kit_id
    FROM barcodes.barcode
    WHERE barcode = '000031307';

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, '0364406520'
    FROM barcodes.project_barcode
    WHERE barcode = '000031307';

-- I'm omitting the sample_barcode_file and sample_barcode_file_md5 as they're
-- no longer used and it would be inappropriate to directly clone a different
-- barcode's associated file.
INSERT INTO ag.ag_kit_barcodes (ag_kit_id, barcode, site_sampled, sample_date, sample_time, notes, moldy, overloaded, other, other_text, date_of_last_email, results_ready, withdrawn, refunded, deposited, source_id, latest_sample_information_update)
    SELECT ag_kit_id, '0364406520', site_sampled, sample_date, sample_time, notes, moldy, overloaded, other, other_text, date_of_last_email, results_ready, withdrawn, refunded, deposited, source_id, latest_sample_information_update
    FROM ag.ag_kit_barcodes
    WHERE barcode = '000031307';

INSERT INTO ag.source_barcodes_surveys (barcode, survey_id)
    SELECT '0364406520', survey_id
    FROM ag.source_barcodes_surveys
    WHERE barcode = '000031307';

INSERT INTO barcodes.barcode_scans (barcode, scan_timestamp, sample_status, technician_notes)
    SELECT '0364406520', scan_timestamp, sample_status, technician_notes
    FROM barcodes.barcode_scans
    WHERE barcode = '000031307';

INSERT INTO ag.vioscreen_registry (account_id, source_id, sample_id, vio_id, deleted, registration_code)
    WITH temp_1 AS (
        SELECT vr.account_id, vr.source_id, vr.vio_id, vr.deleted, vr.registration_code
        FROM ag.vioscreen_registry vr
        INNER JOIN ag.ag_kit_barcodes akb ON vr.sample_id = akb.ag_kit_barcode_id
        WHERE akb.barcode = '000031307'
    ),
    temp_2 AS (
        SELECT ag_kit_barcode_id
        FROM ag.ag_kit_barcodes
        WHERE barcode = '0364406520'
    )
    SELECT temp_1.account_id, temp_1.source_id, temp_2.ag_kit_barcode_id, temp_1.vio_id, temp_1.deleted, temp_1.registration_code FROM temp_1, temp_2;
-- End copying 000031307 to 0364406520
