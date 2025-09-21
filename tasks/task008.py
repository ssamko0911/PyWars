# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python

def sum_of_differences(arr):
    diff = 0
    arr.sort(reverse=True)

    for i in range(len(arr) - 1):
        if i + 1 != len(arr):
            diff += arr[i] - arr[i + 1]

    return diff
