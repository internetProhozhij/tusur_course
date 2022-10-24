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
"""


def solution():
    height = 11
    width = height * 3

    tree_segment1 = int(height * 0.25)
    tree_segment2 = int(height * 0.45)

    print("<>" + "=" * (width - 4) + "<>")

    if height % 2 != 0:
        for line_index in range(1, tree_segment1 + 1):
            print(
                "||" + 
                ("/" + "#" * (line_index - 1)).rjust(width // 2 - 2, "-") +
                "#" +
                ("#" * (line_index - 1) + "\\").ljust(width // 2 - 2, "-") +
                "||"
            )

        print("||" + "|||".center(width - 4, "-") + "||")

        for line_index in range(1, tree_segment2 + 1):
            print(
                "||" +
                ("/" + "#" * (line_index + 2)).rjust(width // 2 - 2, "-") +
                "#" +
                ("#" * (line_index + 2) + "\\").ljust(width // 2 - 2, "-") +
                "||"
            )

        for line_index in range(2):
            print("||" + "|||".center(width - 4, "-") + "||")
    else:
        for line_index in range(1, tree_segment1 + 1):
            print(
                "||" + 
                ("/" + "#" * (line_index - 1)).rjust(width // 2 - 2, "-") +
                ("#" * (line_index - 1) + "\\").ljust(width // 2 - 2, "-") +
                "||"
            )

        print("||" + "||".center(width - 4, "-") + "||")

        for line_index in range(1, tree_segment2 + 1):
            print(
                "||" +
                ("/" + "#" * (line_index + 2)).rjust(width // 2 - 2, "-") +
                ("#" * (line_index + 2) + "\\").ljust(width // 2 - 2, "-") +
                "||"
            )

        for line_index in range(2):
            print("||" + "||".center(width - 4, "-") + "||")

    print("<>" + "=" * (width - 4) + "<>")


if __name__ == "__main__":
    solution()
