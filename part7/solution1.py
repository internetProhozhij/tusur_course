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


def solution(text: str) -> tuple[dict[str:int]]:
    chars_popularity = {}
    words_popularity = {}
    
    words = text.split(sep=" ")

    for word in words:
        # обновление популярности слова
        if word not in words_popularity.keys():
            words_popularity[word] = 1
        else:
            words_popularity[word] += 1

        # обновление популярности букв
        for char in word:
            if char not in chars_popularity.keys():
                chars_popularity[char] = 1
            else:
                chars_popularity[char] += 1

    return (chars_popularity, words_popularity)


if __name__ == "__main__":
    user_input = input("Введите текст: ")
    chars_popularity, words_popularity = solution(user_input)

    print(f"{chars_popularity=}\n")
    print(f"{words_popularity=}")
