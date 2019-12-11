-- September 21, 2015
-- remove question 146 from non-human surveys

DELETE FROM ag.survey_answers
WHERE survey_question_id = 146
AND survey_id NOT IN (
    SELECT DISTINCT SA.survey_id
    FROM ag.surveys S
    JOIN ag.group_questions USING (survey_group)
    JOIN ag.survey_question USING (survey_question_id)
    JOIN ag.survey_answers SA USING (survey_question_id)
    WHERE S.survey_id = 1);