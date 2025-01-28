# Объявляем переменные
print("Введите 3 числа (после ввода каждого нажимайте, пожалуйста, Enter): ")
try:
    a, b, c = int(input()), int(input()), int(input())
except ValueError:
    print("Введено некоррктное значение!")
    quit()
# Проверка на равные числа
if a == b and a == c and b == c:
    print("Все числа одинаковые.")
elif a != b and a != c and b != c:
    print("Нет одинаковых чисел.")
else:
    print("Только два числа одинаковые.")