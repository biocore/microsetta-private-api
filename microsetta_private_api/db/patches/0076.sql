-- add a new "box_id" column to the kit table and populate it
-- (for all records to date) with the kit uuid;
-- require it be not null
ALTER TABLE barcodes.kit ADD COLUMN box_id varchar NULL;
UPDATE barcodes.kit SET box_id = kit_uuid;
ALTER TABLE barcodes.kit ALTER COLUMN box_id SET NOT NULL;