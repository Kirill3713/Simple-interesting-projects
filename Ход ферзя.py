# Определяем функцию
def check_queens_move(x1:int|str, y1:int|str, x2:int|str, y2:int|str) -> bool|str:
    """
    Функция, проверяющая ход ферзя: возможен такой или нет.\n
    Первый параметр: буква или цифра по вертикали начального положения ферзя.\n
    Второй параметр: цифра по горизонтали начального положения ферзя.\n
    Третий параметр: буква или цифра по вертикали конечного положения ферзя.\n
    Четвертый параметр: цифра по горизонтали конечного положения ферзя.\n
    """
    # Если передаются буквенные координаты, то заменяем их на численные
    x_coords = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }
    if x1 in x_coords.keys():
        x1 = x_coords[x1]
    if x2 in x_coords.keys():
        x2 = x_coords[x2]
    # Переводим координаты начального и конечного положения ферзя в int
    try:
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
    except ValueError:
        return "Введено некорректное значение!"
    # Возвращаем True если ход возможен, и False если нет
    if x1 == x2:
        return True
    elif y1 == y2:
        return True
    elif x1 - x2 == y1 - y2:
        return True
    else:
        return False
# Точка входа
if __name__ == "__main__":
    print(check_queens_move(1, 1, 8, 8))
    print(check_queens_move("a", 1, "b", 3))
    print(check_queens_move("c", 7, "c", 1))
    print(check_queens_move(1, "b", 4, "h"))