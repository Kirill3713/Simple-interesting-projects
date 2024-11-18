number_of_user = 1
# name = "Пользователь" - значение по умолчанию
def say_hello(age: int, name:str = f"Пользователь №{number_of_user}") -> None:
    """
    Функция для приветствия пользователя
    """
    # Здороваемся
    print(f"Привет, {name}!")
    print("Вы указали возраст:", age)
    # Прибавляем к счетчику пользователей еще одного
    global number_of_user
    number_of_user += 1

say_hello(100)
# say_hello("Ваня", 14) - Ошибка!
say_hello(name = "Ваня", age = 14)

# Когда стоит *, то можно давать сколько угодно значений, и они будут записываться в кортеж
def multiply(*nums:int) -> int:
    """
    Функция, умножающая все введенные значения.
    """
    result = 1
    # Умножаем все значения
    for num in nums:
        result *= num
    # Возвращаем результат
    return result
# Вызываем функцию
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(multiply(111, 222))
print(multiply(0))
# Аргументы переменной длинны в формате  ключ: значение  (словаря)
def create_user(**params:str) -> dict:
    """
    Функция создания профиля с разными параметрами.
    """
    # Возвращаеим словарь с параметрами
    return params
# Вызов функции
print(create_user(name = "Иван Иваныч", lname = "Иванов", job = "Учитель"))