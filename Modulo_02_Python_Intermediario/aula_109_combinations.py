from itertools import combinations, permutations, product


listaNomes = ["Enzo", "Júlia", "Davi", "Fabrízia", "Aldo", "João"]

listaCamisetas = [
    ["Branca", "Cinza", "Preta"],
    ["P", "M", "G"],
    ["Feminino", "Masculino"]
]

print("Combinations:")
print(*list(combinations(listaNomes, 2)), sep='\n') # Ordem não importa
print()

print("Permutations:")
print(*list(permutations(listaNomes, 2)), sep='\n') # Ordem importa - mais combinações
print()

print("Prdouct:")
print(*list(product(*listaCamisetas)), sep='\n') # Gera todas as combinações possíveis entre os conjuntos de listas