# https://www.codewars.com/kata/5546180ca783b6d2d5000062/train/python

def squares(num: int, length: int) -> list:
    if 0 >= length:
        return []

    powers = [num]

    for i in range(2, length + 1):
        powers.append(powers[-1] ** 2)

    return powers

# def squares(x,n):
#     return [x**(2**i) for i in range(n)]