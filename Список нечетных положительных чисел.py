def odd_list(n:int|float|str) -> list[int]:
    """
    Функция для создания списка нечетных натуральных чисел от одного до n.
    """
    # Обрабатываем число и создаем нужные переменные
    try:
        n = int(n)
    except ValueError:
        return "Введено некорректное значение!"
    list = []
    num = 1
    counter = 0
    # Заполняем список
    while counter != n:
        if num % 2 != 0:
            list.append(num)
        num += 1
        counter += 1
    # Выводим результат
    return list
# Точка входа
if __name__ == "__main__":
    print(odd_list(9))
    print(odd_list(78.9))
    print(odd_list("12"))
    print(odd_list("dfghj"))