# bool (boolean) (тип данных) - может быть только True или False, название от фамилии английского математика Джорджа Буля
# Импортируем модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
light_cyan = colorama.Fore.LIGHTCYAN_EX
blue = colorama.Fore.BLUE
# Собираем информацию о дожде
try:
    is_raining = int(input(cyan + "Дождь идёт? Введите 1 или 0. " + blue))
# Добавляем исключение на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение! Перезапустите программу!" + reset)
    quit()
# Выводим информацию по зонту
if is_raining:
    print(light_cyan + "Надо взять зонт." + reset)
else:
    print(light_cyan + "Можно не брать зонт." + reset)