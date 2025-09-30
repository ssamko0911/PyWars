# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python

def double_char(text: str) -> str:
    doubled_text = ''

    for char in text:
        doubled_text += char * 2

    return doubled_text
