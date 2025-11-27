#https://www.codewars.com/kata/51f41b98e8f176e70d0002a8/train/python
from typing import List


# input: names - unsorted list
# output: sorted list
def sortme(names: List[str]) -> List[str]:
    temp: str
    length: int 
    
    for idx_i, name in enumerate(names):
        for idx_j, next_name in enumerate(names):
            if names[idx_i] > names[idx_j]:
                temp = names[idx_i]
                names[idx_i] = names[idx_j]
                names[idx_j] = temp
        
    return names