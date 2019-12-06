-- create table for individual accounts
CREATE TABLE ag.account (
    id uuid PRIMARY KEY NOT NULL,
    email varchar NOT NULL,
    auth_provider varchar NOT NULL
);

CREATE UNIQUE INDEX idx_account_email ON ag.account ( email );

CREATE TABLE ag.

CREATE TABLE barcodes.project_qiita_buffer_status (
    id integer,
    state varchar,
    CONSTRAINT pk_project_qiita_buffer_status PRIMARY KEY (id)
);

INSERT INTO barcodes.project_qiita_buffer_status (id, state) VALUES (0, 'Idle');
