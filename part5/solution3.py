"""
3. Последовательность

Дано: 
    число N = [1-9].

Задание: 
    нужно написать программу, которая выведет последовательность 123..N

Пример:
    N = 3, результат: 123
    N = 9, результат: 123456789     
    N = 1, результат: 1
"""


def solution(number: int) -> str:
    if number > 9 or number < 1:
        raise ValueError("number должно принадлежать [1..9]")

    sequence = ""
    for number in range(1, number + 1):
        sequence += str(number)

    return sequence


if __name__ == "__main__":
    user_input: str = input("Введите число от 1 до 9: ")

    try:
        number = int(user_input)
        result = solution(int(number))
        print(result)
    except Exception as excp:
        print(excp)