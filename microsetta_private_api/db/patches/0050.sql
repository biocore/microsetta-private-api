-- This script enables the migration of ag.ag_login into the new schema for
-- accounts.

-- Build update triggers for setting timestamps
CREATE OR REPLACE FUNCTION update_trigger()
RETURNS TRIGGER AS $$
BEGIN
    NEW.update_time = current_timestamp;
    RETURN NEW;
END
$$ language 'plpgsql';

ALTER TABLE ag.ag_login RENAME TO ag_login_backup;

-- create table for individual accounts.  Migrated accounts will use
-- the ag_login_id as their id.
CREATE TABLE ag.account (
    id uuid PRIMARY KEY NOT NULL,
    email varchar,
    account_type varchar NOT NULL,
    auth_issuer varchar,
    auth_sub varchar,
    first_name varchar,
    last_name varchar,
    street varchar,
    city varchar,
    state varchar,
    post_code varchar,
    country_code varchar,
    latitude double precision,
    longitude double precision,
    cannot_geocode character(1),
    elevation double precision,
    creation_time timestamptz default current_timestamp,
    update_time timestamptz default current_timestamp
);

CREATE UNIQUE INDEX idx_account_email ON ag.account ( email );
CREATE UNIQUE INDEX idx_account_issuer_sub ON ag.account
( auth_issuer, auth_sub );
CREATE TRIGGER update_account_trigger BEFORE UPDATE ON account FOR EACH ROW
  EXECUTE PROCEDURE update_trigger();

