import datetime
import time
import pytz
x = pytz.timezone('US/Pacific')
y = datetime.datetime(2017,5,26,15,30,16)
z = x.localize(y)
print(time.mktime(z.timetuple()))
