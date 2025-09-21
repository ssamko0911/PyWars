# https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python

def is_digit(s):
    trimmed = s.strip()

    try:
        float(trimmed)
        return True
    except ValueError:
        return False
