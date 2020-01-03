--Aug 12, 2015
-- Remove the test barcodes (900000000 and above) so new barcode system works
DO $do$
DECLARE
	bc varchar;
	sid varchar;
	agl uuid;
	agk uuid;
	pn varchar;
BEGIN
-- Wipe out test barcodes that are already attached to kits and surveys
FOR bc, sid IN
	SELECT barcode, survey_id FROM ag.ag_kit_barcodes WHERE barcode::integer >= 800000000
LOOP
	DELETE FROM ag.survey_answers WHERE survey_id = sid;
	DELETE FROM ag.survey_answers_other WHERE survey_id = sid;
	DELETE FROM ag.ag_login_surveys WHERE survey_id = sid RETURNING participant_name INTO pn;
	DELETE from ag.ag_kit_barcodes WHERE barcode = bc RETURNING ag_kit_id INTO agk;

	DELETE FROM barcodes.barcode_exceptions WHERE barcode = bc;
	DELETE FROM barcodes.plate_barcode WHERE barcode = bc;
	DELETE FROM barcodes.project_barcode WHERE barcode = bc;
	DELETE FROM barcodes.barcode WHERE barcode = bc;

	DELETE FROM ag.ag_consent WHERE ag_login_id = (SELECT ag_login_id FROM ag.ag_kit WHERE ag_kit_id = agk) AND participant_name = pn;
	BEGIN
		DELETE FROM ag.ag_kit WHERE ag_kit_id = agk;
	EXCEPTION WHEN foreign_key_violation THEN CONTINUE;
		--Do nothing on exception because that means there are still barcodes attached to the kit
	END;
END LOOP;

-- Wipe out test barcodes that are  attached to handout kits
FOR bc IN
	SELECT barcode FROM ag.ag_handout_barcodes WHERE barcode::integer >= 800000000
LOOP
	DELETE FROM ag.ag_handout_barcodes WHERE barcode = bc RETURNING kit_id INTO agk;

	DELETE FROM barcodes.barcode_exceptions WHERE barcode = bc;
	DELETE FROM barcodes.plate_barcode WHERE barcode = bc;
	DELETE FROM barcodes.project_barcode WHERE barcode = bc;
	DELETE FROM barcodes.barcode WHERE barcode = bc;

	BEGIN
		DELETE FROM ag.ag_handout_kits WHERE kit_id = agk;
	EXCEPTION WHEN foreign_key_violation THEN CONTINUE;
		--Do nothing on exception because that means there are still barcodes attached to the kit
	END;
END LOOP;

-- Wipe out test barcodes that are not attached to AG
FOR bc IN
	SELECT barcode FROM barcodes.barcode WHERE barcode::integer >= 800000000
LOOP
	DELETE FROM barcodes.barcode_exceptions WHERE barcode = bc;
	DELETE FROM barcodes.plate_barcode WHERE barcode = bc;
	DELETE FROM barcodes.project_barcode WHERE barcode = bc;
	DELETE FROM barcodes.barcode WHERE barcode = bc;
END LOOP;
END $do$;

-- Change name of column so it reflects what it stores
ALTER TABLE barcodes.barcode RENAME COLUMN create_date_time TO assigned_on;
ALTER TABLE barcodes.barcode ALTER COLUMN assigned_on DROP DEFAULT;
ALTER TABLE barcodes.barcode ALTER COLUMN assigned_on DROP NOT NULL;
ALTER TABLE barcodes.barcode ADD COLUMN create_date_time timestamp DEFAULT NOW();
COMMENT ON COLUMN barcodes.barcode.assigned_on IS 'Date the barcode was assigned to a project';
COMMENT ON COLUMN barcodes.barcode.create_date_time IS 'Date barcode created on the system';