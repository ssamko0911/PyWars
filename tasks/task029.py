# https://www.codewars.com/kata/5a512f6a80eba857280000fc/train/python

def nth_smallest(array: list, pos: int) -> int:
    array.sort()

    return array[pos - 1]
