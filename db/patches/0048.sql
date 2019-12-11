-- create table for individual accounts
CREATE TABLE ag.account (
    id uuid PRIMARY KEY NOT NULL,
    email varchar NOT NULL,
    auth_provider varchar NOT NULL
);

CREATE UNIQUE INDEX idx_account_email ON ag.account ( email );
