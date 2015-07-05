import random

def roller():
	nod = input("Enter number of dice to be rolled: ")
	nos = input("Enter number of sides in each die: ")
	try:
		numberOfDice = int(nod)
		numberOfSides = int(nos)
	except ValueError:
		print("Please enter numbers only.")
		askAgain()
	#Rolling dice
	roll(numberOfDice, numberOfSides)

def askAgain():
	ans = input("Do you want to try again (yes/no)")
	ans = ans.lower()
	if (ans == "yes" or ans == "y"):
		roller()
	else:
		print("Thanks for playing!")

def roll(numberOfDice, numberOfSides):
	#Error Cases
	if (numberOfDice < 1):
		print("Number of dice must be at least 1.")
		askAgain()
	elif (numberOfSides < 6):
		print("A die must have at least 6 sides.")
		askAgain()
	else:
		#safe to continue
		#Rolling through each die
		for i in range(1, numberOfDice + 1):
			print("Die ", i, " rolled ", random.randint(1, numberOfSides))
			
	#Finished once
	askAgain()