CREATE TABLE barcodes.interested_users (
    interested_user_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    campaign_id uuid NOT NULL,
    source varchar,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    email varchar NOT NULL,
    phone varchar,
    address_1 varchar,
    address_2 varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    country varchar,
    latitude double precision,
    longitude double precision,
    confirm_consent boolean,
    ip_address varchar,
    creation_time timestamp,
    update_time timestamp,
    address_checked boolean,
    address_valid boolean,
    converted_to_account boolean,
    converted_to_account_time timestamp
);

CREATE TABLE barcodes.campaigns (
    campaign_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    title varchar NOT NULL,
    instructions text,
    header_image varchar,
    permitted_countries text,
    language_key varchar,
    accepting_participants boolean,
    language_key_alt varchar,
    title_alt varchar,
    instructions_alt text
);

CREATE TABLE barcodes.campaigns_projects (
    campaign_id uuid NOT NULL,
    project_id bigint NOT NULL,
    CONSTRAINT campaign_project_pkey PRIMARY KEY ( campaign_id, project_id ),
    CONSTRAINT fk_campaign_id FOREIGN KEY ( campaign_id ) REFERENCES barcodes.campaigns( campaign_id ),
    CONSTRAINT fk_project_id FOREIGN KEY ( project_id ) REFERENCES barcodes.project( project_id )
);
