# Объявляем переменные
print("Введите 3 числа: ")
a, b, c = int(input()), int(input()), int(input())
# Проверка на равные числа
if a == b and a == c and b == c:
    print(3)
elif a != b and a != c and b != c:
    print(0)
else:
    print(2)