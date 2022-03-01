CREATE TABLE source_host_subject_id (
    source_id UUID PRIMARY KEY,
    host_subject_id VARCHAR NOT NULL,
    CONSTRAINT fk_source_hsi FOREIGN KEY (source_id) REFERENCES ag.source(id)
);
