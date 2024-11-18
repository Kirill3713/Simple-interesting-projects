# Операции со списками
# Создаем список
authors = ['Chekhov', 'Dostoevski', 'Tolstoy', 'Nekrasov', 'Bulgakov', 'Pushkin', 'Esenin', 'Blok']
# Замена по индексу
authors[3] = "Gogol"
# Добавляем новый элемент в список (метод append)
authors.append("Turgenev")
# Удаляем элемент
del authors[0]
# Вырезаем элемент из списка
element = authors.pop(0)
print("Удален:", element)

print("Nekrasov" in authors)
print("Esenin" in authors)

print(authors)