-- Table: barcodes.daklapack_order_by_perk_type

-- DROP TABLE IF EXISTS barcodes.daklapack_order_by_perk_type;

CREATE TABLE IF NOT EXISTS barcodes.daklapack_order_by_perk_type
(
   id character varying COLLATE pg_catalog."default" NOT NULL,
   dak_order_id uuid,
   submitter_acct_id uuid NOT NULL,
   planned_send_date date,
   no_of_kits_send character varying COLLATE pg_catalog."default" NOT NULL,
   creation_timestamp timestamp with time zone,
   status character varying COLLATE pg_catalog."default",
   CONSTRAINT order_by_perk_type_pkey PRIMARY KEY (id),
   CONSTRAINT fk_acct_id FOREIGN KEY (submitter_acct_id)
       REFERENCES ag.account (id) MATCH SIMPLE
       ON UPDATE NO ACTION
       ON DELETE NO ACTION,
   CONSTRAINT fk_dak_order_id FOREIGN KEY (dak_order_id)
       REFERENCES barcodes.daklapack_order (dak_order_id) MATCH SIMPLE
       ON UPDATE NO ACTION
       ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS barcodes.daklapack_order_by_perk_type
   OWNER to postgres;

-- Table: campaign.fundrazr_perk_activation_code

-- DROP TABLE IF EXISTS campaign.fundrazr_perk_activation_code;

CREATE TABLE IF NOT EXISTS campaign.fundrazr_perk_activation_code
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    code character varying COLLATE pg_catalog."default" NOT NULL,
    interested_user_id uuid,
    perk_id character varying COLLATE pg_catalog."default",
    CONSTRAINT fundrazr_perk_activation_code_pkey PRIMARY KEY (id),
    CONSTRAINT fk_fundrazr_perk_code FOREIGN KEY (interested_user_id)
        REFERENCES campaign.interested_users (interested_user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_fundrazr_perk_id FOREIGN KEY (perk_id)
        REFERENCES campaign.fundrazr_perk (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS campaign.fundrazr_perk_activation_code
    OWNER to postgres;
ALTER TABLE campaign.fundrazr_perk ADD COLUMN perk_type VARCHAR;
ALTER TABLE campaign.transaction ADD status VARCHAR;

--new patch to remove the not a null constraint in the account table for column created_with_kit_id
ALTER TABLE ag.account ALTER COLUMN created_with_kit_id DROP NOT NULL;
