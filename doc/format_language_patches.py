import pandas as pd
import click
from psycopg2 import connect, sql

_conn = connect(host='localhost', database='ag_test')
_update_question = sql.SQL("UPDATE ag.survey_question "
                           "SET {lang} = {question} "
                           "WHERE survey_question_id = {qid};")
_update_response = sql.SQL("UPDATE ag.survey_question_response "
                           "SET {lang} = {response} "
                           "WHERE survey_question_id = {qid} AND "
                           "    display_index = {response_index};")
_update_survey_response = sql.SQL("UPDATE ag.survey_response "
                                  "SET {language_field} = {response}, "
                                  "WHERE response = {american_response};")


def _format_update_survey_resp(american_response, language_field, response):
    fmt = _update_survey_response.format(american_response=sql.Literal(american_response),
                                         language_field=sql.Identifier(language_field),
                                         response=sql.Literal(response))

    return fmt.as_string(_conn) + '\n'

def _format_update_question(lang, qid, question):
    fmt = _update_question.format(lang=sql.Identifier(lang),
                                  question=sql.Literal(question),
                                  qid=sql.Literal(qid))
    return fmt.as_string(_conn) + '\n'


def _format_update_resp(lang, qid, response, response_index):
    fmt = _update_response.format(lang=sql.Identifier(lang),
                                  response=sql.Literal(response),
                                  qid=sql.Literal(qid),
                                  response_index=sql.Literal(response_index))
    return fmt.as_string(_conn) + '\n'


@click.command()
@click.option('--input', type=click.Path(exists=True), required=True,
              help="Input excel spreadsheet w/ translations")
@click.option('--output', type=click.Path(exists=False), required=True,
              help="The patch file to write")
@click.option('--lang', type=str, required=True,
              help="The name of the language")
def mapper(input, output, lang):
    def stripper(x):
        if pd.isnull(x):
            return None
        else:
            return str.strip(x)

    # sheet_name=None -> load all sheets
    sheets = pd.read_excel(input, dtype=str, sheet_name=None)

    with open(output, 'w') as out:
        out.write("ALTER TABLE ag.survey_question\n"
                  "    ADD COLUMN %s varchar;\n" % lang)
        out.write("ALTER TABLE ag.survey_question_response\n"
                  "    ADD COLUMN %s varchar;\n" % lang)

        for sheet, df in sheets.items():
            # we use row['american'] as the translated spreadsheets
            # did not alter the header
            df['american'] = df['american'].apply(stripper)
            df['response'] = df['response'].apply(stripper)

            for qid, qblock in df.groupby('survey_question_id'):
                i = qblock.iloc[0]

                # we use row['american'] as the translated spreadsheets
                # did not alter the header
                out.write(_format_update_question(lang, qid, i['american']))

                if len(qblock) == 1 and not pd.isnull(i['response_index']):
                    raise ValueError("Unexpected null on qid: %s" % qid)
                elif len(qblock) == 1:
                    # no response to add (e.g., free text)
                    continue
                else:
                    for row in qblock.itertuples():
                        resp = row.response
                        respix = row.response_index
                        amer = row.american
                        # if the response is nan it means the translation
                        # missed a response
                        if pd.isnull(resp):
                            raise ValueError("Null response: %s" % str(row))

                        out.write(_format_update_resp(lang, qid, resp, respix))
                        out.write(_format_update_survey_resp(amer, lang, resp))


if __name__ == '__main__':
    mapper()
