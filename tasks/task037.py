#https://www.codewars.com/kata/552564a82142d701f5001228/train/python

def discover_original_price(discounted_price: int|float, sale_percentage: int|float) -> int|float:
    return (discounted_price * 100) / (100 - sale_percentage)
