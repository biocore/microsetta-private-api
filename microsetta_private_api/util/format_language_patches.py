import pandas as pd
import click


def _format_update_question(lang, qid, question):
    return (f"UPDATE ag.survey_question SET {lang} = '{question}'\n"
            f"  WHERE survey_question_id = {qid};\n\n")


def _format_update_resp(lang, qid, response, response_index):
    # french likes to use single quotes, and postgres wants ''
    # to escape
    response = response.replace("'", "''")
    return (f"UPDATE ag.survey_question_response \n"
            f"  SET {lang} = '{response}'\n"
            f"  WHERE survey_question_id = {qid} AND\n"
            f"        display_index = {response_index};\n")


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

                        # if the response is nan it means the translation
                        # missed a response
                        if pd.isnull(resp):
                            raise ValueError("Null response: %s" % str(row))

                        out.write(_format_update_resp(lang, qid, resp, respix))
                    out.write('\n')

        # only possible at present once all questions have been translated
        # and there is a legacy survey in the system which does not make sense
        # to translate.
        #out.write("ALTER TABLE ag.survey_question\n"
        #          f"    ALTER COLUMN {lang} SET NOT NULL;")
        #out.write("ALTER TABLE ag.survey_question_response\n"
        #          f"    ALTER COLUMN {lang} SET NOT NULL;")


if __name__ == '__main__':
    mapper()
