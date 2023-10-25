"""
The hungman project implemented by DrG


This is an (imperfect) implementation of the Hungman game, in which the player aims at 
guessing a fruit taken at random from a list of five fruits in input. Hangman is a class containing
two methods, originally developed separately as functions. 
Input: a list, as an argument in the class call; and a letter, by keyboard, prompted 5 times (hangman lives).
Output: print statements evaluating the (alphabetical) input character and whether it matches characters 
in the secret word (randomly generated fruit).  

Usage instruction: 1) in command line type python3 hangman_5.py; 2) type a letter and press enter; 3) when 
prompt, repeat step 2, until the computer reveals either a win or a rasberry.

Licence:  none
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
			
		if guess in self.word:
			print(f'Good guess! {guess} is in the word.')
			guess = guess.lower()
			print(guess)
			
			for idx,letter in enumerate(self.word):
				#print(letter)
				
				if letter == guess:
					self.word_guessed[idx] = guess
					print(self.word_guessed)
					self.num_letters += 1
				print(*self.list_of_guesses,sep=",")
			print(f'num_letters,{self.num_letters}')
			#print("Congratulations!")
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

			if self.num_letters > 0 and self.num_lives == 0:
				print("Congratulations!")

### Hangman end

game = Hangman(["orange","apple","date","grape","pear"])
game.ask_for_input()

### This block prints a list of fruits defined above and the secret word...
#print("print the fruit that was not guessed:   ")
#print(*word_list,sep=",")
###
#print("   prrr!   ")