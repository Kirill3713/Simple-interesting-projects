# Объявляем переменную
months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
'Декабрь')
# Берем только зиму
winter = months[-1:] + months[0:2]
print(winter)
# Распаковываем кортеж
dec, jan, feb = winter
print(dec, jan, feb)
# Остальные времена года
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]
# Первая и вторая половина года
half_year1 = winter[1], winter[2], spring, summer[0]
half_year2 = summer[1], summer[2], autumn, winter[0]
print(half_year1, half_year2)