-- create table for individual accounts
CREATE OR REPLACE FUNCTION update_trigger()
RETURNS TRIGGER AS $$
BEGIN
    NEW.update_time = current_timestamp;
    RETURN NEW;
END
$$ language 'plpgsql';

CREATE TABLE ag.account (
    id uuid PRIMARY KEY NOT NULL,
    email varchar NOT NULL,
    auth_provider varchar NOT NULL,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    address varchar NOT NULL,
    account_type varchar NOT NULL,
    creation_time timestamp default current_timestamp,
    update_time timestamp default current_timestamp
);

CREATE TABLE ag.source (
    id uuid PRIMARY KEY NOT NULL,
    account_id uuid NOT NULL,
    source_type varchar NOT NULL,
    source_data varchar NOT NULL,
    creation_time timestamp default current_timestamp,
    update_time timestamp default current_timestamp
);

CREATE UNIQUE INDEX idx_account_email ON ag.account ( email );
CREATE TRIGGER update_account_trigger BEFORE UPDATE ON account FOR EACH ROW
  EXECUTE PROCEDURE update_trigger();

CREATE INDEX idx_source_account_id ON ag.source ( account_id, source_type);
CREATE TRIGGER update_source_trigger BEFORE UPDATE ON source FOR EACH ROW
  EXECUTE PROCEDURE update_trigger();
