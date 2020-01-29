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
-- being accessed by a combination of login id and name
CREATE TABLE ag.source (
    id uuid PRIMARY KEY NOT NULL,
    account_id uuid NOT NULL,
    source_type varchar NOT NULL,
    source_name varchar(200) NOT NULL,
    participant_email varchar,
    is_juvenile bool,
    parent_1_name varchar(200),
    parent_2_name varchar(200),
    deceased_parent bool,
    date_signed date,
    date_revoked date,
    assent_obtainer varchar,
    age_range varchar,
    description varchar,
    creation_time timestamptz default current_timestamp,
    update_time timestamptz default current_timestamp
);

-- We add space for the new source id, we will need to fill it in during the
-- migration.

-- Note:  We cannot make source_id NOT NULL until after we have filled it
-- during the migration.  That constraint will be added in 0049.
ALTER TABLE ag.ag_login_surveys
ADD COLUMN source_id uuid;

-- We add space for the source id in samples as well, as any environmental
-- sourced samples used to specify their environment directly, but now must
-- link to the source table.
-- Note:  We cannot make source_id NOT NULL in ag_kit_barcodes ever, as
-- there is a time point during the process when samples are unassociated with
-- sources.  That said, we can still enforce that samples are assigned sources
-- that do exist within the source table.
ALTER TABLE ag_kit_barcodes
ADD COLUMN source_id uuid;

ALTER TABLE ag_kit_barcodes ADD CONSTRAINT fk_ag_kit_barcodes_sources
FOREIGN KEY (source_id) REFERENCES ag.source (id);

-- Note:  This foreign key reference needs to be detached from ag_consent,
-- as we are detaching that table.  We will replace this foreign key with a
-- new one linking the source table in schema 0049 after the data migration.
ALTER TABLE ag.ag_login_surveys
DROP CONSTRAINT fk_ag_login_surveys0;

-- We deprecate the ag_consent and consent_revoked tables, we will migrate
-- all the data from them

ALTER TABLE ag.ag_consent RENAME TO ag_consent_backup;

ALTER TABLE ag.consent_revoked RENAME TO consent_revoked_backup;

CREATE INDEX idx_source_account_id_type ON ag.source (account_id, source_type);
CREATE UNIQUE INDEX idx_source_account_id_id ON ag.source (account_id, id);
CREATE TRIGGER update_source_trigger BEFORE UPDATE ON source FOR EACH ROW
  EXECUTE PROCEDURE update_trigger();
