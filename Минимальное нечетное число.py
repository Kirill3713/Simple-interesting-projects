# Объявляем переменные
number_of_elements = int(input("Введите кол-во элементов в списке: ")) # кол-во эл-тов в списке
list = [] # список
# Принимаем значения в список
for _ in range(number_of_elements):
    c = int(input("Введите число: "))
    list.append(c)
# Допустим первое число в списке - минимальное
min_num = list[0]
# Перебираем числа и ищем нужное
if min_num % 2 != 0:
    for num in list:
        if num % 2 != 0:

            if min_num > num:
                min_num = num
else:
    for num in list:
        if num % 2 != 0:
            if min_num == list[0]:
                min_num = num

            else:
                if min_num > num:
                    min_num = num
# Если такого нет, то 0
if min_num == list[0] and min_num % 2 == 0:
    min_num = 0
# Выводим результат
print(min_num)