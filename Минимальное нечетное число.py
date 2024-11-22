# Определяем функцию
def min_odd(*nums:int|float|str|list[int|float|str]|tuple[int|float|str]|set[int|float|str]) -> int|float|str:
    """
    Функция, вычисляющая минимальное нечетное число.
    """
    # Объявляем переменные
    num_list = []
    nums = list(nums)
    try:
        while nums != []:
            if isinstance(nums[0], list) or isinstance(nums[0], set) or isinstance(nums[0], tuple):
                temp_num_list = list(nums[0])
                for num in temp_num_list:
                    num_list.append(float(num))
            else:
                num_list.append(float(nums[0]))
            del nums[0]
    except TypeError:
        return "Формат введенного значения не обрабатывается."
    if num_list == []:
        num_list = list(nums)
    # Допустим первое число в списке - минимальное
    min_num = num_list[0]
    # Перебираем числа и ищем нужное
    if min_num % 2 != 0:
        for num in num_list:
            if num % 2 != 0:
                if min_num > num:
                    min_num = num
    else:
        for num in num_list:
            if num % 2 != 0:
                if min_num == num_list[0]:
                    min_num = num

                else:
                    if min_num > num:
                        min_num = num
    # Если такого нет, то 0
    if min_num == num_list[0] and min_num % 2 == 0:
        min_num = 0
    return min_num
# Точка входа
if __name__ == "__main__":
    print(min_odd(0, 9, 8, 78, 77, 77, 5, -9.7))
    print(min_odd([0, 9, 8, 78, 77, 77, 5, -9.7]))
    print(min_odd((0, 9, 8, "78", 77, 77, 5, -9.7)))
    print(min_odd({0, 9, 8, 78, 77, 77, 5, -9.7}))
    print(min_odd({(0, 9, 8, 78), 77, 77, 5, -9.7}))
    print(min_odd({(0, 9, (8, 78, 77)), 77, 5, -9.7}))
    