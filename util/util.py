import datetime
from flask.json import JSONEncoder


class JsonifyDefaultEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__


def json_converter(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    return o.__dict__

