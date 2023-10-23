"""
The hungman project implemented by DrG


Following the instructions step by step, to accomplish my "first" python code project.
Two functions, one that asks for input and the other that checks if it's in target, become
both methods of a class Hangman at this stage
"""

import random

### Hangman class, attributes word_list (list) and num_lives(int)
class Hangman:

	## class constructor with attributes
	def __init__(self, word_list, num_lives=5):
		
		# initialise the class as prescribed
		self.word_list = word_list
		self.num_lives = num_lives

		### generates a random word, the one to guess, from a *fixed list*
		self.word_list = ["orange","apple","date","grape","pear"]
		self.word = random.choice(word_list)
		
		### create a scaffold list with word letters to guess  ...
		self.word_guessed = ["_"] * len(self.word)
		self.list_of_guesses = list()
		self.num_letters  = 0
		###


	## methods: check_guess()
	def check_guess(self,guess):
	
		if len(guess) == 1 and guess.isalpha():
			print("Valid input!")
		else:
			print("Oops! This is not a valid input.") 

		if guess in self.word:
			print(f'Good guess! {guess} is in the word.')
			guess = guess.lower()
			print(guess)
		else:
			print(f'Sorry, {guess} is not in the word. Try again.')

	## methods: ask_for_input()
	def ask_for_input(self):
		
		while True:
			guess = input("Enter one letter:  ")
			print(guess)
			self.check_guess(guess)

### Hangman end

#game= Hangman()
game = Hangman(["orange","apple","date","grape","pear"])
game.ask_for_input()

### This block prints a list of fruits defined above and the secret word...  not anymore

print("print the list of fruits, to help develop:   ")
#print(word)

# print, way 2
#print(*word_list,sep=",")
###
print("         prrr!     ")






