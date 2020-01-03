CREATE TABLE ag.external_survey_sources (
	external_survey_id   bigserial  NOT NULL,
	external_survey      varchar  NOT NULL,
	external_survey_description varchar  ,
	external_survey_url varchar  NOT NULL,
	CONSTRAINT pk_external_surveys PRIMARY KEY ( external_survey_id )
 );

CREATE TABLE ag.external_survey_answers (
	survey_id            varchar  NOT NULL,
	external_survey_id   bigint  NOT NULL,
	pulldown_date        date  NOT NULL,
	answers              json  NOT NULL,
	CONSTRAINT pk_third_party_surveys PRIMARY KEY ( survey_id, external_survey_id, pulldown_date )
 );

CREATE INDEX idx_external_survey ON ag.external_survey_answers ( external_survey_id );

COMMENT ON TABLE ag.external_survey_answers IS 'This stores answers to third party surveys in JSON format, keyed to the original survey ID';

ALTER TABLE ag.external_survey_answers ADD CONSTRAINT fk_third_party_surveys FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys( survey_id );

ALTER TABLE ag.external_survey_answers ADD CONSTRAINT fk_external_survey FOREIGN KEY ( external_survey_id ) REFERENCES ag.external_survey_sources( external_survey_id );