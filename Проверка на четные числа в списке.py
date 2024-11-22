# Определяем функцию
def has_even(list_1:list) -> bool|str:
    """
    Функция для проверки на наличие четных чисел в списке.
    """
    # Проверяем тип данных введенного значения
    if not isinstance(list_1, list):
        return "Введенное значение не является списком!"
    # Проверяем список
    even_in_list = False
    for value in list_1:
        if value % 2 == 0:
            even_in_list = True
    # Возвращаем результат
    return even_in_list
# Точка входа
if __name__ == "__main__":
    print(has_even([1, 2, 3, 4, 5]))
    print(has_even([13, 3, 3, 3, 5, 2]))
    print(has_even([1, 33, 97]))
    print(has_even({1, 2, 7}))