# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
yellow = colorama.Fore.YELLOW
green = colorama.Fore.GREEN
light_green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
try:
    math = int(input(cyan + "Введите оценку по математике: " + blue))
    litra = int(input(cyan + "Введите оценку по литературе: " + blue))
# Добавляем исключение, на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение!" + reset)
    quit()
if math > 5 or litra > 5:
    print(red + "Введено некорректное значение!" + reset)
    quit()
# И
if math == 5 and litra == 5:
    print(light_green + "Молодец!" + reset)
elif math > 3 and litra > 3:
    print(green + "Хороший результат." + reset)
else:
    print(yellow + "Есть куда стремиться!" + reset)
# Или
if math == 5 or litra == 5:
    print(green + "У тебя есть пятёрка." + reset)
else:
    print(red + "У тебя нет пятёрок." + reset)
print(0 or 5 and 0)