CREATE TABLE ag.interested_users (
interested_user_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
first_name varchar,
last_name varchar,
email varchar,
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
address_valid boolean
);

CREATE TABLE ag.campaigns (
campaign_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
title varchar,
instructions text,
header_image varchar,
permitted_countries text,
language_key varchar,
accepting_participants boolean,
associated_projects text,
language_key_alt varchar,
title_alt varchar,
instructions_alt text
);