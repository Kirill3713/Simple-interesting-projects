# Создаем функцию
def recursion(n:int|float|str) -> int|str:
    """
    Функция для обратного отсчета.
    """
    try:
        try:
            n = int(n)
        except ValueError:
            print("Введено некорректное значение!")
            return
        print(n)
        if n == 1:
            return 1
        return recursion(n-1)
    except RecursionError:
        print("Введено некорректное значение")
# Точка входа
if __name__ == "__main__":
    recursion(input('Введите число: '))