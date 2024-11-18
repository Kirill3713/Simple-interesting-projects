# Импортируем модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
light_cyan = colorama.Fore.LIGHTCYAN_EX
# Собираем информацию
name = input(cyan + "Введите имя: " + blue)
# Здороваемся
print(light_cyan + "Привет, " + name + "!" + reset)
# Собираем информацию2
birt_year = input(cyan + "Введите год рождения: " + blue)
# Собираем информацию3
year = input(cyan + "Введите который сейчас год: " + blue)
# Выполняем простейшую математическую информацию
try:
    age = int(year) - int(birt_year)
# Добавляем исключение на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение! Перезапустите программу!" + reset)
    quit()
# Выводим предсказание
print(light_cyan + "В этом году тебе исполняется" + reset, age)
if age < 0:
    print(f"По всей видимости тебя нет с нами уже {age*-1} лет.")
elif age == 0:
    print("Маловат ты еще для компьютера.")
elif age > 90:
    print("Есть сомнения по поводу корректности введенных значений! Корни ромашек покупаются на соседней улице!")