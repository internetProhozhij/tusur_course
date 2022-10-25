"""
2. Деление и еще раз деление

Дано: 
    2 случайных числа.

Задание: 
    написать программу, которая будет печать результат целочисленного 
    деления этих чисел, а также остаток от деления первого от второго.

Пример:
    x = 177 и y = 10

Результат:
    17, 7
"""


from random import randint


def solution(devisable: float, devider: float) -> list:       
    base = devisable // devider
    extra = devisable % devider
    
    return [base, extra]


if __name__ == "__main__":
    x, y = (randint(1, 100) for _ in range(2))
    print(f"{x=}\n{y=}")

    answer = solution(x, y)
    print(f"целая часть = {answer[0]}\nостаток = {answer[1]}")
