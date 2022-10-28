CREATE TABLE IF NOT EXISTS campaign.subscriptions
(
   id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
   submitter_acct_id UUID NOT NULL,
   transaction_id VARCHAR NOT NULL,
   no_of_kits VARCHAR NOT NULL,
   status VARCHAR,
   email VARCHAR NOT NULL,
   creation_timestamp timestamp with time zone,
   CONSTRAINT fk_acct_id FOREIGN KEY (submitter_acct_id) REFERENCES ag.account (id)
);

CREATE TABLE IF NOT EXISTS campaign.subscription_shipment
(
   id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
   subscription_id UUID NOT NULL,
   planned_send_date date,
   creation_timestamp timestamp with time zone,
   status VARCHAR,
   CONSTRAINT fk_subscription_id FOREIGN KEY (subscription_id) REFERENCES campaign.subscriptions (id)
);

CREATE TABLE IF NOT EXISTS campaign.fundrazr_perk_activation_code
(
   id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
   code VARCHAR NOT NULL,
   perk_id VARCHAR NOT NULL,
   account_id uuid NOT NULL,
   campaign_id uuid NOT NULL,
   CONSTRAINT account_id_fk FOREIGN KEY (account_id) REFERENCES ag.account (id),
   CONSTRAINT campaign_id_fk FOREIGN KEY (campaign_id) REFERENCES campaign.campaigns (campaign_id),
   CONSTRAINT fk_fundrazr_perk_id FOREIGN KEY (perk_id) REFERENCES campaign.fundrazr_perk (id)
);
