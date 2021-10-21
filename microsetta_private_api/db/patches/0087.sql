CREATE TABLE barcodes.daklapack_order_to_kit
(
    dak_order_id uuid NOT NULL,
    kit_uuid uuid NOT NULL,
    CONSTRAINT dak_order_to_kit_uuid_pkey PRIMARY KEY ( dak_order_id, kit_uuid ),
    CONSTRAINT fk_dak_order_id FOREIGN KEY ( dak_order_id ) REFERENCES barcodes.daklapack_order( dak_order_id ),
    CONSTRAINT fk_kit_uuid FOREIGN KEY ( kit_uuid ) REFERENCES barcodes.kit( kit_uuid )
);
