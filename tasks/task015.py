# https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python

def search(budget, prices):
    prices.sort()

    result_as_string = ''

    for index, price in enumerate(prices):
        if price <= budget:
            result_as_string += str(price) + ','

    return result_as_string.strip(',')
