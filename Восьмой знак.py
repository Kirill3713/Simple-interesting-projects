# Делим все числа от одного до N и выводим результат
result = 1
try:
    n = int(input("Введите число: "))
except ValueError:
    print("Введено некорректное значение!")
for i in range(1, n + 1):
    result /= i
print(result)
# Выводим восьмой знак результата
a = str(result)
a = a[7]
print(a)
# Выполняем задание
if int(a) >= 5:
    result += 0.000001
    b = str(result)
    print(b[0:7])
elif int(a) <= 5:
    a = str(result)
    print(a[0:7])
else:
    print(result)