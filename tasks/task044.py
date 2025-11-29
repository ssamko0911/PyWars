# https://www.codewars.com/kata/577b9960df78c19bca00007e/train/python

def find_digit(num: int, nth: int) -> int:
    if nth <= 0:
        return -1

    num_as_str: str = str(num)

    if nth > len(num_as_str):
        return 0

    if nth == 1:
        return int(num_as_str[len(num_as_str) - 1])

    return int(num_as_str[-nth:-(nth - 1)])
