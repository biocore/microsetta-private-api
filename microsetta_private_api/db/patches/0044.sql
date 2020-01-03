-- The loaded vioscreen responses are wrong due to an unchecked parse error:
-- https://github.com/biocore/labadmin/blob/4a2d394232243fd87b7a036ee8f76647f8a3b2b3/knimin/lib/data_access.py#L1788
-- leading to a off-by-one shift in the question / answer assocations.

DELETE FROM ag.external_survey_answers 
    WHERE external_survey_id IN (SELECT external_survey_id 
                                 FROM ag.external_survey_sources
                                 WHERE external_survey='Vioscreen');
DELETE FROM ag.external_survey_sources
    WHERE external_survey='Vioscreen';
