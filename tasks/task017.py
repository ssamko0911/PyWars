# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

def max_rot(n):
    values = [n]
    num_len = len(str(n))

    for i in range(0, num_len):
        values.append(custom_slice(str(values[len(values) - 1]), i))

    return max(values)

def custom_slice(number_as_string, slice_index):
    non_rot_part = number_as_string[:slice_index]
    rot_part = number_as_string[slice_index:]

    return int(non_rot_part + rot_part[1:] + rot_part[:1])
