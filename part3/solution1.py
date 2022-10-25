"""
1. Welcome to Python

Дано:
    имя и фамилия.

Задание: 
    написать программу, которая будет приветствовать нового 
    человека в мире Python. 
    Текст приветсвия: 
        Hello NAME SURNAME! You just delved into Python. Great start!

Пример: 
    Hello Ibrahim Petrov! You just delved into Python. Great start!
"""


def solution(name: str, surname: str) -> None:
    print(
        f"Hello, {name} {surname}! You just delved into Python. Great Start!"
    )


if __name__ == "__main__":
    name = "Ibrahim"
    surname = "Petrov"

    solution(name, surname)
