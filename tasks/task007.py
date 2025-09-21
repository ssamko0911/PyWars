# https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python

class Labels(object):
    BOSS_GREETING = 'Hello boss'
    OTHER_GREETING = 'Hello guest'

def greet(name, owner):
    if name == owner:
        return Labels.BOSS_GREETING
    else:
        return Labels.OTHER_GREETING
