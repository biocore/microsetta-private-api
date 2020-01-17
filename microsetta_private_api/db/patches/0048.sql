-- This script is the first half of migrating data and constraints from
-- * ag_consent,
-- * consent_revoked and,
-- * ag_login_survey
-- into a new ag.source table that represents sources/participants with their
-- own unique ids

-- Build update triggers for setting timestamps
CREATE OR REPLACE FUNCTION update_trigger()
RETURNS TRIGGER AS $$
BEGIN
    NEW.update_time = current_timestamp;
    RETURN NEW;
END
$$ language 'plpgsql';

-- source represents sources/participants.  We are migrating information
-- from ag_login_surveys, ag_consent, consent_revoked into this table to
-- make sources their own separate objects with types and ids rather than
-- being accessed by a combination of ag_login_id and participant_name
CREATE TABLE ag.source (
    id uuid PRIMARY KEY NOT NULL,
    account_id uuid NOT NULL,
    source_type varchar NOT NULL,
    participant_name varchar(200) NOT NULL,
    participant_email varchar,
    is_juvenile bool,
    parent_1_name varchar(200),
    parent_2_name varchar(200),
--    parent_1_code varchar(200), -- TODO: Can we drop these two columns?
--    parent_2_code varchar(200),
    deceased_parent varchar(10),
    date_signed date,
    date_revoked date,
    assent_obtainer varchar,
    age_range varchar,
    description varchar,
    creation_time timestamp default current_timestamp,
    update_time timestamp default current_timestamp
);

-- We add space for the new source id, we will need to fill it in during the
-- migration.
-- TODO: Add foreign key ref from source_id to source table
-- TODO: Add not null constraint to source_id
--   TODO's can be done until after migration, verify they are in 0049.sql

ALTER TABLE ag.ag_login_surveys
ADD COLUMN source_id uuid;

ALTER TABLE ag.ag_login_surveys
DROP CONSTRAINT fk_ag_login_surveys0;

-- We deprecate the ag_consent and consent_revoked tables, we will migrate
-- all the data out of them, and then remove them in the next change script
-- TODO: Remove ag_consent_backup, consent_revoked_backup in 0049.sql

ALTER TABLE ag.ag_consent RENAME TO ag_consent_backup;

ALTER TABLE ag.consent_revoked RENAME TO consent_revoked_backup;

CREATE INDEX idx_source_account_id_type ON ag.source (account_id, source_type);
CREATE UNIQUE INDEX idx_source_account_id_id ON ag.source (account_id, id);
CREATE TRIGGER update_source_trigger BEFORE UPDATE ON source FOR EACH ROW
  EXECUTE PROCEDURE update_trigger();
