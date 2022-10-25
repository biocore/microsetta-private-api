CREATE TABLE ag.consent_documents (
    consent_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    consent_type varchar(50) NOT NULL,
    locale varchar(10) NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    consent_content varchar NOT NULL,
    reconsent_required INT NOT NULL,
    account_id uuid NOT NULL,
    PRIMARY KEY (consent_id),
    FOREIGN KEY (account_id) REFERENCES ag.account (id)
);
CREATE TABLE ag.consent_audit (
    signature_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    parent_1_name varchar(200),
    parent_2_name varchar(200),
    deceased_parent boolean,
    assent_obtainer varchar(200),
    consent_id uuid NOT NULL,
    source_id uuid NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (signature_id),
    FOREIGN KEY (consent_id) REFERENCES ag.consent_documents (consent_id)
);

INSERT INTO ag.account VALUES ('ecabc635-3df8-49ee-ae19-db3db03c4500', 'demo@demo.com', 'admin', '', '', 'demo', 'demo', 'demo', 'demo', 'IN', '46227', 'US', 65.01431, -12.88033, 0, NOW(), NOW(), 'bg_sutbg', 'en_US', 'false', 'false');
INSERT INTO ag.consent_documents VALUES ('b8245ca9-e5ba-4f8f-a84a-887c0d6a2233', 'Adult Consent - Data', 'en_US',NOW(), 'This is a sample data consent for adults!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('6b1595a5-4003-4d0f-aa91-56947eaf2901', 'Adult Consent - Biospecimen', 'en_US', NOW(), 'This is a sample biospecimen consent for adults!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('d3e9fa0c-c2a6-4d5c-a926-2eaebbfb055e', 'Parental Consent - Data', 'en_US', NOW(), 'This is a sample data consent for parents!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('a477bc4f-b46e-43a8-86b6-b614c5d8cf3c', 'Parental Consent - Biospecimen', 'en_US', NOW(), 'This is a sample biospecimen consent for parents!', 1, 'ecabcf635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('3b80fd6f-ac65-4530-8cc6-bb37cd2acfe3', 'Teenage Assent - Data', 'en_US', NOW(), 'This is a sample data consent for teenagers!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('4433b220-827a-4172-b285-407db40a9bae', 'Teenage Assent - Biospecimen', 'en_US', NOW(), 'This is a sample biospecimen consent for teenagers!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('0ab8f90d-2792-4e1f-b38d-827fa2ff45f7', 'Child Assent - Data', 'en_US', NOW(), 'This is a sample data consent for children!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');
INSERT INTO ag.consent_documents VALUES ('4b7c8232-73e5-4a0c-b0df-c141431b46d7', 'Child Assent - Biospecimen', 'en_US', NOW(), 'This is a sample biospecimen consent for children!', 1, 'ecabc635-3df8-49ee-ae19-db3db03c4500');