"""
3. Ленивый спекулянт

Дано: 
    словарь банк - курс доллара (dict).

Задание: 
    определить банк и курс покупки валюты с наиболее привлекательным предложением.

Пример:
    rates = {'Sberbank': 55.8, 'VTB24': 53.91}, результат: VTB24 -> 53.91 
"""


def solution(rates: dict[str, float]) -> str:
    target = min(rates.items(), key=lambda pair: pair[1])

    return f"{target[0]} -> {target[1]}"
    

if __name__ == "__main__":
    rates = {
        "СБЕР": 55.8,
        "ВТБ": 53.91,
        "Альфа": 47.57,
    }

    answer = solution(rates)
    print(answer)