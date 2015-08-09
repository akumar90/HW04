#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math

# Body

def evaluate(s):
	try:
		value = str(eval(s))
		print ("The value of the expression '"+s+"' is "+value)
		return value

	except Exception as e:
		print ("Error while evaluating the expression")
		raise Exception


def eval_loop():

	finalReturn = "N/A"

	while(True):
		try:
			s = raw_input("Enter the expression : ")
		
			if(s != "done"):
				finalReturn = evaluate(s)

			else :
				print ("Value of the previous expression : "+finalReturn)
				break

		except Exception as e:
			pass


################################################################################
def main():
    
    eval_loop()
    

if __name__ == '__main__':
    main()