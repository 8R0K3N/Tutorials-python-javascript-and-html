'''	Description: this is a rock paper scissors game which is more advanced to the previous on, this one uses arrays and random int function apon using a more complex and efficient win system
	Notes: the script is currently working and is functioning as required.
	'''

import random, time

computerHand = ['rock','paper','scissors']

userChoice =  "null"
winner = "null"
Continue = "null"
while Continue != 'n':

	if winner == 'null':

		userChoice = input("would you like to choose? rock, paper or scissors: ")
		computerChoice = random.randint(0, 2)
		if userChoice == computerHand[computerChoice]:
			winner = "tie"
		elif computerChoice == 0:
			if userChoice == 'paper':
				winner = "player"
			else:
				winner = "computer "
		elif computerChoice == 1:
			if userChoice == 'scissors':
				winner = "player"
			else:
				winner = "computer"
		elif computerChoice == 2:
			if userChoice == 'rock':
				winner =  "player"
			else:
				winner = "computer"
		else:
			print("error")

	else:
		if winner != "tie":
			print(winner + " wins\n computer chose: " + computerHand[computerChoice] + "\n player chose: " + userChoice)
		else:
			print(winner + "\n computer chose: " + computerHand[computerChoice] + "\n player chose: " + userChoice)
		time.sleep(1)
		Continue = input("would you like to play again? y/n: ")
		winner = "null"

else:
	exit()
