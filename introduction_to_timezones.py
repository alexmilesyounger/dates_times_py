>>> import datetime
>>> # when we create a datetime object we can specify a timezone
... # when we do that we say that the object is "aware" and that
... # it knows where it is in the world and how to relate to other
... # datetime or time objects. An object that doesn't know its
... # timezone is said to be "naive" or "unaware."
...
>>> pacific = datetime.timezone(datetime.timedelta(hours=-8))
>>> # pacific is 8 hours off from UTC time
...
>>> eastern = datetime.timezone(datetime.timedelta(hours=-5))
>>> # eastern is 5 hours off from UTC time
...
>>> naive = datetime.datetime(2014, 4, 21, 9)
>>> naive
datetime.datetime(2014, 4, 21, 9, 0)
>>> aware = datetime.datetime(2014, 4, 21, 9, 0, tzinfo=pacific)
>>> aware
datetime.datetime(2014, 4, 21, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 57600)))
>>> naive.astimezone(eastern)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: astimezone() cannot be applied to a naive datetime
>>> aware.astimezone(eastern)
datetime.datetime(2014, 4, 21, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 68400)))
>>> # you can apply astimezone() to an aware datetime object, but not a naive one
... # because the astimezone() method works off the tzinfo and if there is no tzinfo it
... # has nothing to work off of. It's like trying to add 3 hours to null (not zero, null).
...
>>> auckland = datetime.timezone(datetime.timedelta(hours=13))
>>> aware.astimezone(auckland)
datetime.datetime(2014, 4, 22, 6, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 46800)))
>>> mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
>>> aware.astimezone(mumbai)
datetime.datetime(2014, 4, 21, 22, 30, tzinfo=datetime.timezone(datetime.timedelta(0, 19800)))
>>>