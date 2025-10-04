# Aqui eu começo declarando uma string que vai ser usada no exercício.
# Essa string representa um nome qualquer.
nome = "Enzo Xavier"

# Depois crio uma variável chamada "indice" e inicializo em 0.
# Essa variável vai me ajudar a percorrer cada letra do nome,
# pois em Python as strings são acessadas por índice (posição).
indice = 0

# Também crio uma string vazia chamada "novo_nome".
# Ela vai ser usada para ir montando uma nova versão do nome,
# onde cada letra terá um asterisco "*" depois dela.
novo_nome = ""

# Aqui uso a função len() para saber quantas letras existem no nome original.
qtd_letras_nome = len(nome)

# E aqui uso len() no "novo_nome", que por enquanto está vazio.
# (nesse ponto, a quantidade de letras é 0)
qtd_letras_novo_nome = len(novo_nome)


# Agora começa o laço while.
# A ideia é percorrer o nome letra por letra.
# Enquanto o índice for menor que o tamanho do nome, continuo o loop.
while indice < len(nome):
    # Aqui eu pego a letra correspondente ao índice atual.
    # Exemplo: se indice = 0, pego a primeira letra ("E").
    letra = nome[indice]

    # Mostro a letra atual na tela, só para acompanhar o processo.
    print(letra)

    # Depois de acessar a letra, aumento o índice em +1
    # para ir para a próxima posição do nome.
    indice += 1 

    # Agora, ao mesmo tempo em que percorro o nome,
    # vou construindo uma nova string.
    # Pego a letra atual e adiciono um "*" depois dela.
    # Esse resultado é acumulado dentro da variável novo_nome.
    novo_nome += letra + "*"


# Quando o while terminar (ou seja, percorri todas as letras do nome),
# imprimo as informações finais.

# Mostro o nome original.
print(f"O nome é: {nome}.")

# Mostro o novo nome que eu fui construindo.
# Exemplo: "E*n*z*o* *X*a*v*i*e*r*"
print(f"O novo nome é: {novo_nome}.")

# Mostro quantas letras o nome original tinha (sem contar os asteriscos).
print(f"O nome: {nome} tem {qtd_letras_nome} letras.")
