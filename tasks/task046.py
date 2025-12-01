# https://www.codewars.com/kata/5a905c2157c562994900009d/train/python
from typing import List


def product_array(numbers: List[int]) -> List[int]:
    product: List[int] = []
    
    for idx_i in range(0, len(numbers)):
        product_all: int = 1
        for idx_j in range(0, len(numbers)):
            if idx_i != idx_j:
                product_all = product_all * numbers[idx_j]
        product.append(product_all)        
                
    return product
