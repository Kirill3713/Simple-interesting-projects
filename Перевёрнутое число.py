# Создаем функцию
def turn_num_over(n:int) -> int:
    """
    Функция, переворачивающая натуральные числа.
    """    
    try:
        n = int(n)
    except ValueError:
        return "Можно вводить только натуральные числа."
    # Переворачиваем его
    result = 0
    while n > 0:
        d = n % 10
        result = result * 10 + d
        n = n // 10
    # Выводим результат
    return result
# Точка входа
if __name__ == "__main__":
    print(turn_num_over(3))