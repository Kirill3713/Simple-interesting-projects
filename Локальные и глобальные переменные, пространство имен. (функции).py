# Локальные и глобальные переменные
# Пространство имен

username = "User" # Глобальная переменная
color = "green"
# Определяем новую функцию
def get_user() -> None:
    """
    Учебная функция для примера.
    """
    # Обращаемся к глобальной переменной
    global color
    color = "blue"
      
    username = "Вася123" # Локальная переменная
    # test = 123
    print(f"Имя пользователя: {username}") # Глобальная переменная доступна к чтению внутри функции

# Вызываем функцию
get_user()

print(username)
# print(test) Если так написать, то будет ошибка (NameError: name 'test' is not defined)

print(color)