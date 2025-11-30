# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python
from typing import List


def min_sum(arr: List[int]) -> int:
    arr.sort()
    idx: int = 0
    minSum: int = 0
        
    while idx != len(arr)/2:
        minSum += arr[idx] * arr[len(arr)-1-idx]
        idx += 1
    
    return minSum
