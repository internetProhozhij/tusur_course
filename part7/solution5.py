"""
5. Структурируем данные

Дано: 
    2 списка с измерениями(list).

Задание. 
    Ученый-спекулянт анализировал курс доллара и собрал 2 списка: 
        один с датами (dates), 
        другой с курсами валют (rates). 
    Он знает, что эти списки имеют одинаковую длину, а также что 
    i-ый курс из списка rates соотвествует i-ой дате из списка dates. 
    
    Друзья ученого, зная о его исследовании, часто просят его предоставить 
    значение курса валюты на определенную дату. Так как ученый-спекулянт 
    изучает Python, то решил составить словарь, что позволит ему быстро 
    получать такую информацию.

    Формально нужно получить словарь из 2х списков, где в первом находятся ключи, 
    а во втором значения.

Пример:
    dates = ['2017-03-01', '2017-03-02'], rates = [55.7, 55.2], 
    результат: {'2017-03-01': 55.7, '2017-03-02': 55.2}
"""


def solution(dates: list[str], rates: list[float]) -> dict[str, float]:
    if not dates or not rates:
        raise ValueError(
            "dates и rates должны содержать хотя бы 1 элемент"
            f" (были переданы {dates=}   {rates=}))"
        )

    return dict(list(zip(dates, rates)))


if __name__ == "__main__":
    dates = ['2017-03-01', '2017-03-02']
    rates = [55.7, 55.2]

    answer = solution(dates, rates)
    print(answer)