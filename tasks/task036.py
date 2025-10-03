# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

def string_clean(text: str) -> str:
    cleaned_text = ''

    for char in text:
        if not char.isdigit():
            cleaned_text += char

    return cleaned_text
