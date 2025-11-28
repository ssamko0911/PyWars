#https://www.codewars.com/kata/57096af70dad013aa200007b/train/python

def logical_calc(array: list[bool], op: str) -> bool:
    if not array:
        return False
    
    result: bool = array[0]
    
    for item in array[1:]:
        match op:
            case 'AND':
                result = result and item
            case 'OR':
                result = result or item
            case 'XOR':
                result = result ^ item
    
    return result
