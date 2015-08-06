import datetime

starter = datetime.datetime.now()

def time_machine(my_int, my_string):
	# minutes
	if my_string.lower() == "minutes":
		endtime = starter + datetime.timedelta(minutes=my_int)
	# hours
	elif my_string.lower() == "hours":
		endtime = starter + datetime.timedelta(hours=my_int)
	# days
	elif my_string.lower() == "days":
		endtime = starter + datetime.timedelta(days=my_int)
	# years
	elif my_string.lower() == "years":
		endtime = starter + datetime.timedelta(days=(my_int * 365))
	else:
		pass
	return endtime
