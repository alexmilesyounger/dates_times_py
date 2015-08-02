import datetime

# accept a date and a time from the user
def get_date_and_time():
	date = input("Please enter a date (MM-DD-YYYY): ")
	time = input("Please enter a time (24:00... no a.m. or p.m.): ")

	# convert those variables in to datetimes strptime()
	date_obj = datetime.datetime.strptime(date, '%m-%d-%Y')
	time_obj = datetime.datetime.strptime(time, '%H:%M')
	full_date_and_time = datetime.datetime.combine(date_obj, time_obj)

# lookup the wikipedia page for that date and time

get_date_and_time()