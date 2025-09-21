# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/python

def max_diff(lst):
    if 0 == len(lst):
        return 0

    min_val = lst[0]
    max_val = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
        if lst[i] > max_val:
            max_val = lst[i]

    return max_val - min_val

    #return max(lst) - min(lst)
