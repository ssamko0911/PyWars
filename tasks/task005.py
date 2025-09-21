# https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    processed = ''

    for char in string:
        if not char.isalpha():
            processed += char
        elif char.isupper():
            processed += char.lower()
        elif char.islower():
            processed += char.upper()
        else:
            pass

    return processed
