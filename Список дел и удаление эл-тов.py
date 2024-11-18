# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
light_green = colorama.Fore.LIGHTGREEN_EX
blue = colorama.Fore.BLUE
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
light_cyan = colorama.Fore.LIGHTCYAN_EX
# Создаем список дел
dela = [
    'погулять с друзьями',
    'почитать книжку',
    'рассмотреть потолок',
    'поиграть в Civilization V',
    'помыть посуду',
    'настроить телескоп',
    'сделать-таки домашку'
]
# Выводим его на экран
print(light_green + "Список дел:" + reset)
a = 1
for delo in dela:
    print(green + f"{a}. {delo}" + reset)
    a += 1
print(white + "Чтобы выйти из программы нажмите кнопку Enter." + reset)
# Удаляем то, что не нравится родителям
while True:
    a = input(blue + 'Какой элемент удалить? Введите номер: ' + light_cyan)
    if a == '':
        break
    else:
        try:
            a = int(a) - 1
        # Добавляем исключение, на случай неправильного ввода
        except ValueError:
            print(red + "Введено некорректное значение!" + reset)
            quit()
        del dela[a]
# Печатаем новый список дел
print(light_green + "Новый список дел:" + reset)
a = 1
for delo in dela:
    print(green + f"{a}. {delo}" + reset)
    a += 1