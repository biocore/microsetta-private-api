-- The organization that hosts the skin-scoring app provides us with username
-- and password pairings for participants to access the app. We need to store
-- these pairings, as well as a flag for whether the pairing has been
-- allocated to a participant. We explicitly store this flag to avoid reuse
-- if sources (and their related survey databsase records) were to be deleted.
CREATE TABLE ag.skin_scoring_app_credentials (
    app_username VARCHAR PRIMARY KEY,
    app_password VARCHAR NOT NULL,
    credentials_allocated BOOLEAN NOT NULL DEFAULT FALSE
);

-- And we create a registry table, similar to all of the other external
-- surveys we've hosted in the past, to link the username to the account and
-- source that used it.
CREATE TABLE ag.skin_scoring_app_registry (
    app_username VARCHAR PRIMARY KEY,
    account_id UUID NOT NULL,
    source_id UUID,
    deleted BOOLEAN NOT NULL DEFAULT false,
    creation_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_skin_scoring_app_username FOREIGN KEY (app_username) REFERENCES ag.skin_scoring_app_credentials(app_username),
    CONSTRAINT fk_skin_scoring_app_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_skin_scoring_app_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);

CREATE INDEX skin_scoring_app_registry_source ON ag.skin_scoring_app_registry (account_id, source_id);
