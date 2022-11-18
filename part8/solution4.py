"""
4. Дешифратор.

Дано: 
    шифровальная решетка (4 на 4) и зашифрованный пароль (4 на 4) представлены,
    как массив строк.

Задание. 
    Помогите Софи написать дешифратор для паролей, которые Никола зашифровал с
    помощью шифровальной решетки. Шифрорешетка - это квадрат 4 на 4 с четырьмя 
    вырезанными окошками. Поместите решетку на листе бумаги такого же размера с
    буквами, выписываете первые 4 символа, которые видно в окошках (см. рисунок). 
    
    Затем поверните решетку на 90 градусов по часовой стрелке. Выпишите следующие 
    символы и повторите поворот. В итоге процедура повторяется 4 раза. Таким образом 
    сложно узнать пароль без специальной решетки.

    Напишите программу, которая поможет проводить данную процедуру.

Пример:
    (("X...",
      "..X.",
      "X..X",
      "...."),
     ("itdf",
      "gdce",
      "aton",
      "qrdi"), результат: "icantforgetiddqd"

    (("....",
      "X..X",
      ".X..",
      "...X"),
     ("xhwc",
      "rsqx",
      "xqzz",
      "fyzr")), результат: "rxqrwsfzxqxzhczy"
"""


def rotate(matrix: list) -> list:
    """Поворот матрицы по часовой стрелке.
    """
    lines = len(matrix)
    rows = len(matrix[0])
    rotated_matrix = [
        [matrix[j][i] for j in range(rows-1, -1, -1)]
        for i in range(lines)
    ]
    
    return rotated_matrix


def solution(text: tuple[str], grid: tuple[str], marker: str="X") -> str:
    """Расшифрование сообщения.

    Параметры
    ---------
    text : tuple[str]
        Зашифрованное сообщение (размерность 4x4).
    grid : tuple[str]
        Шифровальная решетка (размерность 4x4).
    marker : str, default="X"
        Маркер для обозначения окошек в решетке.

    Результат
    ----------
    Расшифрованное сообщение.
    """
    LINES, ROWS = 4, 4

    if (
        any(len(line) != ROWS for line in grid)
        or any(len(line) != ROWS for line in text)
    ):
        raise IndexError(f"Длины строк grid и text должны равняться {ROWS}")

    if len(grid) != LINES or len(text) != LINES:
        raise IndexError(
            "grid и text должны быть представлены квадратными матрицами"
        )
        
    grid_cpoy = list(grid)

    decrypted_text = ""
    for iteration in range(4):
        for grid_line, text_line in zip(grid_cpoy, text):
            decrypted_text += "".join(
                char 
                for char, current_marker 
                in zip(text_line, grid_line)
                if current_marker == marker
            )

        grid_cpoy = rotate(grid_cpoy)

    return decrypted_text


if __name__ == "__main__":
    # ВАЖНО: Сначала идет текст, потом маска
    bundle = (
        ("itdf", "gdce", "aton", "qrdi"),
        ("X...", "..X.", "X..X", "....")
    )

    # bundle = (
    #     ("xhwc", "rsqx", "xqzz", "fyzr"),
    #     ("....", "X..X", ".X..", "...X")
    # )

    answer = solution(*bundle)
    print(answer)
