"""
6. Мир захватили левши

"На протяжении веков, левши страдали от дискриминации в мире, 
созданном для правшей." 
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и 
неопределеное число людей вероятно лучше всего охарактеризовать, 
как "симметричные". 
Scientific American. www.scientificamerican.com

Один робот был занят простой задачей: объединить последовательность строк
в одно выражение для создания инструкции по обходу корабля. Но робот был 
левша и зачастую шутил и запутывал своих друзей правшей.

Дано: 
    последовательность строк.

Задание: 
    вы должны объединить эти строки в блок текста, разделив изначальные 
    строки запятыми. В качестве шутки над праворукими роботами, вы должны
    заменить все вхождения слова "right" на слова "left", даже если это 
    часть другого слова. Все строки даны в нижнем регистре.

Примеры:
    ["left", "right", "left", "stop"], результат: "left,left,left,stop"
    ["bright aright", "ok"], результат: "bleft aleft,ok"
    ["enough", "jokes"], результат: "enough,jokes"
"""


def solution(words: list[str]) -> list[str]:
    target = "right"
    joke = "left"

    jokes = [word.replace(target, joke) for word in words]
    
    output = ""
    for index, joke in enumerate(jokes):
        output += joke
        if index != len(jokes) - 1:
            output += "," 

    return output


if __name__ == "__main__":
    test_data = ["bright aright", "ok"]
    result = solution(test_data)
    print(result)