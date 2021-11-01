-- we have a sync issue, where if these data change we cannot assure fundrazr
-- reflects those changes. Right now, this is a pragmatic table to link perks
-- to articles. if we move to centralizing fundrazr content, then this table
-- should be altered to reflect the full perk information, and mechanisms
-- need to be established to enforce fundrazr is consistent. specifically,
-- it would be imperative to revise the fundrazr and fundrazr_perk 
-- representation to track all of their fields, a policy determined for
-- whether fundrazr or us represents the ground truth, and mechanisms
-- to absorb or push change as needed to be added.
CREATE TABLE barcodes.fundrazr (
    remote_campaign_id VARCHAR PRIMARY KEY,
    internal_campaign_id uuid NOT NULL,
    currency VARCHAR NOT NULL,
    UNIQUE (remote_campaign_id, internal_campaign_id),
    CONSTRAINT FOREIGN KEY fk_campaign (internal_campaign_id) REFERENCES barcodes.campaigns (campaign_id)
);

CREATE TYPE tmi_transaction_status AS ENUM ('received', 'valid-address', 'invalid-address', 'shipment-requested');

CREATE TABLE barcodes.fundrazr_transaction (
    id VARCHAR PRIMARY KEY, 
    remote_campaign_id VARCHAR,
    created TIMESTAMP NOT NULL,
    amount FLOAT NOT NULL,
    net_amount FLOAT NOT NULL,
    currency VARCHAR NOT NULL,
    fundrazr_status VARCHAR NOT NULL,
    payer_name VARCHAR NOT NULL,
    payer_first_name VARCHAR NOT NULL,
    payer_last_name VARCHAR NOT NULL,
    payer_email VARCHAR NOT NULL,
    account_type VARCHAR NOT NULL,
    contact_email VARCHAR NOT NULL,
    shipping_first_name VARCHAR NULL,
    shipping_last_name VARCHAR NULL,
    shipping_company VARCHAR NULL,
    shipping_address1 VARCHAR NULL,
    shipping_address2 VARCHAR NULL,
    shipping_city VARCHAR NULL,
    shipping_country VARCHAR NULL,
    shipping_state VARCHAR NULL,
    shipping_postal VARCHAR NULL,
    subscribed_to_updates BOOLEAN NOT NULL,
    tmi_status tmi_transaction_status NOT NULL DEFAULT 'received',
    CONSTRAINT FOREIGN KEY fk_transaction_campaign (remote_campaign_id) REFERENCES barcodes.fundrazr (remote_campaign_id)
);

CREATE TABLE barcodes.fundrazr_perk (
    id VARCHAR PRIMARY KEY,
    remote_campaign_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    CONSTRAINT FOREIGN KEY fk_transaction_campaign (remote_campaign_id) REFERENCES barcodes.fundrazr (remote_campaign_id)
);

CREATE TABLE barcodes.fundrazr_transaction_perk (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id VARCHAR NOT NULL,
    perk_id VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    CONSTRAINT FOREIGN KEY fk_transaction_claimed_perk (transaction_id) REFERENCES barcodes.fundrazr_transaction (id),
    CONSTRAINT FOREIGN KEY fk_transaction_what_perk (perk_id) REFERENCES bardodes.fundrazr_perk (id),
    UNIQUE (transaction_id, perk_id)
);

-- a single claimed perk with N quantity will have N separate
-- daklapack orders
CREATE TABLE barcodes.fundrazr_daklapack_orders (
    fundrazr_transaction_perk_id UUID NOT NULL,
    dak_order_id UUID NOT NULL,
    CONSTRAINT FOREIGN KEY fk_fundrazr_dak_order_perk (fundrazr_transaction_perk_id) REFERENCES barcodes.fundrazr_transaction_perk (id),
    CONSTRAINT FOREIGN KEY fk_fundrazr_dak_order_order (dak_order_id) REFERENCES barcodes.daklapack_order (dak_order_id),
    UNIQUE (fundrazr_transaction_perk_id, dak_order_id)
);

CREATE TABLE barcodes.fundrazr_perk_to_daklapack_article (
    perk_id VARCHAR NOT NULL,
    dak_article_code VARCHAR NOT NULL,
    CONSTRAINT PRIMARY KEY (perk_id, dak_article_code),
    CONSTRAINT FOREIGN KEY (fk_perk_to_dak) REFERENCES barcodes.daklapack_article (dak_article_code)
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
INSERT INTO TABLE barcodes.fundrazr_perk
    (id, remote_campaign_id, title, price)
    VALUES (('0I5n8', '31l0S2', 'Find Out Who’s In Your Gut', 99),
            ('7I5c0', '31l0S2', 'You Plus The World', 130),
            ('6I5fd', '31l0S2', 'See What You’re Sharing', 195));

INSERT INTO TABLE barcodes.fundrazr_perk_to_daklapack_article
    (perk_id, dak_article_code)
    VALUES (('0I5n8', 350100),  
             '7I5c0', 350100), -- you plus the world is single tube + extra to help others
             '6I5fd', 350103));
