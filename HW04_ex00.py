#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import textToNumber
import random
import sys
# Body

def create_random_int():
	return random.randint (1,25)

def compare(a,b):
	if(a == b):
		return "True"

	elif(a > b):
		return "too high"

	else :
		return "too low"

def take_input(randomNum):

	numbr = raw_input("Enter a number :")

#	print ("Random number is : "+str(randomNum))

	validate(randomNum, numbr)

def validate_for_int_from_text(randomNum, numbr):
	try:

		int_number_from_Text = textToNumber.text2num(numbr.lower())

		if (1 <= int_number_from_Text and int_number_from_Text <= 25):
			
			compareResult = compare(int_number_from_Text,randomNum)	
			if(compareResult == "True"):
				print ("Congratulations! You did hit the mark my friend")
				sys.exit()

			else :
				print ("Better luck next time")
				print ("Your guess was "+compareResult)

		else :
			raise ArithmeticError

	except ArithmeticError :
		print ("Number entered is not within the limits. Please enter something within 1 to 25")
		print
	
	except Exception as e:
		print ("Invalid input")
		print e


def validate(randomNum, numbr):
	try:
		int_number = int (numbr)
	
	except Exception:
		validate_for_int_from_text(randomNum, numbr)

	else:
		try :
			if (1 <= int_number and int_number <= 25):
				
				compareResult = compare(int_number,randomNum)

				if(compareResult == "True"):
					print ("Congratulations! You did hit the mark my friend")
					print
					sys.exit()

				else :
					print ("Better luck next time")
					print ("Your guess was "+compareResult)

			else :
				raise ArithmeticError

		except ArithmeticError :
			print ("Number entered is not within the limits. Please enter something within 1 to 25")
			print

################################################################################

def main():

	randomNum = create_random_int()
	
	i = 0

	while (i<5):
		take_input(randomNum)
		i += 1

if __name__ == '__main__':
    main()