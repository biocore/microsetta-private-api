-- Create table to log geocoding requests

CREATE TABLE ag.google_geocoding (
    geocoding_request_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    request_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    request_address VARCHAR NOT NULL UNIQUE,
    response_body JSONB
);