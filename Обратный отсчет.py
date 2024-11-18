# Создаем функцию
def recursion(n:int) -> int:
    """
    Функция для обратного отсчета.
    """
    print(n)
    if n == 1:
        return 1
    return recursion(n-1)
# Точка входа
if __name__ == "__main__":
    recursion(int(input('Введите число: ')))