"""
5. Три слова

Давайте научим наших роботов отличать слова от чисел.
Дана строка со словами и числами, разделенными пробелами 
(один пробел между словами и/или числами). 
Слова состоят только из букв.

Дано: 
    cтрока со словами (str).

Задание: 
    напишите программу, которая проверяет есть ли в исходной строке три
    слова подряд. 
    Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

Примеры:
    text = "Hello World hello", результат: True
    text = "He is 123 man", результат: False
    text = "1 2 3 4", результат: False
"""


def solution(text: str) -> bool:
    words = text.split(sep=" ")
    sequence_length = 0

    for word in words:
        is_valid = all(
            element == False for element
            in (letter.isdecimal() for letter in word)
        )
        if is_valid:
            sequence_length += 1
        else:
            sequence_length = 0

        if sequence_length == 3:
            return True
    
    return False


if __name__ == "__main__":
    user_input = input("Введите предложение: ")
    result = solution(user_input)
    print(result)
