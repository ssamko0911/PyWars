# https://www.codewars.com/kata/58daa7617332e59593000006/train/python

def find_longest(arr):
    length = 0
    longest = arr[0]

    for item in arr:
        temp_length = len(str(item))
        if temp_length > length:
            length = temp_length
            longest = item

    return longest
