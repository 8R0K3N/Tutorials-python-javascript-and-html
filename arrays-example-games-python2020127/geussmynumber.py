'''     Description:  this is a simple geuss my number game of which the random int function is mainly used.
	Notes: script is functioning as required.
	'''

import random, time
choice = 0
number = random.randint(1,10)
while choice != 11:
	choice = int(input("guess my number between 1 and 10, type 11 to exit: "))
	if choice == number:
		print("you win")
		time.sleep(1)
		exit()
	elif choice > number:
		print("too high, guess lower")
	elif choice < number:
		print("too low, guess higher")
else:
	exit()
