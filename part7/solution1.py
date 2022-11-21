"""
1. Анализ текста. Популярность.

Дано: 
    текст (str).

Задание: 
    необходимо получить 2 словаря (популярности слов и популярности букв).

Пример:
    text = "hello, word of word", результат: 
    
    chars_popularity = {'h': 1, 'e': 1, 'l': 2, ..};
    words_popularity = {'hello': 1, 'word': 2, 'of': 1}
"""


import re, string
                

def solution(text: str) -> tuple[dict[str:int]]:
    """Поиск популярности букв и слов.

    Результат
    ---------
    Кортеж словарей
        Первый словарь кортежа содержит популярность букв, втрой -
        популярность слов.

    Примечание
    ----------
    Так как в задании не сказано, какая последовательность символов является
    словом, то был использован следующий подход:
    - словом считается последовательность алфавитных символов, в которой могут
        присутствовать числа, то есть последовательности "hello", "день", "T-24" 
        будут являться словами.
    - буквой является только алфавитный символ, то есть в слове "hello" 5 букв, а
        в слове "T-24" только 1 буква.

    ***
    Текущая реализация функция не умеет в правильную обработку смайликов, 
    содержащих буквы, например, "B-)". В этом случае входная последовательность 
    превратиться в "В" и будет обработана как слово из одной буквы.
    ***
    """
    chars_popularity = {}
    words_popularity = {}
    
    trash_symbols = string.punctuation

    # Замена тире на пробел
    text_to_lowercase = text.lower().replace(" - ", " ")

    for char in trash_symbols:
        # Пропускается символ "-", так как теперь он используется 
        # в качестве дефиса, то есть является частью слова.
        if char == "-":
            continue

        text_to_lowercase = text_to_lowercase.replace(char, " ")

    words = text_to_lowercase.split()
    for word in words:
        if not word or word.isdecimal():
            continue

        if word not in words_popularity.keys():
            words_popularity[word] = 1
        else:
            words_popularity[word] += 1

        for char in word:
            if char.isdecimal() or char == "-":
                continue

            if char not in chars_popularity:
                chars_popularity[char] = 1
            else:
                chars_popularity[char] += 1

    return (chars_popularity, words_popularity)
    

if __name__ == "__main__":
    user_input = input("Введите текст: ")
    
    chars_popularity, words_popularity = solution(user_input)
    print(f"{chars_popularity=}\n{words_popularity=}")
