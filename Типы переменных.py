# Создаем свой класс
class Car():
    def __init__(self) -> None:
        self.color = "red"
# Объявляем переменные и выводим типы переменных
integer = 77
print(type(integer)) # <class 'int'>

string = "string"
print(type(string)) # <class 'str'>

float_number = 90.9
print(type(float_number)) # <class 'float'>

boolean = True
print(type(boolean)) # <class 'bool'>

none = None
print(type(none))

list_type = [5, "77", [0]]
print(type(list_type)) # <class 'list'>

tuple_type = (1, 2, 3, "123", [11, 22, 33])
print(type(tuple_type)) # <class 'tuple'>

dict_type = {"9": 9, "10":10, "8": 8}
print(type(dict_type)) # <class 'dict'>

set_type = {9, 0, 5, 4, 4, 4}
print(type(set_type)) # <class 'set'>

alfa_romeo = Car()
print(type(alfa_romeo)) # <class '__main__.Car'>

print(type(alfa_romeo.color))

type_type = type(alfa_romeo)
print(type(type_type)) # <class 'type'>

func = print
print(type(func)) # <class 'builtin_function_or_method'>

method = alfa_romeo.__init__
print(type(method)) # <class 'method'>