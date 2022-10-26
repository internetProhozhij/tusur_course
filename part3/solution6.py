"""
6. Произведение цифр

Дано: целое число.
 
Задание: 
    написать программу, которая перемножит все цифры заданного
    числа (0 - исключить).
 
 
Примеры: 
    1) value = 123405, результат = 120
    2) value = 999, результат = 729
    3) value = 1000, результат = 1
    4) value = 1111, результат = 1
"""


def solution(number) -> int:
    step = 10
    answer = 1

    while number > 0:
        digit = number % 10
        if digit != 0:
            answer *= digit
        number //= step

    return answer 


if __name__ == "__main__":
    number = 999
    answer = solution(number)
    print(answer)
