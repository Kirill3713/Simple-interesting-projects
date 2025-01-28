# Создаем функцию
def find_simple_divisors(n:int|str) -> str:
    """
    Функция для разложения числа на простые множители.
    """
    # Объявляем необходимые переменные и обрабатываем входные данные
    try:
        n = int(n)
    except ValueError:
        return "Введено некорректное значение!"
    simple_nums = []
    d = 2
    num = n
    my_num = num
    # Находим множители
    while my_num/d != 1:
        if my_num%d == 0:
            simple_nums.append(d)
            my_num /= d
        else:
            d += 1
    simple_nums.append(d)
    # Выодим результат
    print(f"Простые делители числа {num}:", end=" ")
    for i in range(len(simple_nums)):
        if i == len(simple_nums)-1:
            print(f"{simple_nums[-1]}.")
        else:
            print(simple_nums[i], end=", ")
# Точка входа
if __name__ == "__main__":
    find_simple_divisors(216)
    find_simple_divisors(123)
    find_simple_divisors(108)
    find_simple_divisors(99991)
    find_simple_divisors(122)