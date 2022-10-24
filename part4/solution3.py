"""
3. Округление

Дано: 
    число с плавающей точкой.

Задание: 
    написать программу, которая будет округлять заданное число:
        1) 2х знаков после запятой; 
        2) до целого; 
        3) дополнять слева столько нулей, сколько не хватает 
            числу до 11 знаков.

Пример:
    x = 14.721
        1) 14.72
        2) 15
        3) 0000014.721
"""


def solution(number: float) -> list[str]:
    number1 = str(round(number=number, ndigits=2))
    number2 = str(round(number=number))
    number3 = f"{number:011}"
    
    return [number1, number2, number3]


if __name__ == "__main__":
    a = 14.721
    answer = solution(a)

    for result in answer:
        print(result)