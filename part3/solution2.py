"""
2. Python art

Дано: 
    маркер (символ) и толщина фигуры.

Задание: 
    написать программу, которая будет отображать заданную фигуру.

Пример: 
    Маркер = H, толщина 5.

Код:
    thickness = 5
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).______(thickness-1) + c + (c*i).______(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print(
            (c*thickness).______(thickness*2) + 
            (c*thickness).______(thickness*6)
        )

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).______(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print(
            (c*thickness).______(thickness*2) + 
            (c*thickness).______(thickness*6)
        )    

    #Bottom Cone
    for i in range(thickness):
        print(
            (
                (c*(thickness-i-1)).______(thickness) + c + 
                (c*(thickness-i-1)).______(thickness)
            ).______(thickness*6)
        )  
"""


def solution(thickness: int, c: str) -> None:

    #Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    #Top Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2) +
            (c * thickness).center(thickness * 6)
        )

    #Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5 ).center(thickness * 6))    

    #Bottom Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2) + 
            (c * thickness).center(thickness * 6)
        )    

    #Bottom Cone
    for i in range(thickness):
        print(
            (
                (c * (thickness - i - 1)).rjust(thickness) + c + 
                (c * (thickness - i - 1)).ljust(thickness)
            ).rjust(thickness * 6)
        )  


if __name__ == "__main__":
    thickness = 5
    c = 'H'
    
    solution(thickness, c)
    