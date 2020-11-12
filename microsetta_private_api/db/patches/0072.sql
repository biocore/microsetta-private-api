-- create tables to record daklapack orders

CREATE TABLE barcodes.daklapack_order
(
    dak_order_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    submitter_acct_id uuid NOT NULL,
    description varchar,
    fulfillment_hold_msg varchar,
    order_json varchar NOT NULL,
    creation_timestamp timestamptz,
    last_polling_timestamp timestamptz,
    last_polling_status varchar,
    CONSTRAINT dak_order_pkey PRIMARY KEY (dak_order_id),
    CONSTRAINT fk_acct_id FOREIGN KEY ( submitter_acct_id ) REFERENCES ag.account( id )
);

CREATE TABLE barcodes.daklapack_order_to_project
(
    dak_order_to_project_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    dak_order_id uuid NOT NULL,
    project_id bigint NOT NULL,
    CONSTRAINT dak_order_to_project_pkey PRIMARY KEY (dak_order_to_project_id),
    CONSTRAINT fk_dak_order_id FOREIGN KEY ( dak_order_id ) REFERENCES barcodes.daklapack_order( dak_order_id ),
    CONSTRAINT fk_project_id FOREIGN KEY ( project_id ) REFERENCES barcodes.project( project_id )
);
