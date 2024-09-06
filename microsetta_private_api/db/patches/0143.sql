-- Associate Qiita Studies with TMI Projects - Phase 1
-- Add qitta study id column to barcodes - project
ALTER TABLE barcodes.project
ADD COLUMN qiita_study_id VARCHAR;

ALTER TABLE barcodes.project
ADD CONSTRAINT qiita_study_id_unique UNIQUE (qiita_study_id);

-- Create new table for qiita api auth
CREATE TABLE barcodes.qiita_api_authentication (
    qiita_study_id VARCHAR NOT NULL,
    qiita_client_id BIGINT,
    qiita_client_secret VARCHAR,
    FOREIGN KEY (qiita_study_id) REFERENCES barcodes.project(qiita_study_id)
);


