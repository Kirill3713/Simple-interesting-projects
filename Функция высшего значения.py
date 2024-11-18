# Объявляем переменную 
nums = ["1", "45", "87878", "-18"]

# def int():
#     new_nums = []
#     for num in nums:
#         new_nums.append(int(num))
#     return new_nums

def my_func(a:int|str) -> int|str:
    try:
        return int(a)**2
    except ValueError:
        return "Введено некорректное значение!"
# map вызывает функцию для каждого значения
new_nums = list(map(int, nums))
print(new_nums)
new_data = list(map(my_func, nums))
# new_data1 == new_data2, lambda - анонимная функция, которая выполняется мало раз
new_data = list(map(lambda a: int(a)**2, nums))
print(new_data)