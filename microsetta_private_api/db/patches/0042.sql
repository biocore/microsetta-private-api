-- create the new many-to-many relation between barcodes and surveys
CREATE TABLE ag.source_barcodes_surveys (
	barcode              varchar NOT NULL ,
	survey_id            varchar NOT NULL
 );
CREATE INDEX idx_source ON ag.source_barcodes_surveys ( barcode );
CREATE INDEX idx_source_0 ON ag.source_barcodes_surveys ( survey_id );
COMMENT ON COLUMN ag.source_barcodes_surveys.barcode IS 'Points to barcode(s) that are assigned to this source.';
COMMENT ON COLUMN ag.source_barcodes_surveys.survey_id IS 'Points to survey(s) that are assigned to this source.';
ALTER TABLE ag.source_barcodes_surveys ADD CONSTRAINT fk_source_barcode FOREIGN KEY ( barcode ) REFERENCES barcodes.barcode( barcode );
ALTER TABLE ag.source_barcodes_surveys ADD CONSTRAINT fk_source_survey_id FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys (survey_id);


-- create a view of all of the participants with multiple survey ids
CREATE OR REPLACE TEMP VIEW multiple_ids AS
SELECT ag_login_id,
       participant_name,
       unnest(survey_ids) AS survey_id
FROM (SELECT DISTINCT ag_login_id,
                      participant_name,
                      array_agg(survey_id) AS survey_ids
      FROM ag.ag_login_surveys
      GROUP BY ag_login_id, participant_name) AS foo
where array_length(survey_ids, 1) > 1;

-- barcode <-> source relations, with only one survey per source
CREATE OR REPLACE TEMP VIEW single_source_bc_survey AS
SELECT ag_login_id, participant_name, survey_id, barcode
FROM ag.ag_kit_barcodes
JOIN ag.ag_login_surveys USING (survey_id)
WHERE (ag_login_id, participant_name) NOT IN (SELECT DISTINCT ag_login_id, participant_name FROM multiple_ids);

-- view that associates sources and there barcodes (for those sources that have more than one survey)
CREATE OR REPLACE TEMP VIEW multi_source_bc AS
SELECT ag_login_id, participant_name, ag_kit_barcodes.barcode
FROM multiple_ids
LEFT JOIN ag.ag_kit_barcodes USING (survey_id)
WHERE ag_kit_barcodes.barcode IS NOT NULL;
-- (871 rows)

-- assignes all barcodes of a source to all source's surveys (for those sources that have more than one survey)
CREATE OR REPLACE TEMP VIEW multi_source_bc_survey AS
SELECT ag_login_id, participant_name, survey_id, barcode
FROM multiple_ids
JOIN multi_source_bc USING (ag_login_id, participant_name);
-- (1823 rows)
-- (288 rows) distinct sources
-- (871 rows) distinct barcodes
-- (599 rows) distinct surveys !?! 652 --> because some sources with multiple surveys have no barcodes assignes!


-- insert barcode survey (many-to-many) into newly created table
INSERT INTO ag.source_barcodes_surveys (survey_id, barcode)
SELECT survey_id, barcode FROM multi_source_bc_survey UNION SELECT survey_id, barcode FROM single_source_bc_survey;

-- remove views
DROP VIEW multi_source_bc_survey;
DROP VIEW multi_source_bc;
DROP VIEW single_source_bc_survey;
DROP VIEW multiple_ids;

-- see previous patch: this removes the misleading column since data are now stored in source_barcodes_surveys
-- remove incomplete information from other table:
ALTER TABLE ag.ag_kit_barcodes DROP COLUMN survey_id;
