# print(100 + 1)
# print("100" +"1")

n = [12345678, 223, 33]
k = n
k.append(0)
print(n) # [12345678, 223, 33, 0]

# У объектов всегда есть уникальный номер - айди.
print(id(n))
print(type(n))