from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.source import Source, \
    HumanInfo, AnimalInfo, EnvironmentInfo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
import datetime
import json
import microsetta_private_api.util.vue_adapter

# TODO: Refactor me into proper unit tests!


def json_converter(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    elif isinstance(o, datetime.date):
        return str(o)
    return o.__dict__


ACCT_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"
HUMAN_ID = "b0b0b0b0-b0b0-b0b0-b0b0-b0b0b0b0b0b0"
DOGGY_ID = "dddddddd-dddd-dddd-dddd-dddddddddddd"
PLANTY_ID = "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee"


with Transaction() as t:
    source_repo = SourceRepo(t)
    acct_repo = AccountRepo(t)
    source_repo.delete_source(ACCT_ID, DOGGY_ID)
    source_repo.delete_source(ACCT_ID, PLANTY_ID)
    source_repo.delete_source(ACCT_ID, HUMAN_ID)
    acct_repo.delete_account(ACCT_ID)
    t.commit()


with Transaction() as t:
    acct_repo = AccountRepo(t)
    kit_repo = KitRepo(t)
    kit = kit_repo.get_kit("eba20873-b88d-33cc-e040-8a80115d392c", "#6á$E")
    print("Kit: ")
    print(json.dumps(kit, default=json_converter, indent=2))

    acc = Account(ACCT_ID,
                  "foo@baz.com",
                  "standard",
                  "https://RepoTestScratch.dancode",
                  "THISSUBISNOTREAL",
                  "Dan",
                  "H",
                  {
                      "street": "123 Dan Lane",
                      "city": "Danville",
                      "state": "CA",
                      "post_code": 12345,
                      "country_code": "US"
                  })
    print(acct_repo.create_account(acc))
    t.commit()

with Transaction() as t:
    acct_repo = AccountRepo(t)
    acc = acct_repo.get_account(ACCT_ID)
    print("Account: ")
    print(json.dumps(acc, default=json_converter, indent=2))

with Transaction() as t:
    acct_repo = AccountRepo(t)
    acc = acct_repo.get_account(ACCT_ID)
    acc.last_name = "The Greatest"
    acct_repo.update_account(acc)
    acc = acct_repo.get_account(ACCT_ID)
    print("Account: ")
    print(json.dumps(acc, default=json_converter, indent=2))
    t.commit()

with Transaction() as t:
    source_repo = SourceRepo(t)

    source_repo.create_source(Source.create_human(
        HUMAN_ID,
        ACCT_ID,
        HumanInfo("Bo", "bo@bo.com", False, "Mr Bo", "Mrs Bo",
                  False, datetime.datetime.utcnow(), None, "Mr. Obtainer",
                  "18-plus")
    ))
    source_repo.create_source(Source.create_animal(
        DOGGY_ID,
        ACCT_ID,
        AnimalInfo("Doggy")))
    source_repo.create_source(Source.create_environment(
        PLANTY_ID,
        ACCT_ID,
        EnvironmentInfo("Planty", "The green one")))

    doggy = source_repo.get_source(ACCT_ID, DOGGY_ID)
    planty = source_repo.get_source(ACCT_ID, PLANTY_ID)
    all_sources = source_repo.get_sources_in_account(ACCT_ID)
    just_plants = source_repo.get_sources_in_account(ACCT_ID, "environmental")

    print("Doggy:")
    print(json.dumps(doggy, default=json_converter, indent=2))

    print("Planty:")
    print(json.dumps(planty, default=json_converter, indent=2))

    print("All:")
    print(json.dumps(all_sources, default=json_converter, indent=2))

    print("Just Plants:")
    print(json.dumps(just_plants, default=json_converter, indent=2))
    t.commit()

with Transaction() as t:
    survey_template_repo = SurveyTemplateRepo(t)
    ids = survey_template_repo.list_survey_ids()
    print(ids)

    the_stuff = survey_template_repo.get_survey_template(ids[0])
    # print(json.dumps(the_stuff.groups[0].questions[10],
    #                  default=json_converter,
    #                  indent=2))

    in_vue = microsetta_private_api.util.vue_adapter.to_vue_schema(the_stuff)
    # print(json.dumps(in_vue, default=json_converter, indent=2))

    with open("surveySchema.json", "w") as outFile:
        outFile.write(json.dumps(in_vue, default=json_converter, indent=2))
