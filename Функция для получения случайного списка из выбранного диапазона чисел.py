# Импортируем нужные модули
import random
import colorama
red = colorama.Fore.RED
reset = colorama.Fore.RESET
# Создаем функцию
def get_random_list(start:int, end:int, len:int) -> list[int]|str:
    """
    Функция для получения случайного списка из выбранного диапазона.
    """
    try:
        # Создаем нужный список
        my_list = []
        for _ in range(len):
            my_list.append(random.randint(int(start), int(end)))
        # Возвращаем список
        return my_list
    # Добавляем исключения
    except ValueError:
        return red + "Введено некорректное значение!" + reset
    except TypeError:
        return red + "Введено некорректное значение!" + reset
# Точка входа
if __name__ == "__main__":
    print(get_random_list(0, 11, 5))
    print(get_random_list(0, 50, "ghj"))