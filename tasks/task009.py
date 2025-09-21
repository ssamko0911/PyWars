# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python

def no_odds(values):
    odds = []

    for value in values:
        if value % 2 == 0:
            odds.append(value)

    return odds
