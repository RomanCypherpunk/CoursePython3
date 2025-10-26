# Aqui eu defino uma string chamada "frase".
# Ela será o texto que vou percorrer letra por letra.
frase = "A democracia é falha, pois dá voz a maioria, e a maioria é burra."


# Agora uso um laço for para percorrer a string.
# O for em Python é muito prático porque já percorre cada elemento da sequência
# sem precisar de um índice manual (como no while).
# Ou seja: a cada repetição, a variável "letra" já recebe diretamente
# a próxima letra da frase.
for letra in frase:
    # Aqui eu simplesmente imprimo a letra atual.
    # Isso vai fazer com que cada caractere da string apareça um embaixo do outro.
    print(letra)
