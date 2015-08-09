#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count(word, char):
	count = 0

	for letter in word:
		if (letter == char):
			count +=1

	print ("Count of '"+char+"' in '"+word+"' is : "+str(count))



################################################################################
def main():

    count ("abcabcabcabcabc","a")

if __name__ == '__main__':
    main()