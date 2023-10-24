"""
The hungman project implemented by DrG


Following the instructions step by step, to accomplish my "first" python full code project.
Two functions, one which asks for input and the other one that checks if it's on target, 
both became methods of class Hangman. Major subsequent changes involves 1) ask_for_input() 
that now stops asking input after 5 "lives"; and 2)  check_guess that extracts the index 
of the letter on target [on-going]; 3) the quality of input must be checked in ask for 
input, i am convinced [on-going]
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
	
	    #### this check shall migrate to ask for input method!
		if len(guess) == 1 and guess.isalpha():
			print("Valid input!")
		else:
			print("Oops! This is not a valid input.") 
	    ####
		
#		unfortunately  self.word is not a list!!!
		for index in self.word:
#		
			if guess in self.word:
				print(f'Good guess! {guess} is in the word.')
				guess = guess.lower()
				print(guess)
				print(index)
				#self.list_of_guesses.append(guess)
#			#### insertion 24 OCT
			# NB: to modify the guess check to memorise the index as well as letter
			
			#	idx = self.word(index)
			#while idx < len(self.word):
				#self.word_guessed.insert(idx,guess)### works but scrambles the word
			#self.word_guessed.append(guess)### works but it makes it very long ...
#					
				#print(self.word_guessed)
				print(*self.list_of_guesses,sep=",")
				#self.num_lives = self.num_lives - 1

####
			else:
				print(f'Sorry, {guess} is not in the word. Try again.')

	## methods: ask_for_input()
	def ask_for_input(self):
		
		while self.num_lives > 0:
			guess = input("Enter one letter:  ")
			print(guess)
			self.check_guess(guess)
			self.num_lives = self.num_lives - 1


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






