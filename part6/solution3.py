"""
3. Умная сортировка

Дано: 
    кортеж (tuple) чисел.

Задание: 
    необходимо отсортировать их, но отсортировать на основе абсолютных 
    значений в возрастающем порядке. Для примера, последовательность 
    (-20, -5, 10, 15) будет отсортирована следующим образом 
    (-5, 10, 15, -20). 
    Ваша функция должна возвращать список (list) или кортеж (tuple).

Пример:
    elements = (-20, -5, 10, 15), результат: [-5, 10, 15, -20]
    elements = (1, 2, 3, 0), результат: [0, 1, 2, 3]
    elements = (-1, -2, -3, 0), результат: [0, -1, -2, -3]
"""


def solution(numbers: tuple) -> list:
    numbers_list = list(numbers)
    result = sorted(numbers_list, key=lambda number: abs(number))
    return result


if __name__ == "__main__":
    test_data = (-1, -2, -3, 0)
    result = solution(test_data)

    print(result)