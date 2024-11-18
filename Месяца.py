# Создаем список месяцев
list_of_months = [
'январь', 'февраль', 'март', 'апрель',
'май', 'июнь', 'июль', 'август',
'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
]
# Сортируем по временам года
winter = list_of_months[-1:] + list_of_months[:2]
spring = list_of_months[2:5]
summer = list_of_months[5:8]
autumn = list_of_months[8:11]
# Создаем красивый словарь для времен года и месяцев
seasons = {
    "Зима": winter,
    "Весна": spring,
    "Лето": summer,
    "Осень": autumn
}
# Выводим красивущий ответ
for season, months in seasons.items():
    print(f"{season}: ", end="")
    a = 1
    for month in months:
        if a != 3:
            print(month, end=", ")
            a += 1
        else:
            print(f"{month}.")
            a = 1