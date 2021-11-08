CREATE SCHEMA campaign;
ALTER TABLE barcodes.interested_users SET SCHEMA campaign;
ALTER TABLE barcodes.campaigns SET SCHEMA campaign;
ALTER TABLE barcodes.campaigns_projects SET SCHEMA campaign;

-- we have a sync issue, where if these data change we cannot assure fundrazr
-- reflects those changes. Right now, this is a pragmatic table to link perks
-- to articles. if we move to centralizing fundrazr content, then this table
-- should be altered to reflect the full perk information, and mechanisms
-- need to be established to enforce fundrazr is consistent. specifically,
-- it would be imperative to revise the fundrazr and fundrazr_perk 
-- representation to track all of their fields, a policy determined for
-- whether fundrazr or us represents the ground truth, and mechanisms
-- to absorb or push change as needed to be added.
CREATE TABLE campaign.fundrazr (
    remote_campaign_id VARCHAR PRIMARY KEY,
    internal_campaign_id uuid NOT NULL,
    currency VARCHAR NOT NULL,
    UNIQUE (remote_campaign_id, internal_campaign_id),
    CONSTRAINT fk_campaign FOREIGN KEY (internal_campaign_id) REFERENCES campaign.campaigns (campaign_id)
);

INSERT INTO campaign.campaigns 
    (title) 
    VALUES ('The Microsetta Initiative');
INSERT INTO campaign.fundrazr 
    SELECT '31l0S2' AS remote_campaign_id, campaign_id AS internal_campaign_id, 'usd' AS currency
    FROM campaign.campaigns
    WHERE title='The Microsetta Initiative';

CREATE TABLE campaign.fundrazr_transaction (
    id VARCHAR PRIMARY KEY, 
    created TIMESTAMP NOT NULL,
    amount FLOAT NOT NULL,
    net_amount FLOAT NOT NULL,
    currency VARCHAR NOT NULL,
    payer_first_name VARCHAR NOT NULL,
    payer_last_name VARCHAR NOT NULL,
    payer_email VARCHAR NOT NULL,
    account_type VARCHAR NOT NULL,
    message VARCHAR,
    subscribed_to_updates BOOLEAN NOT NULL,
    CONSTRAINT fk_transaction_campaign FOREIGN KEY (remote_campaign_id) REFERENCES campaign.fundrazr (remote_campaign_id),
    CONSTRAINT fk_transaction_user FOREIGN KEY (interested_user_id) REFERENCES campaign.interested_users (interested_user_id)
);

CREATE TABLE campaign.transaction (
    interested_user_id UUID PRIMARY KEY,
    fundrazr_transaction_id VARCHAR NULL,
    -- this constraint is placed on the assumption that future
    -- transaction types will be introduced. the model is for 
    -- a single field per transaction type, and the check ensures
    -- that a single, and only a single, field is not null.
    -- this check will need to be ALTER'd if additional transaction
    -- types are added
    CONSTRAINT chk_ensure_transaction CHECK (fundrazr_transaction_id IS NOT NULL),
    CONSTRAINT fk_fundrazr_transaction FOREIGN KEY (fundrazr_transaction_id) REFERENCES campaign.fundrazr_transaction (id),
);

CREATE TABLE campaign.fundrazr_perk (
    id VARCHAR PRIMARY KEY,
    remote_campaign_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    CONSTRAINT fk_transaction_campaign FOREIGN KEY (remote_campaign_id) REFERENCES campaign.fundrazr (remote_campaign_id)
);

CREATE TABLE campaign.fundrazr_transaction_perk (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id VARCHAR NOT NULL,
    perk_id VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    CONSTRAINT fk_transaction_claimed_perk FOREIGN KEY (transaction_id) REFERENCES campaign.fundrazr_transaction (id),
    CONSTRAINT fk_transaction_what_perk FOREIGN KEY (perk_id) REFERENCES campaign.fundrazr_perk (id),
    UNIQUE (transaction_id, perk_id)
);

-- a single claimed perk with N quantity will have N separate
-- daklapack orders
CREATE TABLE campaign.fundrazr_daklapack_orders (
    fundrazr_transaction_perk_id UUID NOT NULL,
    dak_order_id UUID NOT NULL,
    CONSTRAINT fk_fundrazr_dak_order_perk FOREIGN KEY (fundrazr_transaction_perk_id) REFERENCES campaign.fundrazr_transaction_perk (id),
    CONSTRAINT fk_fundrazr_dak_order_order FOREIGN KEY (dak_order_id) REFERENCES barcodes.daklapack_order (dak_order_id),
    UNIQUE (fundrazr_transaction_perk_id, dak_order_id)
);

CREATE TABLE campaign.fundrazr_perk_to_daklapack_article (
    perk_id VARCHAR NOT NULL,
    dak_article_code INTEGER NOT NULL,
    CONSTRAINT pk_perk_to_dak PRIMARY KEY (perk_id, dak_article_code),
    CONSTRAINT fk_perk_to_dak FOREIGN KEY (dak_article_code) REFERENCES barcodes.daklapack_article (dak_article_code)
);

-- This is not a complete list, but what is available right now. A 
-- minimal set are added, relative to the Microsetta campaign
-- (31l0S2) so we can exercise links against daklapack

-- >>> res = requests.get('https://api.fundrazr.com/v1/campaigns?organization=873K6', headers=d)
-- >>> res
-- <Response [200]>
-- >>> x = res.json()
-- >>> [e['title'] for e in x['entries']]
-- ['The Microsetta Initiative - Mexico', 'The Microsetta Initiative', 'Australian Gut', 'Global FoodOmics Project', 'British Gut', 'American Gut']
-- >>> for e in x['entries']:
-- ...   campaign_id = e['id']
-- ...   for item in e.get('items', []):
-- ...     perk_id = item['id']
-- ...     price = item['price']
-- ...     title = item['title']
-- ...     print(f"('{perk_id}', '{campaign_id}', '{title}', {price}),")
-- ... 
-- ('0Kzr2', 'b1q1v4', 'ASD-Cohort Parent', 75),
-- ('cKzqc', 'b1q1v4', 'Find Out Who’s In Your Gut', 99),
-- ('5Kzm3', 'b1q1v4', 'You Plus The World', 130),
-- ('5Kzna', 'b1q1v4', 'See What You’re Sharing', 195),
-- ('2Kzoa', 'b1q1v4', 'Microbes For Three', 290),
-- ('0I5n8', '31l0S2', 'Find Out Who’s In Your Gut', 99),
-- ('7I5c0', '31l0S2', 'You Plus The World', 130),
-- ('6I5fd', '31l0S2', 'See What You’re Sharing', 195),
-- ('eI5ie', '31l0S2', 'Microbes For Three', 290),
-- ('aG1g6', '11OxG1', 'Find Out Who’s In Your Gut - Microbes for One', 99),
-- ('0G1h3', '11OxG1', 'Microbes For Two: See What You’re Sharing', 180),
-- ('3G1ic', '11OxG1', 'Microbes For Three', 260),
-- ('7G1j6', '11OxG1', 'Microbes For Four', 320),
INSERT INTO campaign.fundrazr_perk
    (id, remote_campaign_id, title, price)
    VALUES ('0I5n8', '31l0S2', 'Find Out Who’s In Your Gut', 99.0),
           ('7I5c0', '31l0S2', 'You Plus The World', 130.0),
           ('6I5fd', '31l0S2', 'See What You’re Sharing', 195.0);

INSERT INTO campaign.fundrazr_perk_to_daklapack_article
    (perk_id, dak_article_code)
    VALUES ('0I5n8', 350100),  
           ('7I5c0', 350100), -- you plus the world is single tube + extra to help others
           ('6I5fd', 350103);
