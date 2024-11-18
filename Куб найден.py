# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
light_cyan = colorama.Fore.LIGHTCYAN_EX
white = colorama.Fore.WHITE
light_white = colorama.Fore.LIGHTWHITE_EX
# Создаем функцию
def find_cube(n:int) -> int:
    """
    Функция для нахождения квадратного корня.
    """
    # Объявляем переменную x
    x = 1
    # Получаем информацию о квадрате, который необходимо найти
    try:
        n = int(n)
    # Добавляем исключение, на случай неправильного ввода
    except ValueError:
        print(red + "Введено некорректное значение!" + reset)
        return
    while x < 10001:
        # Тренировка (просто чтоб знать, что так тоже можно))
        if x ** 3 % 100 == 0:
            print(cyan + "Пропуск(", f"{x}³ = {x ** 3} "")" + reset)
            # Проверяем: это тот квадрат, который нам нужен, или нет
            if x ** 3 == n:
                print(light_white + "Число  найдено." + reset)
                break
            x += 1
            continue
        # Выводим число и его квадрат
        print(blue + f"{x}³ = {x ** 3}" + reset)
        # Проверяем: это тот квадрат, который нам нужен, или нет
        if x ** 3 == n:
            print(light_white + "Число  найдено." + reset)
            break
        # Прибавляем к x единицу
        x += 1
    # Если n - не квадрат числа
    else:
        print(white + "Число не найдено. Такого куба в пределах миллиона нет." + reset)
# Объявляем переменную x
x = 1
# Получаем информацию о кубе, который необходимо найти
try:
    n = int(input(cyan + "Введите число, которое хотите найти: " + blue))
# Добавляем исключение, на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение!" + reset)
    quit()

while x < 1001:
    # Тренировка (опять же просто чтоб знать, что так тоже можно)) (просто копируем комментарии из 'Квадрат найден.py'))
    if x ** 3 % 100 == 0:
        print(cyan + "Пропуск(", f"{x}³ = {x ** 3} "")" + reset)
        # Проверяем: это тот куб, который нам нужен, или нет
        if x ** 3 == n:
            print(light_white + "Число  найдено." + reset)
            break
        x += 1
        continue
    # Выводим число и его куб
    print(blue + f"{x}³ = {x ** 3}" + reset)
    # Проверяем: это тот куб, который нам нужен, или нет
    if x ** 3 == n:
        print(light_cyan + "Число  найдено." + reset)
        break
    # Прибавляем к x единицу
    x += 1
# На случай если n - не куб числа
else:
    print(white + "Число не найдено. Такого куба, в пределах тысячи, нет." + reset)