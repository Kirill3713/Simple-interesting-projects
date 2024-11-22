# Импортируем модули
import colorama
import random
# Создаем цвета
light_green = colorama.Fore.LIGHTGREEN_EX
reset = colorama.Fore.RESET
light_white = colorama.Fore.LIGHTWHITE_EX
# Создаем алфавиты
lower_en_alph = "abcdefghijklmnopqrstuvwxyz"
UPPER_EN_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_symbols = "!@'£$%^&*()_+-+/*:~#/?.>,<\\`¬№;><=|™§×÷}[]‰✓✕¡¿⁈⁇µ⁒€$₽₴ß↔↘↗↖⇅⇊⇈⇵▬◌▲△■■⁰³⁹ⁱ⁻⁼⁺⅓⅞⅜⅚⅔½⅘⅐₃₉₋₍₄₂₅₎₌Ⅹ∆∉∊∑√∞∘≈≤≥⑦βαθγΞλΣπρνΨΩφ·ʹιͺ;" + '"'
lower_ru_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
UPPER_RU_ALPH = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbs = (lower_en_alph, UPPER_EN_ALPH, numbers, special_symbols, lower_ru_alph, UPPER_RU_ALPH)
# Определяем функцию
def generate_password(length:int|str = 12) -> str|None:
    """
    Функция генерации пароля
    """
    # Создаем список символов пароля
    password_symbs = []
    try:
        length = int(length)
    except ValueError:
        print("Можно вводить только числа.")
        try:
            length = int(input("Введите длину кода еще раз, пожалуйста: "))
        except ValueError:
            print("Вы опять ввели некорректное значение! Перезапустите программу!")
            quit()

    if length == 12:
        for group in symbs:
            for _ in range(2):
                password_symbs.append(random.choice(group))
    elif length == 6:
        for group in symbs:
            for _ in range(1):
                password_symbs.append(random.choice(group))
    else:
        local_symbs = "abcdefgабвгдеёжАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯзийклмнопрстуфхцчшщъыьэюяhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@'£$%^&*()_+-+/*:~#/?.>,<\\`¬№;><=|™§×÷}[]‰✓✕¡¿⁈⁇µ⁒€$₽₴ß↔↘↗↖⇅⇊⇈⇵▬◌▲△■■⁰³⁹ⁱ⁻⁼⁺⅓⅞⅜⅚⅔½⅘⅐₃₉₋₍₄₂₅₎₌Ⅹ∆∉∊∑√∞∘≈≤≥⑦βαθγΞλΣπρνΨΩφ·ʹιͺ;" + '"'
        local_symbs = set(local_symbs)
        a = ""
        for symb in local_symbs:
            a += symb
        for _ in range(length):
            password_symbs.append(random.choice(a))
    # Убираем повторы
    password_set = set(password_symbs)
    while len(set(password_symbs)) != length:
        password_set = set(password_set)
        password_set = password_symbs + random.choice(random.choice(symbs))
    # Собираем пароль
    password = ""
    for symb in password_set:
        password += symb
    return password
# Точка входа
if __name__ == "__main__":
    length = input("Введите длину Вашего пароля: ")
    print(light_white + "Ваш надежный пароль:" + light_green, generate_password(length))