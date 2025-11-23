import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.copy(produtos)
novos_produtos[0] = {'nome': 'Produto 5', 'preco': 20.00}
cres_produtos = sorted(produtos, key=lambda n: n["nome"], reverse=True)
print(cres_produtos)