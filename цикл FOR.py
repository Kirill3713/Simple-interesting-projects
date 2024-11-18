# Цикл FOR
for i in range(5): # i счетчик, который изменяется до n не включительно
    print("Hello!")
    print(i)
# Складываем все числа от 25 до 50
a = 0
for i in range(25, 51):
    a += i
print(a)
# Выводим все числа от а до б
try:
    a, b = int(input("Введите два числа, но чтобы а ≤ б: ")), int(input())
except ValueError:
    print("Введено некорректное значение!")
    quit()
for i in range(a, b + 1):
    if i == b:
        print(i, end =".\n")
    else:
        print(i, end =", ")
# Делим все числа от 2 до n
n = 5
result = 1
for i in range(2, n + 1):
    result /= i
print(result)