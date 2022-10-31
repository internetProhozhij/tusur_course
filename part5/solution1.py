"""
1. Fizz Buzz

Дано: 
    число, как целочисленное (int).

Задание:
    "Fizz buzz" это игра со словами, с помощью которой мы будем учить
    наших роботов делению. Давайте обучим компьютер.

    Вы должны написать программу, которая принимает положительное целое
    число и возвращает сл. значения.
        "Fizz Buzz", если число делится на 3 и 5;
        "Fizz", если число делится на 3;
        "Buzz", если число делится на 5;

        Число, как строку для остальных случаев.
"""


def solution(number: int) -> str:
    if number % 3 == 0: 
        if number % 5 == 0:
            return "Fizz Buzz"
        return "Buzz"
    
    if number % 5 == 0:
        return "Fizz"

    return str(number)


if __name__ == "__main__":
    user_input: str = input("Введите целое число: ")

    try:
        number = int(user_input)
        result = solution(int(user_input))
        print(result)
    except Exception as exp:
        print(exp)
