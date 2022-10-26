"""
4. Число "наоборот"

Дано: 
    целое число (int).
 
Задание: 
    написать программу, которая будет инвертировать целое число
     
Пример:
    1) x = 123 -> 321
    2) x = -325 -> -523
    3) x = 0 -> 0
"""


def solution(number: int): 
    if -10 < number < 10:
        return number

    if number < 0:
        negative = True
        number *= -1
    else:
        negative = False

    reversed_number = 0
    while number:
        reversed_number = reversed_number * 10 + (number % 10)
        number //= 10

    if negative:
        reversed_number *= -1
    
    return reversed_number
    

if __name__ == "__main__":
    number = -312
    print(solution(number))