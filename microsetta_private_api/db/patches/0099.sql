CREATE TABLE ag.polyphenol_ffq_registry (
    polyphenol_ffq_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    account_id UUID NOT NULL,
    source_id UUID,
    language_tag VARCHAR,
    study VARCHAR,
    deleted BOOLEAN NOT NULL DEFAULT false,
    creation_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_polyphenol_ffq_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_polyphenol_ffq_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);

CREATE INDEX polyphenol_ffq_registry_source ON ag.polyphenol_ffq_registry (account_id, source_id);
