# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

hex_numbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hex_to_dec(hex_num):
    base = 16
    decimal_num = 0
    hex_len = len(hex_num)

    for ch in hex_num:
        if ch not in hex_numbers:
            return None

    for index, ch in enumerate(hex_num):
        decimal_num += hex_numbers[ch] * (base ** (hex_len - index - 1))

    return decimal_num
