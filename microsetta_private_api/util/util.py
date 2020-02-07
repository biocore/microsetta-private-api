import datetime
from flask.json import JSONEncoder

# Need python 3.7 for datetime.fromisotime !!
ISO_FORMAT_8601 = "%Y-%m-%dT%H:%M:%S.%f"


class JsonifyDefaultEncoder(JSONEncoder):
    def default(self, o):
        return json_converter(o)


def fromisotime(s):
    return datetime.datetime.strptime(s, ISO_FORMAT_8601)


def json_converter(o):
    if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
        return o.isoformat()
    return o.__dict__
