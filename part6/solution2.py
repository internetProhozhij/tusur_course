"""
2. Max-min

Дано: 
    массив чисел (float или/и int).

Задание: 
    нужно найти разницу между самым большим (максимум) и самым малым (минимум)
    элементом. Если список пуст, то результат равен 0 (ноль).

    Числа с плавающей точкой представлены в компьютерах как двоичная дробь. 
    Результат проверяется с точностью до третьего знака, как ±0.001

Пример:
    elements = [1, 2, 3], результат: 2
    elements = [5, -5], результат: 30
    elements = [10.2, -2.2, 0, 1.1, 0.5], результат: 12.4
    elements = [] , результат: 0
"""


def solution(numbers: list) -> float:
    if numbers == []:
        return 0

    max_number = max(numbers)
    min_number = min(numbers)
    return round(max_number - min_number, 3)


if __name__ == "__main__":
    test_data = [10.2, -2.2, 0, 1.1, 0.5]
    result = solution(test_data)

    print(result)