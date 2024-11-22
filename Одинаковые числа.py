# Объявляем переменные
print("Введите 3 числа (после ввода каждого нажимайте, пожалуйста, Enter): ")
try:
    a, b, c = int(input()), int(input()), int(input())
except ValueError:
    print("Введено некоррктное значение!")
    quit()
# Проверка на равные числа
if a == b and a == c and b == c:
    print(3)
elif a != b and a != c and b != c:
    print(0)
else:
    print(2)