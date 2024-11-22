# Создаем функцию
def rects_S_and_P(a:int|float|str, b:int|float|str) -> str|str:
    """
    Функция для нахождения площади и периметра прямоугольника.
    """
    # Обрабатываем входные даннные
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Введено некорректное значение!"
    # Расчитаем периметр
    p = (a+b) * 2
    # Расчитаем площадь
    s = a * b
    # Возвращаем данные
    return f"Периметр: {p}\nПлощадь: {s}"
# Точка входа
if __name__ == "__main__":
    print(rects_S_and_P(10, "75"))