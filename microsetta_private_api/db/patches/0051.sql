-- This script completes the migration of ag.ag_login into accounts

ALTER TABLE ag.ag_kit
DROP CONSTRAINT fk_ag_kit_to_login_id;

ALTER TABLE ag.ag_login_surveys
DROP CONSTRAINT fk_ag_login_surveys;

ALTER TABLE ag.source
DROP CONSTRAINT fk_source;

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

-- In the past, each kit could be constructed with an ag_login_id,
-- now, while we have to leave this column around for enabling login
-- by kit_id, we can't really assign kits to accounts, as individual
-- samples are assigned to accounts instead.  Thus we have to remove the
-- NOT NULL constraint on this field.
ALTER TABLE ag.ag_kit
ALTER COLUMN ag_login_id DROP NOT NULL;
