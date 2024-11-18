# Создаем функцию
def get_middle_len(*strings) -> float:
    """
    Функция вычисляющая среднюю длину значений.
    В аргумент можно передовать абсолютно что угодно.
    """
    if strings == ():
        return 0.0
    # Переводим введенные значения в формат строк
    list_of_lengths = []
    for value in strings:
        list_of_lengths.append(len(str(value)))
    # Находим сумму всех значений
    sum = 0
    for length in list_of_lengths:
        sum += length
    # Находим среднее арифметическое
    middle_len = sum/len(list_of_lengths)
    # Возвращаем результат
    return middle_len
# Точка входа
if __name__ == "__main__":
    print(get_middle_len(1, "34560", 9.0, {90, "sdfghjk", 78, "gh", 90}, (), {90:90}, 90*0))
    print(get_middle_len())