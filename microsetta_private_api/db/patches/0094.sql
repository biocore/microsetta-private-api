CREATE TABLE ag.myfoodrepo_registry (
    account_id UUID NOT NULL,
    source_id UUID NOT NULL,
    myfoodrepo_id VARCHAR NULL,
    deleted boolean NOT NULL DEFAULT false,
    creation_timestamp timestamptz NOT NULL DEFAULT NOW(),
    CONSTRAINT pk_myfoodrepo_registry_pk PRIMARY KEY (account_id, source_id),
    CONSTRAINT fk_myfoodrepo_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_myfoodrepo_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);
