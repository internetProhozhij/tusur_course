"""
1. Среднее

Дано: 
    3 случайных числа.

Задание: 
    написать программу, которая будет вычислять среднее значение 
    этих чисел.

Пример: 
    (52 + 56 + 60) / 3 = 56
"""


from random import randint


def solution(number1: float, number2: float, number3: float) -> float:
    return (number1 + number2 + number3) / 3


if __name__ == "__main__":
    a, b, c = (randint(0, 100) for _ in range(3))
    print(f"n1 = {a}\nn2 = {b}\nn3 = {c}")

    answer = solution(a, b, c)
    print(f"Среднее арифметическое = {answer}")
