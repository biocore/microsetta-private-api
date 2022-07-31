CREATE TABLE ag.delete_account_queue (
    id SERIAL PRIMARY KEY,
    account_id uuid UNIQUE NOT NULL REFERENCES ag.account(id),
    requested_on timestamptz default current_timestamp
);  

