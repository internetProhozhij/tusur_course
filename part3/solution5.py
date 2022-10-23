"""
Дизайнер составил шаблон домашних ковриков. Для массового выпуска 
ковриков ему нужно уметь быстро составлять макет произвольного 
размера. 

Известно, что длина коврика всегда больше в 3 раза чем его ширина.

Дано: 
    ширина коврика.

Задание: 
    написать программу, которая будет составлять макет коврика для 
    его дальнейшего производства.
"""


def solution():
    height = 11
    width = height * 3

    flag = True
    for line_index in range(height - 6):
        if line_index == 0:
            print("<>" + "=" * (width - 4) + "<>")
        elif line_index == height - 7:
            print("||".ljust(width // 2, "=") + "||".rjust(width // 2 + 1, "="))
        else:
            if line_index % 2 != 0:
                if flag:
                    print("||" + "<+" * ((width - 4) // 2) + "<||")
                    flag = False
                else:
                    print("||" + ">+" * ((width - 4) // 2) + ">||")
                    flag = True
            else:
                print("||" + "@|" * ((width - 4) // 3) + "||")


if __name__ == "__main__":
    solution()
