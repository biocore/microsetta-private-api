-- Add a flag to the campaign.fundrazr_transaction_perk table to reflect whether it has been processed
ALTER TABLE campaign.fundrazr_transaction_perk ADD COLUMN processed BOOLEAN NOT NULL DEFAULT FALSE;

-- Add a flag to the campaign.fundrazr_daklapack_orders table to reflect whether we've sent out a tracking number
ALTER TABLE campaign.fundrazr_daklapack_orders ADD COLUMN tracking_sent BOOLEAN NOT NULL DEFAULT FALSE;

-- The campaign.fundrazr_perk_to_daklapack_article table hasn't been used yet, so it's safe to drop.
DROP TABLE campaign.fundrazr_perk_to_daklapack_article;

-- Since our model has changed to include perks that are FFQ-only and subscriptions,
-- we're going to retool the table to better reflect how perks function.
-- For subscriptions, we'll utilize the fulfillment_spacing_* columns to control scheduling.
-- E.g., fulfillment_spacing_number = 3 and fulfillment_spacing_unit = 'months' will schedule quarterly orders.
-- If we decide to offer perks with multiple kits shipped at once in the future, fulfillment_spacing_number = 0 can be used to reflect this behavior.
CREATE TYPE FULFILLMENT_SPACING_UNIT AS ENUM ('days', 'months');
CREATE TABLE campaign.fundrazr_perk_fulfillment_details (
    perk_id VARCHAR NOT NULL PRIMARY KEY,
    ffq_quantity INTEGER NOT NULL,
    kit_quantity INTEGER NOT NULL,
    dak_article_code VARCHAR, -- Must be nullable, as not all perks include a kit
    fulfillment_spacing_number INTEGER NOT NULL,
    fulfillment_spacing_unit FULFILLMENT_SPACING_UNIT,
    CONSTRAINT fk_perk_to_dak FOREIGN KEY (dak_article_code) REFERENCES barcodes.daklapack_article (dak_article_code)
);

-- The API will pull down perks automatically, but we need it to exist so we can add the fullfilment info,
-- so we're just going to insert them here
INSERT INTO campaign.fundrazr_perk
    (id, remote_campaign_id, title, price)
    VALUES ('3QeVd', '4Tqx5', 'Analyze Your Nutrition', 20),
           ('3QeW6', '4Tqx5', 'Explore Your Microbiome', 180),
           ('0QeXa', '4Tqx5', 'Follow Your Gut', 720);

-- Insert the fulfillment info for the perks we're offering
INSERT INTO campaign.fundrazr_perk_fulfillment_details
    (perk_id, ffq_quantity, kit_quantity, dak_article_code, fulfillment_spacing_number, fulfillment_spacing_unit)
    VALUES ('3QeVd', 1, 0, NULL, 0, NULL),
           ('3QeW6', 1, 1, '3510005E', 0, NULL),
           ('0QeXa', 4, 4, '3510005E', 3, 'months');

-- Both the subscriptions and subscriptions_fulfillment tables will have cancelled flags to create
-- an audit trail in the event someone contacts us to cancel scheduled shipments.
-- We're storing the flag at both levels so we can track what portion of a subscription was actually sent.
-- We say "No refunds" but it would be good to have the granular data on what people received, just in case.
CREATE TABLE campaign.subscriptions (
    subscription_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    account_id UUID, -- Must be nullable in case someone contributes to receive a subscription before creating their account
    transaction_id VARCHAR NOT NULL,
    fundrazr_transaction_perk_id UUID NOT NULL,
    cancelled BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_account_id FOREIGN KEY (account_id) REFERENCES ag.account (id),
    CONSTRAINT fk_transaction_id FOREIGN KEY (transaction_id) REFERENCES campaign.transaction (id),
    CONSTRAINT fk_ftp_id FOREIGN KEY (fundrazr_transaction_perk_id) REFERENCES campaign.fundrazr_transaction_perk (id)
);

-- Participants can alter shipment dates, but only once per shipment.
-- The fulfillment_date_changed column will manage this.
CREATE TYPE FULFILLMENT_TYPE AS ENUM ('ffq', 'kit');
CREATE TABLE campaign.subscriptions_fulfillment (
    fulfillment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subscription_id UUID NOT NULL,
    fulfillment_type FULFILLMENT_TYPE NOT NULL,
    dak_article_code VARCHAR, -- Must be nullable, as not all perks include a kit
    fulfillment_date DATE,
    fulfillment_date_changed BOOLEAN NOT NULL DEFAULT FALSE,
    fulfilled BOOLEAN NOT NULL DEFAULT FALSE,
    cancelled BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_subscription_id FOREIGN KEY (subscription_id) REFERENCES campaign.subscriptions (subscription_id),
    CONSTRAINT fk_dak_article_code FOREIGN KEY (dak_article_code) REFERENCES barcodes.daklapack_article (dak_article_code)
);

-- FFQs will have a registration code (similar to the old activation code) moving forward,
-- although it will not be tied to an email address.
CREATE TABLE campaign.ffq_registration_codes (
    ffq_registration_code VARCHAR PRIMARY KEY,
    registration_code_used TIMESTAMP -- Nullable => null = unused code
)

-- Create a record of the fulfillment of FFQ codes relative to a transaction/perk combination.
CREATE TABLE campaign.fundrazr_ffq_codes (
    fundrazr_transaction_perk_id UUID NOT NULL,
    ffq_registration_code VARCHAR NOT NULL,
    CONSTRAINT fk_ftp_id FOREIGN KEY (fundrazr_transaction_perk_id) REFERENCES campaign.fundrazr_transaction_perk (id),
    CONSTRAINT fk_ffq_code FOREIGN KEY (ffq_registration_code) REFERENCES campaign.ffq_registration_codes (ffq_registration_code)
)