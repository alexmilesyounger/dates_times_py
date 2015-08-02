import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
	answer = input("What date would you like? Please use the MM/DD format. Enter 'quit' to quit. ")
	if answer.upper() == 'QUIT':
		break

	try:
		date = datetime.datetime.strptime(answer, answer_format)
		# datetime.datetime.strptime() will qualify whether something is a valid date or not. I'm not sure how it's doing this, but it's just part of what is baked in. I kept thinking we'd have to build something complex to figure this out, but thank you Python for having done the hard work for me already.
		output = link.format(date.strftime(link_format))
		print(output)
	except ValueError:
		# how did he know that if the datetime.datetime.strptime() didn't find the date to be valid it would throw a ValueError? Experience. I guess I could have played around in the shell to figure that out. 
		print("That's not a valid date. Please try again.")