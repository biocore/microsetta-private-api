-- add and fill daklapack_article table

-- create table barcodes.daklapack_article
CREATE TABLE barcodes.daklapack_article
(
    dak_article_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    dak_article_code INTEGER NOT NULL,
    short_description VARCHAR NOT NULL,
    num_2point5ml_etoh_tubes INTEGER NOT NULL,
    num_7ml_etoh_tube INTEGER NOT NULL,
    num_neoteryx_kit INTEGER NOT NULL,
    outer_sleeve VARCHAR NOT NULL,
    box VARCHAR NOT NULL,
    return_label VARCHAR NOT NULL,
    compartment_bag VARCHAR NOT NULL,
    num_stool_collector INTEGER NOT NULL,
    instructions VARCHAR,
    registration_card VARCHAR,
    swabs VARCHAR,
    rigid_safety_bag VARCHAR,
    CONSTRAINT dak_article_pkey PRIMARY KEY (dak_article_id),
    CONSTRAINT idx_dak_article_code UNIQUE (dak_article_code)
);

INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350100,'TMI 1 tube', '1', '0', '0', 'Microsetta', 'Microsetta', 'Microsetta', 'Microsetta', '0', 'Fv1', 'Microsetta', '1x bag of two', 'yes');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350103,'TMI 2 tubes', '2', '0', '0', 'Microsetta', 'Microsetta', 'Microsetta', 'Microsetta', '0', '3v1', 'Microsetta', '2x bag of two', 'yes');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350104,'TMI 2 tubes + Blood', '2', '0', '1', 'Microsetta', 'Microsetta', 'Microsetta', 'Microsetta', '0', '3v1 + Bv1', 'Microsetta', '2x bag of two', 'yes');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350109,'TMI 4 tubes', '4', '0', '0', 'Microsetta', 'Microsetta', 'Microsetta', '4 tubes', '0', '4v1', 'Microsetta', '4x bag of two', 'no');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350110,'TMI 4 tubes + Blood', '4', '0', '1', 'Microsetta', 'Microsetta', 'Microsetta', '4 tubes', '0', '4v1 + Bv1', 'Microsetta', '4x bag of two', 'no');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350200,'AGMP Tube', '0', '1', '0', 'Microsetta', 'Microsetta', 'Microsetta', 'Microsetta', '1', 'TBD', '', '', 'no');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350201,'AGMP Tube + blood', '0', '1', '1', 'Microsetta', 'Microsetta', 'Microsetta', 'Microsetta', '1', 'TBD', '', '', 'no');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350205,'2 AGMP Tube', '0', '2', '0', 'Microsetta', 'Microsetta', 'Microsetta', '4 tubes', '1', 'TBD', '', '', 'no');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, num_2point5ml_etoh_tubes, num_7ml_etoh_tube, num_neoteryx_kit, outer_sleeve, box, return_label, compartment_bag, num_stool_collector, instructions, registration_card, swabs, rigid_safety_bag) VALUES (350210,'TMI  7 tubes', '7', '0', '0', 'Microsetta', 'Microsetta', 'Microsetta', '4 tubes', '0', 'FV1', 'Microsetta', '7x bag of two', 'no');