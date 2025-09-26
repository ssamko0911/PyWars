#https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python

def remove_rotten(bag_of_fruits):
    slice_from = len('rotten')
    ripe_fruits = []

    if not bag_of_fruits:
        return []

    for fruit in bag_of_fruits:
        if fruit.startswith('rotten'):
            ripe_fruits.append(fruit[slice_from:].lower())
        else:
            ripe_fruits.append(fruit)

    return ripe_fruits
