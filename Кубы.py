# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
light_cyan = colorama.Fore.LIGHTCYAN_EX
# Объявляем переменную x
x = 1
# Выводим все кубы до 1000
while x < 1001:
    # Выводим число и его куб
    print(blue + f"{x}³ = {x ** 3}" + reset)
    # Прибавляем к x единицу
    x += 1
# Возводим в куб заданное число и выводим результат
try:
    a = float(input(cyan + "Введите число, которое хотите возвести в куб: " + blue))
    print(light_cyan + "Ваше число в кубе:" + reset, a ** 3)
# Добавляем исключение, на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение!" + reset)