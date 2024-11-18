# Кортеж (tuple)
# Пример кортежа
my_tuple = 1, 3.7, "строка"
# Смотрим тип переменной
print(type(my_tuple))
# Выводим кортеж на экран
print(my_tuple)
# Срезы в кортежах
print(my_tuple[0:2])
print(my_tuple[-1])

# Пробуем изменить значение
# my_tuple[0] = 999 - ошибка, кортеж неизменяемый (по сути это единственное отличие от списка, поэтому его можно назвать неизменяемым списком).

# Распаковка кортежа
а, б, в = my_tuple
print(а)
print(б)
print(в)

# Перебираем кортеж так же, как и список
for value in my_tuple:
    print(value*2)
# Преобразуем кортеж в список
my_list = list(my_tuple)
print(my_list)
print(type(my_list))