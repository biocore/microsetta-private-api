CREATE TABLE ag.melissa_address_queries (
id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
query_timestamp timestamp,
source_address_1 varchar,
source_address_2 varchar,
source_city varchar,
source_state varchar,
source_postal varchar,
source_country varchar,
source_url text,
result_raw text,
result_codes varchar,
result_good boolean,
result_formatted_address text,
result_address_1 varchar,
result_address_2 varchar,
result_city varchar,
result_state varchar,
result_postal varchar,
result_country varchar,
result_latitude double precision,
result_longitude double precision
);

