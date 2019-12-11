-- August 14, 2015
-- Assign unknown project barcodes to the project UNKNOWN so we can continue using database properly
DO $do$
DECLARE
	pid bigint;
BEGIN
	pid := (SELECT project_id + 1 FROM barcodes.project ORDER BY project_id DESC LIMIT 1);
	INSERT INTO barcodes.project (project_id, project) VALUES (pid, 'UNKNOWN');

	INSERT INTO barcodes.project_barcode (project_id, barcode)
		SELECT pid, barcode FROM barcodes.barcode
		LEFT JOIN barcodes.project_barcode USING (barcode)
		WHERE project_id IS NULL AND barcode::integer < 33796;
END $do$;