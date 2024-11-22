# Определяем функцию
def get_initials(full_name:str) -> str:
    """
    Функция для получения инициалов.
    """
    if not isinstance(full_name, str):
        return "Введено некорректное значение!"
    full_name = full_name.split()
    return full_name[0][0:1] + "." + full_name[1][0:1] + "." + full_name[2][0:1] + "."
# Создаем переменную имени
name1 = "Герасимов Михаил Матвеевич"
# Разбиваем ее в список
name1 = name1.split()
print(name1[0][0:1] + "." + name1[1][0:1] + "." + name1[2][0:1] + ".")
# Создаем и редактируем вторую переменную имени
name2 = "Воробьёв Андрей Олегович"
name2 = name2.split()
print(name2[0][0:1] + "." + name2[1][0:1] + "." + name2[2][0:1] + ".")