# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
green = colorama.Fore.GREEN
light_green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
light_cyan = colorama.Fore.LIGHTCYAN_EX
light_white = colorama.Fore.LIGHTWHITE_EX
# Создаем функцию
def multiply_range(start: int|float|str, end: int|float|str) -> int|str:
    """
    Функция для умножения всех целых чисел заданного диапазона.
    """
    # Объявляем переменные
    result = 1
    try:
        start = int(start)
        end = int(end)
    # Добавляем исключение, на случай неправильного ввода
    except ValueError:
        return red + "Введено некорректное значение!"  + reset
    # Умножаем все числа от end до start, если end меньше start
    if start > end:
        for i in range(end, start + 1):
            result *= i
    # и от start до end, если все хорошо
    else:
        for i in range(start, end + 1):
            result *= i
    # Возвращаем результат
    return result
# Точка входа
if __name__ == "__main__":
    # Объявляем глобальную переменную result и записываем в нее результат multiply_range с заданными числами
    result = multiply_range(input(light_green + "Введите начальное число: " + cyan), input(light_green + "Введите конечное число: " + light_cyan))
    # Выводим результат
    print(light_white + "Результат:" + reset, result)