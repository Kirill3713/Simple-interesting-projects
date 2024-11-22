# Создаем функцию
def divide_nums(a:int|float|str, b:int|float|str) -> float|str:
    """
    Функция для деления.
    """
    result = 0
    try: # Пытаемся выполнить код
        result = float(a) / float(b)
    except ZeroDivisionError: # Исключение
        return "Нельзя делить на ноль."
    except ValueError:
        return "Функция деления работает только с числами."
    finally: # Код, который выполняется вконце, и в любом случае (есть ошибка, или ее нет).
        return result
# Проверяем
print(divide_nums(5, 5))
print(divide_nums(10, 2))
print(divide_nums(5, 0))
print(divide_nums(78, "строка"))
