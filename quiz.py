import datetime
import random

from questions import Add, Multiply

# a nice formatting habit is to list standard library imports at the very top and then list local custom imports a line down. This notation will let me easily see what is custom and what is standard as well as where modules are coming from


class Quiz:
	questions = []
	answers = []

	def __init__(self):
		# generate 10 random questions with numbers from 1 to 10
		# add these questions into self.questions

	def take_quiz(self):
		# log the start time
		# ask all of the questions
		# log if they got the question right
		# log the end time
		# show a summary

	def ask(self, question):
		# log the start time
		# capture the answer
		# check the answer
		# log the end time
		# if the answer is right, send back True
		# otherwise, send back False
		# send back the elapsed time, too

	def summary(self):
		# print how many you got right and the total # of questions. 5/10
		# print the total time for the quiz: 30 seconds! 