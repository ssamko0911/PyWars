# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python

def uni_total(string):
    char_sum = 0

    for letter in string:
        char_sum += ord(letter)

    return char_sum
