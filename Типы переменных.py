# Создаем свой класс
class Car():
    def __init__(self) -> None:
        ...

def my_func():
    ...
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

ellipsis = ...
print(type(ellipsis)) # <class 'ellipsis'>

type_type = type(alfa_romeo)
print(type(type_type)) # <class 'type'>

func = print
print(type(func)) # <class 'builtin_function_or_method'>

my_func_type = my_func
print(type(my_func_type)) # <class 'function'>

method = alfa_romeo.__init__
print(type(method)) # <class 'method'>