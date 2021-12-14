import datetime
import time
import pytz
x = pytz.timezone('US/Pacific')
y = datetime.datetime(2017,5,26,15,30,16)
z = x.localize(y)
try:
    print(time.mktime(z.timetuple()))
except Exception as e:
    print(repr(e))

try:
    print(time.mktime(y.timetuple()))
except Exception as e:
    print(repr(e))

raise ValueError("trigger build failure")
