# Определяем функцию
def module(n:int|str|float) -> float|str:
    """
    Функция, находящая модуль числа.
    """    
    # Обрабатываем входные данные
    try:
        n = float(n)
    except:
        return "Введено некрректное значение!"
    # Находим модуль
    if n < 0:
        n = n *-1
    # Возвращщаем результат
    return n
# Точка входа
if __name__ == "__main__":
    print(module(-90))