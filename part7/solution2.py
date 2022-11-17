"""
2. Римские цифры

Дано: 
    целое число (int).

Задание: 
    Римские цифры пришли к нам из древней римской системы счета. 
    Они основаны на особых буквах алфавита, которые в различных сочетаниях,
    путем суммирования (а иногда и разницы) описывают различные числа. 
    
    Первые 10 римских чисел это:
        I, II, III, IV, V, VI, VII, VIII, IX, and X.

    Римская система счета имеет десятичное основание, но она непозиционная и
    не включает в себя 0 (ноль). Римские числа образуются путем комбинации 
    следующих семи символов:

        Символ Значение 
        I 1 (unus) 
        V 5 (quinque) 
        X 10 (decem) 
        L 50 (quinquaginta) 
        C 100 (centum) 
        D 500 (quingenti) 
        M 1,000 (mille)

    В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999)
    в римскую систему счета.

Пример:
    x = 6, результат: 'VI'
    x = 76, результат: 'LXXVI'
    x = 13, результат: 'XIII'
    x = 44, результат: 'XLIV'
    x = 3999, результат: 'MMMCMXCIX'
"""


from collections import OrderedDict

def solution(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(
            f"number должен быть типа int (был передан {type(number)})"
        )

    if number < 1 or number > 3_999:
        raise ValueError(
            f"number - число из отрезка [1, 3999] (был передан {number})"
        )

    mapper = OrderedDict({
        1_000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    })

    roman_number = ""
    while number:
        for normal_number in mapper.keys():
            while number >= normal_number:
                roman_number += mapper[normal_number]
                number -= normal_number

    return roman_number


if __name__ == "__main__":
    user_input = input("Введите число: ")

    try:
        number = int(user_input)
        answer = solution(number)
        print(answer)
    except Exception as excp:
        print(excp)
