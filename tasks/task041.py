#https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python
from typing import List


def small_enough(array: List[int], limit: int) -> bool:
    for num in array:
        if not num <= limit:
            return False
    
    return True    
