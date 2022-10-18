-- Table: barcodes.daklapack_order_by_perk_type

-- DROP TABLE IF EXISTS barcodes.daklapack_order_by_perk_type;

-- Table: campaign.subscriptions

-- DROP TABLE IF EXISTS campaign.subscriptions;

CREATE TABLE IF NOT EXISTS campaign.subscriptions
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    submitter_acct_id uuid,
    transaction_id character varying COLLATE pg_catalog."default" NOT NULL,
    no_of_kits character varying COLLATE pg_catalog."default" NOT NULL,
    status character varying COLLATE pg_catalog."default",
    creation_timestamp timestamp with time zone,
    CONSTRAINT subscriptions_pkey PRIMARY KEY (id),
    CONSTRAINT fk_acct_id FOREIGN KEY (submitter_acct_id)
        REFERENCES ag.account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS campaign.subscriptions
    OWNER to postgres;

-- Table: campaign.subscription_shipment

-- DROP TABLE IF EXISTS campaign.subscription_shipment;

CREATE TABLE IF NOT EXISTS campaign.subscription_shipment
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    subscription_id character varying COLLATE pg_catalog."default" NOT NULL,
    planned_send_date date,
    creation_timestamp timestamp with time zone,
    status character varying COLLATE pg_catalog."default",
    CONSTRAINT subscription_shipment_pkey PRIMARY KEY (id),
    CONSTRAINT fk_subscription_id FOREIGN KEY (subscription_id)
        REFERENCES campaign.subscriptions (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS campaign.subscription_shipment
    OWNER to postgres;


-- Table: campaign.fundrazr_perk_activation_code

-- DROP TABLE IF EXISTS campaign.fundrazr_perk_activation_code;

CREATE TABLE IF NOT EXISTS campaign.fundrazr_perk_activation_code
(
    code character varying COLLATE pg_catalog."default" NOT NULL,
    perk_id character varying COLLATE pg_catalog."default",
    account_id uuid,
    campaign_id character varying COLLATE pg_catalog."default",
    CONSTRAINT account_id_fk FOREIGN KEY (account_id)
        REFERENCES ag.account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT campaign_id_fk FOREIGN KEY (campaign_id)
        REFERENCES campaign.transaction_source_to_campaign (remote_campaign_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_fundrazr_perk_id FOREIGN KEY (perk_id)
        REFERENCES campaign.fundrazr_perk (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS campaign.fundrazr_perk_activation_code
    OWNER to postgres;
