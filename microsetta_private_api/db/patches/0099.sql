CREATE TABLE ag.pffqsurvey_registry (
    account_id UUID NOT NULL,
    source_id UUID NULL,  -- nullable if deleted, derived from MPA source table
    pffq_survey_id UUID NOT NULL,
    pffq_survey_url varchar,
    deleted boolean NOT NULL DEFAULT false,
    creation_timestamp timestamptz NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_pffqsurvey_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_pffqsurvey_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id) ON DELETE CASCADE
);

CREATE INDEX pffqs_reg_by_pffq_id ON ag.pffqsurvey_registry (pffq_survey_id);
CREATE INDEX pffqs_reg_by_source ON ag.pffqsurvey_registry (account_id, source_id);
