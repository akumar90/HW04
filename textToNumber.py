
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

#hundred thousand three hundred forty four
def text2num(s):
    a = re.split("[\s]+", s)
    n = 0
    g = 0
    for w in a:
        x = UnitsAndTens.get(w, None)

        if x is not None:
            g += x

        elif w == "hundred":
            g *= 100
        else:
            x = ThousandsAndAbove.get(w, None)
            if x is not None:
                n += g * x
                g = 0
            else:
                raise LookupError("Unknown number: "+w)

    return n + g