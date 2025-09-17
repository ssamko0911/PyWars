#https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python

class Labels:
    TEXT = 'Who ate the last cookie? It was %s!'
    STR_NAME = 'Zach'
    INT_NAME = 'Monica'
    GENERIC_NAME = 'the dog'

def cookie(x):
    if type(x) == str:
        return Labels.TEXT % Labels.STR_NAME
    elif type(x) == int or type(x) == float:
        return Labels.TEXT % Labels.INT_NAME
    else:
        return Labels.TEXT % Labels.GENERIC_NAME
