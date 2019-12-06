/*
29 October 2014
---------------
We would like to keep track of which survey_ids correspond to "promoted"
surveys, which are surveys that existed in the old (Oracle) database that we
are porting into the new structure. We aren't sure why we will/might need this,
but better safe than sorry!
*/
CREATE TABLE ag.promoted_survey_ids ( 
	survey_id            varchar  NOT NULL,
	CONSTRAINT pk_promoted_survey_ids PRIMARY KEY ( survey_id )
 ) ;

COMMENT ON TABLE ag.promoted_survey_ids IS 'Keeps track of the survey_ids that correspond to surveys that were ported from first questionnaire to the second';

ALTER TABLE ag.promoted_survey_ids ADD CONSTRAINT fk_promoted_survey_ids FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys( survey_id )    ;

/*
This survey question was "dangling" (it was not in any group and was not
triggered by any other question), so it should be removed.
*/

DELETE FROM survey_question_response_type WHERE survey_question_id = 102;
DELETE FROM survey_question WHERE survey_question_id = 102;
