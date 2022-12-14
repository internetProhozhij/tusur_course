"""
5. Дизайнер ковриков

Дизайнер составил шаблон домашних ковриков. Для массового выпуска 
ковриков ему нужно уметь быстро составлять макет произвольного 
размера. 

Известно, что длина коврика всегда больше в 3 раза чем его ширина.

Дано: 
    ширина коврика.

Задание: 
    написать программу, которая будет составлять макет коврика для 
    его дальнейшего производства.

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""


def solution(height: int) -> None:
    width = height * 3
    
    marker = ".|."

    line = ""
    for line_index in range(1, height, 2):
        line += marker * line_index
        print(line.center(width, "-"))
        line = ""

    print("WELCOME".center(width, "-"))

    for line_index in range(height, 1, -2):
        line += marker * (line_index - 2)
        print(line.center(width, "-"))
        line = ""


if __name__ == "__main__":
    solution(13)
