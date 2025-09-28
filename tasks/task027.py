# https://www.codewars.com/kata/562926c855ca9fdc4800005b/train/python

def number_to_pwr(number: int, power: int)-> int:
    if power == 0:
        return 1

    powered_num = number

    while power != 1:
        powered_num *= number
        power -= 1

    return powered_num
