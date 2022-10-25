"""
3. Заголовок

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


def solution(text: str) -> str:
    return text.title()


if __name__ == "__main__":
    text = "hello world"
    title = solution(text)

    print(title)
