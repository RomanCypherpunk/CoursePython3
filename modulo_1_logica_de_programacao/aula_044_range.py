# Aqui eu uso a função range() para gerar uma sequência de números.
# O range funciona assim: range(início, fim, passo)
# - início: número onde a sequência começa (inclusivo)
# - fim: número onde a sequência termina (exclusivo, ou seja, não entra no resultado)
# - passo: de quanto em quanto os números vão aumentar

# Nesse caso: range(1, 100, 1)
# Significa: comece no 1, vá até 99 (porque o 100 não entra) e incremente de 1 em 1.
numeros = range(1, 100, 1)


# Agora eu faço um laço for para percorrer cada número gerado pelo range.
# A cada repetição, a variável "numero" recebe o próximo valor da sequência.
for numero in numeros:
    # Aqui eu simplesmente mostro o número atual na tela.
    print(numero)
