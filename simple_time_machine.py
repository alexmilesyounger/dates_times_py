import datetime


def delorean(my_int):
	starter = datetime.datetime(2015, 10, 21, 16, 29)
	my_delta = datetime.timedelta(hours=my_int)
	return starter + my_delta
