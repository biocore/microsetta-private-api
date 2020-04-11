-- the following procedure migrates all handout kit details into
-- ag_kit and ag_kit_barcodes to satisfy new expectations for how
-- kit identifiers are handled

DO $do$
DECLARE
    r record;
BEGIN
    FOR r IN
        SELECT * FROM ag.ag_handout_kits
    LOOP
        INSERT INTO ag.ag_kit
            (supplied_kit_id, kit_password, swabs_per_kit,
             kit_verification_code, print_results)
            VALUES (r.kit_id, r.password, r.swabs_per_kit,
                    r.verification_code, 'Y');
    END LOOP;
    FOR r IN
        SELECT *
        FROM ag.ag_handout_barcodes ahb
        LEFT JOIN ag.ag_kit ak ON ahb.kit_id = ak.supplied_kit_id
        WHERE barcode NOT IN (
            SELECT barcode
            FROM ag.ag_kit_barcodes
            )
    LOOP
        INSERT INTO ag.ag_kit_barcodes
            (ag_kit_id, barcode, sample_barcode_file)
            VALUES (r.ag_kit_id, r.barcode, r.barcode || '.jpg');

        DELETE FROM ag.ag_handout_kits WHERE kit_id = r.kit_id;
        DELETE FROM ag.ag_handout_barcodes WHERE kit_id = r.kit_id;
    END LOOP;
END $do$;
