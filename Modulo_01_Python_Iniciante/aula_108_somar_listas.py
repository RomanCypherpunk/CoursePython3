lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [6, 99, 105, 40]
lista_3 = [x + y for x, y in zip(lista_1, lista_2)]
print(lista_3)