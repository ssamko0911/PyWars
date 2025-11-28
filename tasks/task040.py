# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
from typing import List


def check_exam(correct_answers: List[str], student_answers: List[str]) -> int:
    score: int = 0

    for idx, correct_answer in enumerate(correct_answers):
        if student_answers[idx] == '':
            pass
        elif correct_answer == student_answers[idx]:
            score += 4
        elif correct_answer != student_answers[idx]:
            score -= 1

    return 0 if score < 0 else score
