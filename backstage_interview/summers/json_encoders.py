import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    ''' This JSON Ecoder supports datetime objects.

    The default JSONEncoder cannot parse a datime object.
    '''
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)

