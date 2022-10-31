"""
2. Оценка числа

Дано: 
    число x.

Задание: 
    нужно написать программу, которая дает оценку заданному значению,
    используя следующие правила.
        если x нечетное, то это "Плохо"
        если x = [2, 5] и четное, то это "Неплохо"
        если x = [6, 20] и четное, то это "Так себе"
        если x > 20 и четное, то это "Отлично"
"""


def solution(number: int) -> str:
    if number % 2 != 0:
        return "Плохо"

    if 2 <= number <= 5: 
        return "Неплохо"

    if 6 <= number <= 20:
        return "Так себе"

    if number % 2 == 0 and number > 20:
        return "Отлично"

    return "Не определено"


if __name__ == "__main__":
    user_input: str = input("Введите целое число: ")

    try:
        number = int(user_input)
        result = solution(int(user_input))
        print(result)
    except Exception as exp:
        print(exp)
