"""
5. Число "наоборот" (усложненное)

Дано:
    целое число (int).
 
Задание:
    написать программу, которая будет инвертировать целое число. 
    Если инвертированное число выходит за границы (32-bit integer)
     
Пример:
    1) x = 123 -> 321
    2) x = -325 -> -523
    3) x = 0 -> 0
    4) x = 1563847412 -> 0
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

    if reversed_number > 2 ** 31 - 1 and not negative:
        return 0
    
    if reversed_number > 2 ** 31 and negative:
        return 0

    if negative:
        reversed_number *= -1
    
    return reversed_number
    

if __name__ == "__main__":
    number = -9463847412
    print(solution(number))