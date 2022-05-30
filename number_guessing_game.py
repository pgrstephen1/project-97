print("number guessing game")

import random
number = random.choice(range(1,9))

guess = int(input("enter a number from 1-9: "))

chances = 1
while chances < 5:
	chances=chances+1
	if(guess < number):
		print("Incorrect number. Guess a higher number")
		guess = int(input("enter a number from 1-9: "))
	elif(guess > number):
		print("Incorrect number. Guess a lower number")
		guess = int(input("enter a number from 1-9: "))
	if(number==guess):
		print("Correct number! You win!")
		break

if not chances < 5:
	print("You Lose !!! the number is", number)

