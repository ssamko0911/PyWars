#https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
class Constraint(object):
    LEN_LIMIT = 2

def array(string):
    items = string.split(',')

    if  len(items) <= Constraint.LEN_LIMIT:
        return None

    for item in items:
        item = item.strip()

    items.pop(0)
    items.pop(len(items) - 1)

    return ' '.join(items)
