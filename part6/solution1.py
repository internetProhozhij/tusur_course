"""
1. Последний с четными

Дано: 
    список (list) целых чисел (int).

Задание: 
    нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
    затем перемножить эту сумму и последний элемент исходного массива.

Пример:
    elements = [0, 1, 2, 3, 4, 5], результат: 30
    elements = [1, 3, 5], результат: 30
    elements = [] , результат: 0
"""


def solution(numbers: list[int]) -> int:
    answer = 0
    if numbers == []:
        return answer

    for index in range(0, len(numbers), 2):
        answer += numbers[index]
    
    return answer * numbers[len(numbers) - 1]


if __name__ == "__main__":
    test_data = [0, 1, 2, 3, 4, 5]
    result = solution(test_data)

    print(result)