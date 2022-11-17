"""
5. Полосатые слова

Дано: 
    текст, как строка (str).

Задание: 
    Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в
    лингвистике. Сейчас они изучают английский алфавит и что с этим делать.

    Алфавит разделен на гласные и согласные буквы (да, мы разделили буквы, а не звуки).

    Гласные -- A E I O U Y
    Согласные -- B C D F G H J K L M N P Q R S T V W X Z

    Дан текст с разными словами и/или числами, которые разделены пробелами и знаками 
    пунктуации. Числа не считаются за слова (также как и смесь букв и цифр). 
    Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными 
    (полосатые слова), то есть в таких словах нет двух гласных или двух согласных букв
    подряд. Слова состоящие из одной буквы - не "полосатые" (не считайте их). Регистр 
    букв не имеет значения.

Пример:
    text = "My name is ...", результат: 3
    text = "Hello world", результат: 0
    text = "A quantity of striped words.", результат: 1
    text = "Dog,cat,mouse,bird.Human.", результат: 3
"""


def solution(text: str) -> int:
    if not text:
        return -1

    VOWELS = "aeiouy"
    CONSONANS = "bcdfghjklmnpqrstvwxz"
    ALPHABET = VOWELS.join(CONSONANS)
    MARKS = [",", ".", "!", "?", "-", ":", ";"]
    
    normalized_text = text.lower()
    for mark in MARKS:
        normalized_text = normalized_text.replace(mark, " ")

    words = normalized_text.split()

    count = 0
    for word in words:
        if len(word) == 1 or any(letter not in ALPHABET for letter in word):
            continue
        
        even_index_chars = ""
        odd_index_chars = ""

        for index, char in enumerate(word):
            if index % 2 == 0:
                even_index_chars += char
            else:
                odd_index_chars += char
        
        if (
            all(char in VOWELS for char in even_index_chars) 
            and all(char in CONSONANS for char in odd_index_chars)
            or all(char in VOWELS for char in odd_index_chars) 
            and all(char in CONSONANS for char in even_index_chars)
        ):
            count += 1

    return count


if __name__ == "__main__":
    user_input = input("Введите текст: ")

    answer = solution(user_input)
    print(answer)