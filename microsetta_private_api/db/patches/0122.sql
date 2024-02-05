CREATE TABLE ag.delete_account_queue (
    id SERIAL PRIMARY KEY,
    account_id uuid UNIQUE NOT NULL REFERENCES ag.account(id),
    requested_on timestamptz default current_timestamp
);  

CREATE TYPE DISPOSITION_TYPE AS ENUM ('ignored', 'deleted');
CREATE TABLE ag.account_removal_log (
    id SERIAL PRIMARY KEY,
    -- account_id is not referenced to ag.account(id) so that the account may
    -- be deleted and the record of it kept afterward.
    account_id uuid NOT NULL,
    admin_id uuid NOT NULL REFERENCES ag.account(id),
    -- although a method exists to remove entries from this table, the
    -- intention is to record the admin who accepted or denied the request
    -- here. This means that an account_id may appear more than once if the
    -- user makes multiple requests.
    disposition DISPOSITION_TYPE,
    requested_on timestamptz,
    reviewed_on timestamptz default current_timestamp,
    delete_reason VARCHAR
);
