-- modify campaign.fundrazr_perk_to_daklapack_article
-- to use article UUID as foreign key instead of article code;
-- table is not yet in use so just drop and re-create.
-- (drop should fail if the primary key here is being used as a foreign
-- key anywhere else, so should be safe to do this.)

DROP TABLE campaign.fundrazr_perk_to_daklapack_article;
CREATE TABLE campaign.fundrazr_perk_to_daklapack_article (
    perk_id VARCHAR NOT NULL,
    dak_article_id uuid NOT NULL,
    CONSTRAINT pk_perk_to_dak PRIMARY KEY (perk_id, dak_article_id),
    CONSTRAINT fk_perk_to_dak FOREIGN KEY (dak_article_id) REFERENCES barcodes.daklapack_article (dak_article_id)
);

-- modify the daklapack_article table
-- to take out columns not being used and add a new detailed description and a column indicating
-- which articles are retired.
-- mark those being retired now as retired=true and then change the data type of the article code
-- from integer to string since new codes are strings.
-- update and add records to bring article set up to date, including adding the new detailed descriptions,
-- then set the detailed description column not to allow nulls.

ALTER TABLE barcodes.daklapack_article DROP COLUMN num_2point5ml_etoh_tubes;
ALTER TABLE barcodes.daklapack_article DROP COLUMN num_7ml_etoh_tube;
ALTER TABLE barcodes.daklapack_article DROP COLUMN num_neoteryx_kit;
ALTER TABLE barcodes.daklapack_article DROP COLUMN outer_sleeve;
ALTER TABLE barcodes.daklapack_article DROP COLUMN box;
ALTER TABLE barcodes.daklapack_article DROP COLUMN return_label;
ALTER TABLE barcodes.daklapack_article DROP COLUMN compartment_bag;
ALTER TABLE barcodes.daklapack_article DROP COLUMN num_stool_collector;
ALTER TABLE barcodes.daklapack_article DROP COLUMN instructions;
ALTER TABLE barcodes.daklapack_article DROP COLUMN registration_card;
ALTER TABLE barcodes.daklapack_article DROP COLUMN swabs;
ALTER TABLE barcodes.daklapack_article DROP COLUMN rigid_safety_bag;
ALTER TABLE barcodes.daklapack_article ADD COLUMN detailed_description VARCHAR;
ALTER TABLE barcodes.daklapack_article ADD COLUMN retired boolean DEFAULT FALSE;

UPDATE barcodes.daklapack_article SET retired=TRUE, detailed_description=short_description;

ALTER TABLE barcodes.daklapack_article ALTER COLUMN dak_article_code TYPE VARCHAR;

UPDATE barcodes.daklapack_article SET dak_article_code='3510000E', short_description='TMI 1 tube', detailed_description='TMI 1 tube, American English', retired=FALSE WHERE dak_article_code='350100';

INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510001E', 'TMI 1 tube', 'TMI 1 tube, American English, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3511000E', 'TMI 1 tube + blood', 'TMI 1 tube + blood, American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3541002E', 'TMI 6 tubes + blood', 'TMI 6 tubes + blood , American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3512004E', 'TMI 1 tube + urine', 'TMI 1 tube + urine, American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3532004E', 'TMI 2 tubes + urine', 'TMI 2 tubes + urine, American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510001M', 'TMI 1 tube', 'TMI 1 tube, Mexican Spanish, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510001S', 'TMI 1 tube', 'TMI 1 tube, Spanish, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510001J', 'TMI 1 tube', 'TMI 1 tube, Japanese, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3520003E', 'TMI scoop tube', 'TMI 1 scoop tube (6ml EtOH), American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3521003E', 'TMI scoop tube + blood', 'TMI 1 scoop tube (6 ml EtOH) + blood, American English');

ALTER TABLE barcodes.daklapack_article ALTER COLUMN detailed_description SET NOT NULL;
