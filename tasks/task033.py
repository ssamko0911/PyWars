# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

def vapor_code(text: str) -> str:
    capitalized = [letter.title() for letter in text if letter != ' ']

    return '  '.join(capitalized)
