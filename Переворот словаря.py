# Определяем функцию
def turn_dict_over(dictionary:dict) -> dict:
    """
    Функция, меняющая местами ключ и значение словаря.
    """
    dict1 = dict()
    for k, v in dictionary.items():
        dict1[v] = k
    return dict1
# Точка входа
if __name__ == "__main__":
    print(turn_dict_over({0: 9, 9:0, 77:58, 315:95}))