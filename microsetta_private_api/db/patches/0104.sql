CREATE TABLE ag.consent_documents (
    consent_id uuid NOT NULL,
    consent_type varchar(50) NOT NULL,
    locale varchar(10) NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    consent_content varchar NOT NULL,
    account_id uuid NOT NULL,
    PRIMARY KEY (consent_id),
    FOREIGN KEY (account_id) REFERENCES ag.account (id)
);
CREATE TABLE ag.consent_audit (
    signature_id uuid NOT NULL,
    parent_1_name varchar(200) NOT NULL,
    parent_2_name varchar(200) NOT NULL,
    deceased_parent boolean NOT NULL,
    assent_obtainer varchar(200) NOT NULL,
    consent_id uuid NOT NULL,
    source_id uuid NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (signature_id),
    FOREIGN KEY (consent_id) REFERENCES ag.consent_documents (consent_id),
    FOREIGN KEY (source_id) REFERENCES ag.source (id)
);