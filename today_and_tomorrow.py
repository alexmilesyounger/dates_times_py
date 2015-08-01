>>> import datetime

>>> now = datetime.datetime.now() # now() method
>>> today = datetime.datetime.today() # today() method
>>> now
datetime.datetime(2015, 8, 1, 19, 15, 50, 373988)
>>> today
datetime.datetime(2015, 8, 1, 19, 15, 57, 129226)
# now() can take a timezone as an argument, but today() can't
# otherwise they're very similar


>>> today = datetime.datetime.combine(datetime.date.today(), datetime.time())
>>> today
datetime.datetime(2015, 8, 1, 0, 0)
# use the combine() method to create a today variable which is the current day, but wherein the time is set to exactly midnight a.k.a. the start of the day


>>> today.month
8
>>> today.hour
0
>>> today.year
2015
>>> now.hour
19
>>> today.weekday()
5
# in Python weeks start on Monday, and Monday = 0


>>> now.timestamp()
1438470950.373988
# this is a POSIX timestamp, also known as Unix time or erroneously as Epoch time. The Epoch started on Thursday, January 1st, 1970 at 00:00:00

# because Unix time doesn't handle leap seconds it is neither a linear representation of time nor a true representation of UTC.

# POSIX is an achronim for Portable Operating System Interface