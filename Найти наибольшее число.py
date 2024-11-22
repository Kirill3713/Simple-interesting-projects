# Объявляем переменные
try:
    a = int(input("Введите кол-во элементов в списке: "))
    b = []
    for _ in range(a): # это значит, что мы не используем i
        c = float(input("Введите число: "))
        b.append(c)
except ValueError:
    print("Введено некорректное значение!")
    quit()
max_num = b[0]
# Ищем максимальное и выводим результат
for num in b:
    if max_num < num:
        max_num = num
print(max_num)