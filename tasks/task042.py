#https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python


def update_longest(temp_counter: int, longest_vowel_sequence: int) -> int:
    if temp_counter > longest_vowel_sequence:
        return temp_counter
        
    return longest_vowel_sequence

def solve(word: str) -> int:
    longest_vowel_sequence: int = 0
    temp_counter: int = 0
    
    for letter in word:
        if letter in 'aeiou':
            is_vowel = True
        else:
            is_vowel = False
            
        if is_vowel:
            temp_counter += 1
        else:
            longest_vowel_sequence = update_longest(temp_counter, longest_vowel_sequence)
            temp_counter = 0

    if temp_counter != 0:
        longest_vowel_sequence = update_longest(temp_counter, longest_vowel_sequence)
            
    return longest_vowel_sequence