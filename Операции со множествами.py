# Создаем два множества
set_1 = {'CSS', 'Python', 'HTML', 'C++', 'Go'}
set_2 = {'CSS', 'Python', 'Go', 'Rust', 'Java'}
# Объединение двух множеств в одно (без повторов)
print(set_1.union(set_2))
print(set_1 | set_2)
# Пересечение множеств (только то, что есть в обоих множествах)
print(set_1.intersection(set_2))
print(set_1 & set_2)
# Разность
print(set_1.difference(set_2))
print(set_1 - set_2)
print(set_2 - set_1)
# Симметричная разность
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)
# Добавление значения
set_1.add('JavaScript')