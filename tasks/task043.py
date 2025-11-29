# https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python
from typing import List


def remove(integer_list: List[int], values_list: List[int]) -> List[int]:
    return [number for number in integer_list if number not in values_list]
