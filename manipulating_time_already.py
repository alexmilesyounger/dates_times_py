>>> import datetime # the datetime library will help keep me out of trouble by making sure that i'm using other people's tools for dates and times and not trying to write something myself from scratch. I'm thinking of the the Tom Scott timezone video on Computerphile here. 

>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '_EPOCH', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
# I'll mainly be using date, datetime, time, timedelta, and timezone

>>> datetime.datetime.now() # get the current server time
datetime.datetime(2015, 8, 1, 18, 34, 6, 103190)
# year, month, day, hour (24hour time), minute, second, microsecond

>>> datetime.datetime.now()
datetime.datetime(2015, 8, 1, 18, 34, 27, 480613)

>>> treehouse_start = datetime.datetime.now() # set a start time

>>> treehouse_start
datetime.datetime(2015, 8, 1, 18, 34, 43, 309139)
# instead of running now() each time it's called it holds onto the now of the start

>>> treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)
# the replace() function gives me the ability to set a certain time

>>> treehouse_start
datetime.datetime(2015, 8, 1, 9, 0)

>>> th_start = datetime.datetime(2014, 10, 15, 9)
# you can also set a time by declaring it

>>> th_start
datetime.datetime(2014, 10, 15, 9, 0)
>>> treehouse_start
datetime.datetime(2015, 8, 1, 9, 0)

>>> datetime.datetime.now() - treehouse_start
datetime.timedelta(0, 34622, 823924)
# a timedelta is new, don't totally understand it yet, but in this case it's showing the difference between now() and the starttime

# a timedelta represents a gap in time

>>> time_worked = datetime.datetime.now() - treehouse_start
# get the amount of time I've worked today

>>> time_worked.days
0
# count in days

>>> time_worked.microseconds
821118
# count in microseconds

>>> time_worked.seconds
34680
# count in seconds

>>> dir(time_worked)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']
# check the available methods that I can use on time_worked, which is interesting because it's a variable. I'm guessing it knows I can use the datetime methods because it's datetime information (created with datetime)

>>> hours_worked = round(time_worked.seconds/3600)
# divide by 3600 seconds and you get hours

>>> hours_worked
10
# I didn't really work for 10 hours, I manually adjusted the start time so it would look like I had worked for 10 hours. Tricky, tricky. 