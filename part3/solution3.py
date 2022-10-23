"""
Дано: 
    текст любой длины.

Задание: 
    написать программу, которая выведет заголовок, используя заданный
    текст. Подсказка используйте метод title.

Пример: 
    text = 'hello world'; 
    
Результат:
    Hello World
"""


def solution() -> None:
    text = "hello, world"
    print(text.title())


if __name__ == "__main__":
    solution()
