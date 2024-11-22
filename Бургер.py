# Импортируем модули
import colorama
# Интересное примечание
# ВАЖНО!!!!!!! Чтобы вывести символ "\" в консоль, перед ним нужно поставить еще один такой символ
# Вот так: "\\"
# Создаем переменные цветов
light_red = colorama.Fore.LIGHTRED_EX
light_yellow = colorama.Fore.LIGHTYELLOW_EX
green = colorama.Fore.GREEN
reset = colorama.Fore.RESET
# Создаем функции для слоев бутерброда
def top_bread() -> None:
    """
    Верхняя булка.
    """
    print(light_yellow + "/￣￣￣\\" + reset)
def tomato() -> None:
    """
    Помидоры.
    """
    print(light_red + "◯◯◯◯◯◯◯◯" + reset)
def meat_and_chease() -> None:
    """
    Мясо и сыр.
    """
    print(green + "🧀🍗🧀🍗\n" + green + " ^^^^^^" + reset)
def bottom_bread() -> None:
    """
    Нижняя булка.
    """
    print(light_yellow + "\\______/" + reset)
# Вызываем функции и приятного аппетита!
top_bread()
tomato()
meat_and_chease()
bottom_bread()