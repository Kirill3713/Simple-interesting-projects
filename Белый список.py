# Создаем переменную для белого списка
white_list = set()
# Создаем белый список
add_request = None
print("Чтобы закончить создавать белый список нажмите кнопку Enter два раза.")
while add_request != "":
    add_request = input("Введите запросы для белого списка: ")
    white_list.add(add_request)
print("Ваш белый список: ")
# Выводим белый список
a = 1
white_list.remove("")
for request in white_list:
    print(f"{a}. {request}")
    a += 1
# Создаем переменную для запросов, получаем запросы и блокируем ненужные
all_requests = set()
add_request = None
print("Чтобы закончить задавать запросы нажмите кнопку Enter два раза.")
while add_request != "":
    add_request = input("Введите запрос: ")
    all_requests.add(add_request)
correct_requests = all_requests.intersection(white_list)
correct_requests = set(correct_requests)
# Выводим разрешенные запросы
print("Разрешенные запросы: ")
b = 1
for i in correct_requests:
    print(f"{b}. {i}")
    b += 1