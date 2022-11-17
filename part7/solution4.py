"""
4. Вверх дном

Дано: 
    словарь ФИО - номер телефона(dict).

Задание: 
    получить новый словарь, инвертировав исходный, т.е. пары ключ - значение
    поменять местами (значение - ключ).

Пример:
    book = {'Petr': '546810', 'Katya': '241815'}, 
    результат: {'546810': 'Petr', '241815': 'Katya'}
"""


def solution(object: dict[str, str]) -> dict[str, str]:
    keys = list(object.keys())
    values = list(object.values())

    return dict(list(zip(values, keys)))


if __name__ == "__main__":
    book = {'Petr': '546810', 'Katya': '241815'}

    answer = solution(book)
    print(answer)