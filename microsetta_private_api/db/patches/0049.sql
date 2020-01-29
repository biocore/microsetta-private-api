-- This script is the second half of migrating data and constraints from
-- ag_consent, consent_revoked and ag_login_survey into a new ag.source table

-- Unlink foreign keys after migration, we will not delete the backups yet.
ALTER TABLE ag.consent_revoked_backup
DROP CONSTRAINT fk_consent_revoked;

ALTER TABLE ag.ag_consent_backup
DROP CONSTRAINT fk_american_gut_consent;

-- Remove the replaced environmental data column so we don't get out of sync
ALTER TABLE ag_kit_barcodes
DROP COLUMN environment_sampled;

-- Replace foreign key constraints in the new schema
-- Replaces consent_revoked.fk_consent_revoked AND
-- ag_consent.fk_american_gut_consent
ALTER TABLE ag.source
ADD CONSTRAINT fk_source FOREIGN KEY (account_id)
REFERENCES ag.ag_login (ag_login_id);

-- Replaces ag_login_surveys.fk_ag_login_surveys0
ALTER TABLE ag.ag_login_surveys
ADD CONSTRAINT fk_ag_login_surveys0 FOREIGN KEY (ag_login_id, source_id)
REFERENCES ag.source (account_id, id);

ALTER TABLE ag.ag_login_surveys ALTER COLUMN source_id SET NOT NULL;

-- Remove duplication of participant_name, this is now keyed by source_id
DROP INDEX idx_ag_login_surveys;
DROP INDEX idx_ag_login_surveys_0;

ALTER TABLE ag.ag_login_surveys
DROP COLUMN participant_name;