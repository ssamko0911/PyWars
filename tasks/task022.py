# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

def alias_gen(f_name: str, l_name: str) -> str:
    f_letter_name = f_name[0]
    l_letter_name = l_name[0]

    if not f_letter_name.isalpha() or not l_letter_name.isalpha():
        return 'Your name must start with a letter from A - Z.'

    uc_f_letter_name = f_letter_name.upper()
    uc_l_letter_name = l_letter_name.upper()

    return f'{FIRST_NAME[uc_f_letter_name]} {SURNAME[uc_l_letter_name]}'
