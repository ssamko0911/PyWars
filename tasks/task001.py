#https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python

class Constraints:
    THRESHOLD_LEN = 2

def who_is_paying(name):
    name_len = name.__len__()

    if Constraints.THRESHOLD_LEN < name_len:
        return [name, name[0:Constraints.THRESHOLD_LEN]]
    elif Constraints.THRESHOLD_LEN >= name_len:
        return [name]
    else:
        return ['']
