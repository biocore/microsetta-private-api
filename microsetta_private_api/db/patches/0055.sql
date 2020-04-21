-- Prior to the TMI collection kit, the concept of a kit was specific to the
-- American Gut Project and its schema. The TMI kit though is physically a kit
-- and reasonably will be used on non-TMI projects in the future. Therefore
-- we are ensuring kit names can be reflected for all kits created, even if they
-- are not part of the TMI/AGP. 

-- A note on projects: previously, barcodes were associated with projects not
-- kits. This was necessary as non-AGP projects did not have a notion of a kit.

-- With TMI kits, we are also now positioned to (for many kits) get fedex tracking 
-- information, so lets us up for that...
CREATE TABLE barcodes.kit (
    kit_uuid uuid DEFAULT uuid_generate_v4() NOT NULL,
    kit_id VARCHAR NOT NULL CONSTRAINT unq_kit_id UNIQUE,
    fedex_tracking VARCHAR NULL,
    address VARCHAR NULL,
    CONSTRAINT kit_uuid_pkey PRIMARY KEY ( kit_uuid )
);

-- Now lets make sure the barcodes are associated to the kits
ALTER TABLE barcodes.barcode ADD COLUMN kit_id VARCHAR;
ALTER TABLE barcodes.barcode ADD CONSTRAINT fk_barcode_kit_id
    FOREIGN KEY (kit_id) REFERENCES barcodes.kit (kit_id);

-- Let's make sure all existing kits are reflected in this 
-- table
INSERT INTO barcodes.kit (kit_id) 
    SELECT supplied_kit_id 
    FROM ag.ag_kit;

-- and we need to also set the kit_id reference in the barcodes.barcode
-- table
DO $do$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT supplied_kit_id, barcode
            FROM ag.ag_kit
            JOIN ag.ag_kit_barcodes USING(ag_kit_id)
    LOOP
        UPDATE barcodes.barcode
            SET kit_id = rec.supplied_kit_id
            WHERE barcode=rec.barcode;
    END LOOP;
END $do$;


-- And finally, let's establish FK relationships
ALTER TABLE ag.ag_kit ADD CONSTRAINT fk_barcode_schema_kit_id
    FOREIGN KEY (supplied_kit_id) REFERENCES barcodes.kit (kit_id);
