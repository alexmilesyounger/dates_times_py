import datetime
import random

from questions import Add, Multiply

# a nice formatting habit is to list standard library imports at the very top and then list local custom imports a line down. This notation will let me easily see what is custom and what is standard as well as where modules are coming from


class Quiz:
	questions = []
	answers = []

	def __init__(self):
		question_types = (Add, Multiply)
		for _ in range(10): # the underscore tells Python that we don't really care about the value we just care about doing it 10 time. 
			num1 = random.randint(1, 10)
			num2 = random.randint(1, 10)
			question = random.choice(question_types)(num1, num2)
			self.questions.append(question)

	def take_quiz(self):
		# log the start time
		# ask all of the questions
		# log if they got the question right
		# log the end time
		# show a summary
		pass

	def ask(self, question):
		# log the start time
		# capture the answer
		# check the answer
		# log the end time
		# if the answer is right, send back True
		# otherwise, send back False
		# send back the elapsed time, too
		pass

	def total_correct(self):
		total = 0
		for answer in self.answers: # iterate through the list of answers
			if answer[0]: # each answer is also a list, the first item of an answer's list is a Boolean, and if the Boolean is set to True then this if statement will increment the total by one
				total += 1
		return total

	def summary(self):
		print("You got {} out of {} right.".format(
			self.total_correct(), len(self.questions)))
		print("It took you {} seconds total.".format(
			(self.end_time - self.start_time).seconds)) 