DROP INDEX campaign.source_address_composite;
DROP INDEX campaign.result_address_composite;

ALTER TABLE campaign.melissa_address_queries ADD COLUMN source_address_3 VARCHAR;
ALTER TABLE campaign.melissa_address_queries ADD COLUMN result_address_3 VARCHAR;

CREATE INDEX idx_melissa_source_address ON campaign.melissa_address_queries (source_address_1, source_address_2, source_address_3, source_postal, source_country, result_processed);
CREATE INDEX idx_melissa_result_address ON campaign.melissa_address_queries (result_address_1, result_address_2, result_address_3, result_postal, result_country, result_processed);
