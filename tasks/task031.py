# https://www.codewars.com/kata/592e830e043b99888600002d/train/python
import string

def encode(message: str, key: int) -> list:
    keys = string.ascii_letters
    values = list(range(1, 27))

    cypher_dict = dict(zip(keys, values))

    encoded = []
    key_as_str = str(key)

    for idx, char in enumerate(message):
        num = cypher_dict.get(char)
        num += int(key_as_str[idx % len(key_as_str)])
        encoded.append(num)

    return encoded
