# Создаем функцию
def dec_to_bi(n10:int|str) -> str:
    """
    Функция для перевода числа из десятичной в двоичную систему.
    """
    # Объявляем необходимые переменные и обрабатываем входные данные
    my_list = []
    try:
        n10 = int(n10)
    except ValueError:
        return "Введено некорректное значение!"
    n10_copy = n10
    # Вычисляем двоичное число
    while n10 != 0:
        my_list.append(n10%2)
        n10 //= 2
    n2 = ""
    my_list.reverse()
    for n in my_list:
        n2 += str(n)
    # Возвращаем результат
    return f"{n10_copy}₁₀ = {n2}₂"

# Точка входа
if __name__ == "__main__":
    print(dec_to_bi(10))
    print(dec_to_bi(2))
    print(dec_to_bi(8))
    print(dec_to_bi(23))