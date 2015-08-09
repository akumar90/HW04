# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

# ROT13 is a weak form of encryption that involves “rotating” each 
# letter in a word by 13 places. To rotate a letter means to shift 
# it through the alphabet, wrapping around to the beginning if necessary,
#  so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

# Write a function called rotate_word that takes a string and an integer 
# as parameters, and that returns a new string that contains the letters 
# from the original string “rotated” by the given amount.

# For example, “cheer” rotated by 7 is “jolly” and “melon” 
# rotated by -10 is “cubed”.

# You might want to use the built-in functions ord, 
# which converts a character to a numeric code, 
# and chr, which converts numeric codes to characters.

def rotate_word(word, rotateBy):
	newWord = ''
	for i in range(0,len(word)):
		
		if(ord(word[i]) >= 65 and ord(word[i]) <=90):
			tempcharNum = ord(word[i]) + rotateBy
			print (tempcharNum)

			if(tempcharNum > 90):
				tempcharNum = ord('A') + (tempcharNum - 90 - 1)

			elif (tempcharNum < 65):
				tempcharNum = ord('Z') - (ord('A') - tempcharNum) + 1

			newWord += chr(tempcharNum)

		elif (ord(word[i]) >= 97 and ord(word[i]) <=122):
			tempcharNum = ord(word[i]) + rotateBy
			
			if(tempcharNum > 122):
				tempcharNum = ord('a') + (tempcharNum - 97 - 1)

			elif (tempcharNum < 97):
				tempcharNum = ord('z') - (ord('a') - tempcharNum) + 1

			newWord += chr(tempcharNum)


		else :
			print ("Error rotating the alphabet : "+word[i])

	return newWord


print (rotate_word("cheer",7))
print (rotate_word("melon",-10))
