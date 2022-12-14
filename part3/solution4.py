"""
4. Форматированный вывод денежной суммы

Дано: 
    денежная сумма (amount > 0).

Задание: 
    написать программу, которая распечатает число в принятом 
    денежном формате XXX,XXX.XX.

Пример: 
    amount = 100500.157

Результат:
    100,500.16
"""


def solution(amount: float) -> str:
    return f"{amount:,.2f}"


if __name__ == "__main__":
    amount = 100500.157
    answer = solution(amount)

    print(answer)
