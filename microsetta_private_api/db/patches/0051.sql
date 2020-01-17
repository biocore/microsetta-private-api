-- This script completes the migration of ag.ag_login into accounts

ALTER TABLE ag.ag_kit
DROP CONSTRAINT fk_ag_kit_to_login_id;

ALTER TABLE ag.ag_login_surveys
DROP CONSTRAINT fk_ag_login_surveys;

ALTER TABLE ag.source
DROP CONSTRAINT fk_source;

-- Replaces ag.ag_kit.fk_ag_kit_to_login_id
ALTER TABLE ag.ag_kit
ADD CONSTRAINT fk_ag_kit_to_login_id FOREIGN KEY (ag_login_id)
REFERENCES ag.account (id);

-- Replaces ag.ag_login_surveys.fk_ag_login_surveys
ALTER TABLE ag.ag_login_surveys
ADD CONSTRAINT fk_ag_login_surveys FOREIGN KEY (ag_login_id)
REFERENCES ag.account (id);

-- Replaces ag.source.fk_source
ALTER TABLE ag.source
ADD CONSTRAINT fk_source_account FOREIGN KEY (account_id)
REFERENCES ag.account (id);

-- TODO: !!CRITICAL!! Are we confident to remove the backup table at this time
--  due to existence of other backup mechanisms?
--DROP TABLE ag.ag_login_backup
