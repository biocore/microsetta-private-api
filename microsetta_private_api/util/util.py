import datetime
from flask.json import JSONEncoder


class JsonifyDefaultEncoder(JSONEncoder):
    def default(self, o):
        return json_converter(o)


def json_converter(o):
    if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
        return str(o)
    return o.__dict__
