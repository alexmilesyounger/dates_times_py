import datetime


def minutes(datetime_one, datetime_two):
	difference = datetime_two - datetime_one
	# we can assume that datetime_two will always be newer
	num_of_minutes = difference.seconds/60
	return round(num_of_minutes)