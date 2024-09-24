CREATE TABLE ag.skin_scoring_app_registry (
    skin_scoring_app_id VARCHAR PRIMARY KEY,
    account_id UUID NOT NULL,
    source_id UUID,
    language_tag VARCHAR,
    deleted BOOLEAN NOT NULL DEFAULT false,
    creation_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_skin_scoring_app_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_skin_scoring_app_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);

CREATE INDEX skin_scoring_app_registry_source ON ag.skin_scoring_app_registry (account_id, source_id);