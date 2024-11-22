# Целочисленная арифметика
# х % у - остаток от деления числа х на число у
# х // у - деление нацело числа х на число у
# Создаем функцию
def sum_and_number_of_digits(n:int|str) -> int|str:
    """
    Функция для получения количества и суммы чисел.
    """
    # Обрабатываем входные данные и создаем переменные суммы и количества символов
    try:
        n = int(n)
    except ValueError:
        return "Введено некорректное значение!"
    sum = 0
    number_of_digits = 0
    # Вычисляем значения
    while n > 0:
        b = n % 10 # получаем последнюю цифру
        sum += b # прибавляем ее к сумме цифр
        number_of_digits += 1 # +1 к количеству цифр
        n = n // 10 # Убираем последнюю цифру
    # Выводим результат
    return f"Число: {n}.\nКоличество цифр: {number_of_digits};\nСумма цифр: {sum}."
# Точка входа
if __name__ == "__main__":
    print(sum_and_number_of_digits(9857))
    print(sum_and_number_of_digits("777"))
    print(sum_and_number_of_digits("dfghbnjm"))