import psycopg2
import sys
import pandas as pd
import numpy as np

con = psycopg2.connect(host='localhost', database='ag_test')
cursor = con.cursor()
sid = int(sys.argv[1])

sql = """SELECT survey_question_id,
        survey_group,
        american,
        question_shortname,
        response,
        ag.survey_question_response.display_index
            AS response_index
     FROM ag.survey_question
     LEFT JOIN ag.survey_question_response
         USING (survey_question_id)
     LEFT JOIN ag.group_questions USING (survey_question_id)
     LEFT JOIN ag.surveys USING (survey_group)
     WHERE survey_id = %d""" % sid
df = pd.read_sql(sql, con)


# sorts so that questions emmulate survey order
df = df.sort_values(by=['survey_group',
            'survey_question_id',
            'response_index']).drop(columns='survey_group')
df['response_index'] = df['response_index'].apply(lambda x: None if np.isnan(x) else int(x), convert_dtype=False)
df.to_csv(sys.argv[2], sep='\t', index=False, header=True)
