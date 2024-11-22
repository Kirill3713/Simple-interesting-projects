# Определяем функцию
def fib_list(n:int|float|str) -> list[int]|str:
    """
    Функция для получения чисел Фибоначчи до заданного числа.
    """
    # Сложный, непонятный, но работающий способ №1.
    # Объявляем переменные
    # a = 1
    # b = 0
    # c = 0
    # x = 0
    try:
        n = int(n)
    except ValueError:
        print("Введено некорректное значение!")
    # while c <= n: 
    #     if x % 2 == 0:
    #         a += b
    #         print(a, end = " ")
    #         x += 1
    #         c = a
    #     else:
    #         b += a
    #         print(b, end = " ")
    #         x += 1
    #         c = b
    # print()


    # Способ №2
    fib1 = 1
    fib2 = 1
    list_of_fibs = []
    # Выдаем последовательность
    while  fib1 <= n:
        list_of_fibs.append(fib1)
        temp = fib1
        fib1 = fib2
        fib2 = temp + fib2
    list_of_fibs.append(f"{fib1}.")
    return list_of_fibs
# Точка входа
if __name__ == "__main__":
    fib_list(100000)