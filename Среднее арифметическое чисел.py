# Создаем функцию
def get_arithmetic_mean(*nums:int|float|str|list[int|float|str]|tuple[int|float|str]|set[int|float|str]) -> float:
    """
    Функция, вычисляющая среднее арифметическое чисел.
    """
    if nums == ():
        return 0.0
    # Переводим введенные значения в формат нецелочисленных в зависимости от типа и добавляем исключение на случай некорректного ввода 
    list_of_int = []
    if isinstance(nums[0], list) or isinstance(nums[0], tuple) or isinstance(nums[0], set):
        try:
            for num in nums[0]:
                list_of_int.append(float(num))
        except ValueError:
            return "Введено некорректное значение!"
    else:
        try:
            for num in nums:
                list_of_int.append(float(num))
        except ValueError:
            return "Введено некорректное значение!"
    # Находим сумму всех значений
    sum = 0
    for num in list_of_int:
        sum += num
    # Находим среднее арифметическое
    mean = sum/len(list_of_int)
    # Возвращаем результат
    return mean
# Точка входа
if __name__ == "__main__":
    print(get_arithmetic_mean(1, 2, 7, 9, 0, 7))
    print(get_arithmetic_mean(1.9, 3.8, 5, 0.5, 34))
    print(get_arithmetic_mean("78", 5, "-19", 4.5, 7))
    print(get_arithmetic_mean(2, "5"))
    print(get_arithmetic_mean([9, 7, "23", -23.5]))
    print(get_arithmetic_mean({8, 8, 8, 8, 9, 5.5555, "123"}))
    print(get_arithmetic_mean((70, 77, 80, 88, 90, 9.9, "100")))
    print(get_arithmetic_mean())