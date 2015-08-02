>>> import datetime
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2015, 8, 2, 9, 57, 4, 685311)

>>> now.strftime('%B %d') # strftime() will pretty print a date/time object. Note that it's datetime.datetime.strftime()
'August 02'

>>> now.strftime('%m/%d/%y')
'08/02/15'
# lookup the strftime shortcodes at https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior


# strftime = string from time

# strptime = string parsed into time, converts a string to a datetime.datetime object


>>> birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d') #convert a string to a datetime object

>>> birthday
datetime.datetime(2015, 4, 21, 0, 0)

>>> birthday_party = datetime.datetime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')

>>> birthday_party
datetime.datetime(2015, 4, 21, 12, 0)
