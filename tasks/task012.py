# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python

class Operator(object):
    ADD = 'add'
    SUB = 'subtract'
    DIV = 'divide'
    MUL = 'multiply'

def arithmetic(a, b, operator):
    match operator:
        case Operator.ADD:
            return a + b
        case Operator.SUB:
            return a - b
        case Operator.DIV:
            return a / b
        case Operator.MUL:
            return a * b
    return None
