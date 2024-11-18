# Создаем функцию
def get_list(n:int|float|str) -> list[int]:
    """
    Функция для получения списка натуральных чисел от одного до n. 
    """
    # Обрабатываем входные данные и создаем переменную списка
    try:
        n = int(n)
    except ValueError:
        return "Введено некорректное значение!"
    my_list = []
    # Заполняем список
    for i in range(n):
        my_list.append(i+1)
    # Возвращаем список
    return my_list
# Точка входа
if __name__ == "__main__":
    print(get_list(9))
    print(get_list("3"))
    print(get_list(8.9))