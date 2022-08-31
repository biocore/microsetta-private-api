CREATE TABLE ag.delete_account_queue (
    id SERIAL PRIMARY KEY,
    /* foreign key requirement was relaxed because this requirement will
       cause regular delete_account() calls to fail if the account_id is
       in the delete_account_queue. This will cause a cascade of errors
       in unittesting that aren't useful.*/
    account_id uuid UNIQUE NOT NULL, /* REFERENCES ag.account(id), */
    requested_on timestamptz default current_timestamp
);  

CREATE TABLE ag.account_removal_log (
    id SERIAL PRIMARY KEY,
    account_id uuid NOT NULL, /* deleted account.ids can't be referenced here.*/
    /* constraint on admin_id relaxed for similar reasons as above.*/
    admin_id uuid, /* NOT NULL REFERENCES ag.account(id), */
    disposition VARCHAR(8),
    requested_on timestamptz,
    reviewed_on timestamptz default current_timestamp
);
