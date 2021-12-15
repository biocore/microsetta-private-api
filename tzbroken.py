import datetime
import time
import pytz
x = pytz.timezone('US/Pacific')
y = datetime.datetime(2017,5,26,15,30,16)
z = x.localize(y)

# without pytz
print(time.mktime(y.timetuple()))

print(y.timetuple())
print(z.timetuple())

# recommended test from stub42
print(time.mktime((2017,5,26,15,30,16,4,146,1)))

# with pytz
print(time.mktime(z.timetuple()))
