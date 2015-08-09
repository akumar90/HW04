
import re

UnitsAndTens = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred' : 100
}

ThousandsAndAbove = {
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000
}


def text2num(s):
    textFrmUsr = re.split("[\s]+", s)
    value = 0
    magnitude = 0
    
    for i in textFrmUsr:
        faceVal = UnitsAndTens.get(i, None)

        if faceVal is not None:
            magnitude += faceVal

        elif i == "hundred":
            magnitude *= 100
        
        else:
            faceVal = ThousandsAndAbove.get(i, None)
            if faceVal is not None:
                value += magnitude * faceVal
                magnitude = 0
            else:
                raise LookupError("Unknown number: "+i)

    return value + magnitude