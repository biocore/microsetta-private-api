CREATE TABLE ag.myfoodrepo_registry (
    account_id UUID NOT NULL,
    source_id UUID NULL,  -- nullable if deleted
    myfoodrepo_id VARCHAR NULL,
    deleted boolean NOT NULL DEFAULT false,
    creation_timestamp timestamptz NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_myfoodrepo_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_myfoodrepo_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);

CREATE INDEX mfr_reg_by_mfr_id ON ag.myfoodrepo_registry (myfoodrepo_id);
CREATE INDEX mfr_reg_by_source ON ag.myfoodrepo_registry (account_id, source_id);
