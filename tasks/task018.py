# https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python

def capitals_first(text):
    caps = []
    lowers = []

    for word in text.split():
        if word[0].isupper():
            caps.append(word)
        elif word[0].islower():
            lowers.append(word)
        else:
            pass

    return ' '.join(caps + lowers)
