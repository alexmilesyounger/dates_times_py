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
		self.start_time = datetime.datetime.now()
		for question in self.questions:
			self.answers.append(self.ask(question))
		else: # the else should really be "then" because it only happens if the for loop successfully completes. This is a huge new piece of functionality.
			self.end_time = datetime.datetime.now()
		return self.summary()

	def ask(self, question):
		correct = False
		question_start = datetime.datetime.now()
		answer = input(question.text + ' = ')
		if answer == str(question.answer):
			correct = True
		question_end = datetime.datetime.now()
		return correct, question_end - question_start
		

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


Quiz().take_quiz()