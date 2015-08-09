#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body  

def any_lowercase1(s):
    """Explain what is wrong, if anything, here."""

    """The method will end just after one iteration,
    since there are return statements in the if as well as else
    block. 
    Hence, depending upon what the first character is in the string,
    the answer will change.

    Example : Lets say s = "Ankur"
    Clearly this has lowercase characters, so the answer we are expecting is True
    But, this method will return False as the first character is in CAPS"""

    for c in s:
        if c.islower():
            return True
        else:
            return False



def any_lowercase2(s):
    """Explain what is wrong, if anything, here."""

    """This will always return True.
    Because in the if condition, 'c' instead of c has been written.
    'c' is a lowercase character, so the method always returns True,
    irrespective of the value parsed"""

    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Explain what is wrong, if anything, here."""

    """This method will return the flag value based on the
    last character of the string, since everytime the for loop
    runs, it overwrites the flag value."""

    for c in s:
        flag = c.islower()

    return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here."""

    "Finally !  Nothing wrong here"

    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Explain what is wrong, if anything, here."""

    """This will return False the instant the loop encounters a CAPS
    character. That is not what we are expecting"""

    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    
    print ("Lowercase1 : "+str(any_lowercase1("This will return an incorrect value")))

    print ("Lowercase2 : "+str(any_lowercase2("THIS WILL RETURN AN INCORRECT VALUE")))

    print ("Lowercase3 : "+str(any_lowercase3("this will return an incorrect valuE")))
    
    

if __name__ == '__main__':
    main()