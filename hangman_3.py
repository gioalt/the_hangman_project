"""
The hungman project implemented by DrG


Following instructions to accomplish milestone no. 2 ...
there are two functions, one that ask for input and the other that check if it's in target.
however, it asks  once only!
"""


### This chunk generates a random word, the one to guess, from a *fixed list*
import random
word_list = ["orange","apple","date","grape","pear"]
word = random.choice(word_list)
word_1 = word
###


### Function that ask_for_input() and call check_guess() -- iteratively : to do

def ask_for_input():

	guess = input("Enter one letter:  ")
	print(guess)
	return guess
###


### Function that assesses the input guess
def check_guess(guess):
	
	guess = guess.lower()

	if len(guess) == 1 and guess.isalpha():
		print("Valid input!")
	else:
		print("Oops! That is not a valid input.") 

	if guess in word_1:
		print(f'Good guess! {guess} is in the word.')
	else:
		print(f'Sorry, {guess} is not in the word. Try again.')
###
guess = ask_for_input()
check_guess(guess)
###


### This block prints a list of fruits defined above in three ways
print("              ")
print("Temporarily print:   ")
# print, way 1
for i in range(5):
	print(word_list[i])

# another way,
for fruit in word_list:
	print("Favorite fruit:" + fruit)

# print, way 2
print(*word_list,sep=",")
###
