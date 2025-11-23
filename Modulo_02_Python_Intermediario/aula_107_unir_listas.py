# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

listaCidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
listaEstados = ['BA', 'SP', 'MG', 'RJ']

def zipper(list_1, list_2):
    interval = min(len(list_1), len(list_2))
    return [(list_1[i], list_2[2]) for i in range(interval)]

print(zipper(listaCidades, listaEstados))