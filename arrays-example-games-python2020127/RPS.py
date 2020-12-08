'''	Description: this is a simple rock paper scissors game of which arrays and random in function is used.
	Notes: script is minimul but runs correctly.
	'''
import random

computerHand = ['rock','paper','scissors']

userChoice = input("would you like to play? y/n: ")

if userChoice == 'y':
    userChoice = input("would you like to choose? Rock, Paper or Scissors: ")
    computerChoice = random.randint(0, 2)
    print("player1 choice: " + userChoice + "\n" + "computersChoice: " + computerHand[computerChoice])

else:
    exit()
