CREATE SCHEMA campaign;
ALTER TABLE barcodes.interested_users SET SCHEMA campaign;
ALTER TABLE barcodes.campaigns SET SCHEMA campaign;
ALTER TABLE barcodes.campaigns_projects SET SCHEMA campaign;
ALTER TABLE ag.melissa_address_queries SET SCHEMA campaign;

CREATE TABLE campaign.transaction_source_to_campaign (
    remote_campaign_id VARCHAR PRIMARY KEY,
    internal_campaign_id uuid NOT NULL,
    currency VARCHAR NOT NULL,
    UNIQUE (remote_campaign_id, internal_campaign_id),
    CONSTRAINT fk_campaign FOREIGN KEY (internal_campaign_id) REFERENCES campaign.campaigns (campaign_id)
);

INSERT INTO campaign.campaigns 
    (title) 
    VALUES ('The Microsetta Initiative'),
           ('American Gut Project'),
           ('British Gut Project');
INSERT INTO campaign.transaction_source_to_campaign
    SELECT '31l0S2' AS remote_campaign_id, campaign_id AS internal_campaign_id, 'usd' AS currency
    FROM campaign.campaigns
    WHERE title='The Microsetta Initiative';
INSERT INTO campaign.transaction_source_to_campaign
    SELECT '4Tqx5' AS remote_campaign_id, campaign_id AS internal_campaign_id, 'usd' AS currency
    FROM campaign.campaigns
    WHERE title='American Gut Project';
INSERT INTO campaign.transaction_source_to_campaign
    SELECT '4sSf3' AS remote_campaign_id, campaign_id AS internal_campaign_id, 'gbp' AS currency
    FROM campaign.campaigns
    WHERE title='British Gut Project';

CREATE TYPE TRN_TYPE AS ENUM ('fundrazr');

-- interested_user_id is nullable in the case of 
-- offline contributions. these transactions do not
-- have payer or contact emails per fundrazr's
-- dev team.
CREATE TABLE campaign.transaction (
    id VARCHAR PRIMARY KEY, 
    interested_user_id UUID,
    transaction_type TRN_TYPE NOT NULL,
    remote_campaign_id VARCHAR NOT NULL,
    created TIMESTAMP NOT NULL,
    amount FLOAT NOT NULL,
    net_amount FLOAT NOT NULL,
    currency VARCHAR NOT NULL,
    payer_first_name VARCHAR NOT NULL,
    payer_last_name VARCHAR NOT NULL,
    payer_email VARCHAR,
    account_type VARCHAR NOT NULL,
    message VARCHAR,
    subscribed_to_updates BOOLEAN NOT NULL,
    CONSTRAINT fk_transaction_campaign FOREIGN KEY (remote_campaign_id) REFERENCES campaign.transaction_source_to_campaign (remote_campaign_id),
    CONSTRAINT fk_transaction_user FOREIGN KEY (interested_user_id) REFERENCES campaign.interested_users (interested_user_id)
);

CREATE TABLE campaign.fundrazr_perk (
    id VARCHAR PRIMARY KEY,
    remote_campaign_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    CONSTRAINT fk_transaction_campaign FOREIGN KEY (remote_campaign_id) REFERENCES campaign.transaction_source_to_campaign (remote_campaign_id)
);

CREATE TABLE campaign.fundrazr_transaction_perk (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id VARCHAR NOT NULL,
    perk_id VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    CONSTRAINT fk_transaction_claimed_perk FOREIGN KEY (transaction_id) REFERENCES campaign.transaction (id),
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
