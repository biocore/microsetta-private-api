CREATE TABLE ag.pffqsurvey_registry (
    account_id UUID NOT NULL,
    source_id UUID NULL,  -- nullable if deleted, derived from MPA source table
    pffq_survey_id VARCHAR NOT NULL, -- PFFQ but TMI generated (return/sent payload) 
    pffq_survey_url varchar NOT NULL,
    deleted boolean NOT NULL DEFAULT false,
    creation_timestamp timestamptz NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_pffqsurvey_registry_account FOREIGN KEY (account_id) REFERENCES ag.account(id),
    CONSTRAINT fk_pffqsurvey_registry_source FOREIGN KEY (source_id) REFERENCES ag.source(id)
);

CREATE INDEX pffqs_reg_by_pffq_id ON ag.pffqsurvey_registry (pffq_survey_id);
CREATE INDEX pffqs_reg_by_source ON ag.pffqsurvey_registry (account_id, source_id);
