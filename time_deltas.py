>>> import datetime
>>> now = datetime.datetime.now() # get a time to work with
>>> now
datetime.datetime(2015, 8, 1, 18, 57, 50, 348201)

>>> datetime.timedelta(hours=5) # create a five hour timedelta
datetime.timedelta(0, 18000) # returned in seconds

>>> datetime.timedelta(days=3) # create a three day timedelta
datetime.timedelta(3) # returned in days

>>> now + datetime.timedelta(days=3) # add a timedelta to a time
datetime.datetime(2015, 8, 4, 18, 57, 50, 348201)

>>> now # the now variable didn't change because I didn't reassign it to the new value
datetime.datetime(2015, 8, 1, 18, 57, 50, 348201)

>>> now + datetime.timedelta(days=-5) # add a negative timedelta
datetime.datetime(2015, 7, 27, 18, 57, 50, 348201)

>>> now - datetime.timedelta(days=5) # subtract a positive timedelta
datetime.datetime(2015, 7, 27, 18, 57, 50, 348201)

>>> now.date() # get just the date info 
datetime.date(2015, 8, 1)

>>> now.time() # get just the time info
datetime.time(18, 57, 50, 348201)

>>> hour = datetime.timedelta(hours=1) # create a variable with a one hour timedelta

>>> hour
datetime.timedelta(0, 3600)

>>> workday = hour * 9 # create a variable with a nine hour time delta (or more properly with nine one hour timedeltas?)

>>> tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1) # create a variable for tomorrow, start with now, replace() the time to 9am, then replace() the day +1

>>> tomorrow
datetime.datetime(2015, 8, 2, 9, 0, 50, 608217)

>>> tomorrow + workday
datetime.datetime(2015, 8, 2, 18, 0, 50, 608217)
# the end of my workday tomorrow

>>> appointment = datetime.timedelta(minutes=45) # create an appointment variable with a 45 minutes timedelta

>>> start = datetime.datetime(2014, 11, 1, 12, 45) # create an appoint start time

>>> end = start + appointment # calculate the end of the appointment by adding start time to the appointment timedelta

>>> end
datetime.datetime(2014, 11, 1, 13, 30) # the time I get out of my appointment
