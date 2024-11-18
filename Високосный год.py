# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
light_white = colorama.Fore.LIGHTWHITE_EX
blue = colorama.Fore.BLUE
light_blue = colorama.Fore.LIGHTBLUE_EX
def check_leap_year(year:int|str) -> bool:
    """
    Функция для проверки високосности года
    """
    # Узнаем какой сейчас год
    try:
        year = int(year)
    # Добавляем исключение, на случай неправильного ввода
    except ValueError:
        return red + "Введено некорректное значение!" + reset
    # Выводим информацию
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        False

# Узнаем какой сейчас год
try:
    year = int(input(cyan + "Введите год, чтобы определить високосный ли он: " + light_white))
# Добавляем исключение, на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение!" + reset)
    quit()
# Выводим информацию
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(light_blue + "Год високосный." + light_white)
else:
    print(blue + "Год не високосный." + light_white)