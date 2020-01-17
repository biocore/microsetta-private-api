-- This script is the second half of migrating data and constraints from
-- ag_consent, consent_revoked and ag_login_survey into a new ag.source table

-- Clean up foreign keys and leftover tables after the migration

-- TODO: !!CRITICAL!! - Do we have automated backups in place, or are these
-- tables our -only- record of data before the migration?  If this is it,
-- we should drop foreign keys and indexes, but not delete the data until
-- we're absolutely confident the migration is 100% successful.

-- These alter tables can be removed if we are confident to drop the backups
ALTER TABLE ag.consent_revoked_backup
DROP CONSTRAINT fk_consent_revoked;

ALTER TABLE ag.ag_consent_backup
DROP CONSTRAINT fk_american_gut_consent;

--DROP TABLE ag.consent_revoked_backup;
--DROP TABLE ag.ag_consent_backup;

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

-- Remove duplication of participant_name, this is now keyed by source_id
DROP INDEX idx_ag_login_surveys;
DROP INDEX idx_ag_login_surveys_0;

ALTER TABLE ag.ag_login_surveys
DROP COLUMN participant_name;