# Импортируем нужные модули и создаем переменные цветов
import os
import colorama
cyan = colorama.Fore.CYAN
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
light_green = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
blue = colorama.Fore.BLUE
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
dark_red = colorama.Fore.RED
light_cyan = colorama.Fore.LIGHTCYAN_EX
light_white = colorama.Fore.LIGHTWHITE_EX
yellow = colorama.Fore.YELLOW
light_blue = colorama.Fore.LIGHTBLUE_EX
# Очищаем экран
os.system("cls")
# Создаем функции математических действий
# Деление
def divide_nums(a:int|float|str, b:int|float|str) -> None:    
    """
    Функция деления.
    """
    result = 0
    try:
        result = float(a) / float(b)
        print(f"{a} / {b} = {result}")
    # Добавляем исключения: деление на ноль и некорректный ввод
    except ZeroDivisionError:
        print(red + "Нельзя делить на ноль." + reset)
    except ValueError:
        print(red + "Функция деления работает только с числами." + reset)
# Умножение
def multiply_nums(a:int|float|str, b:int|float|str) -> None:    
    """
    Функция умножения.
    """
    result = 0
    try:
        result = float(a) * float(b)
        print(f"{a} * {b} = {result}")
    # Добавляем исключение некорректного ввода
    except ValueError:
        print(red + "Функция умножения работает только с числами." + reset)
# Сложение
def add_nums(a:int|float|str, b:int|float|str) -> None:    
    """
    Функция сложения.
    """
    result = 0
    try:
        result = float(a) + float(b)
        print(f"{a} + {b} = {result}")
    # Добавляем исключение некорректного ввода
    except ValueError:
        print(red + "Функция сложения работает только с числами." + reset)
# Разность
def difference_nums(a:int|float|str, b:int|float|str) -> None:    
    """
    Функция разности.
    """
    result = 0
    try:
        result = float(a) - float(b)
        print(f"{a} - {b} = {result}")
    # Добавляем исключение некорректного ввода
    except ValueError:
        print(red + "Функция разности работает только с числами." + reset)
# Возведение в степень
def stepen(a:int|float|str, b:int|float|str) -> None:    
    """
    Функция возведения в степень.
    """
    result = 0
    try:
        result = float(a) ** float(b)
        print(f"{a} ^{b} = {result}")
    # Добавляем исключение некорректного ввода
    except ValueError:
        print(red + "Функция возведения в степень работает только с числами." + reset)
# Запуск основного цикла
while True:
    # Выбор действия
    print(cyan + 'Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень\n10. Выход' + reset)
    choice = input(light_white + 'Введите номер действия: ' + light_blue)
    # Получаем числа и вызываем функции действий
    if choice in ('1', '2', '3', '4', '5', '10'):
        if choice == '1':
            add_nums(input(light_green + "Введите первое число: " + white), input(green + "Введите второе число: " + white))
        elif choice == '2':
            difference_nums(input(light_green + "Введите первое число: " + white), input(green + "Введите второе число: " + white))
        elif choice == '3':
            multiply_nums(input(light_green + "Введите первое число: " + white), input(green + "Введите второе число: " + white))
        elif choice == '4':
            divide_nums(input(light_green + "Введите первое число: " + white), input(green + "Введите второе число: " + white))
        elif choice == '5':
            stepen(input(light_green + "Введите основание степени: " + white), input(green + "Введите степень: " + white))
        elif choice == '10':
            print(blue + 'Выход из калькулятора. . . . . . . .' + light_magenta)
            quit()
    # Error: "Такого действия нет!"
    else:
        print(dark_red + 'Такого действия нет!' + reset)
    # Очистка экрана
    input(light_cyan + "Нажмите Enter." + yellow)
    os.system("cls")