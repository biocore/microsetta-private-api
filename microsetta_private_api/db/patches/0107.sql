CREATE TABLE barcodes.rack_samples (
    location_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    rack_id varchar NOT NULL,
    sample_id varchar NOT NULL,
    location_row varchar NOT NULL,
    location_col varchar NOT NULL, 
    date_time TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (location_id)
);