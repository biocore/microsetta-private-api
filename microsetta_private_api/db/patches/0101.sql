CREATE TABLE ag.delete_account_queue (
    id SERIAL PRIMARY KEY,
    account_id uuid NOT NULL REFERENCES ag.account(id),
    requested_on timestamptz default current_timestamp
);  

CREATE TABLE ag.account_removal_log (
    id SERIAL PRIMARY KEY,
    account_id uuid NOT NULL REFERENCES ag.account(id),
    admin_id uuid NOT NULL REFERENCES ag.account(id),
    disposition VARCHAR(8),
    requested_on timestamptz,
    reviewed_on timestamptz default current_timestamp
);  
