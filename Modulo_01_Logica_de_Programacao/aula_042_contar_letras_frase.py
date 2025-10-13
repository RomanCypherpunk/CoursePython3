# Aqui eu começo definindo uma string chamada "frase".
# Ela vai ser o texto onde vou procurar qual letra aparece mais vezes.
frase = 'aaaooo'


# Crio uma variável "i" que será meu índice, começando em 0.
# Esse índice vai me permitir percorrer a string letra por letra.
i = 0

# Crio uma variável "qtd_apareceu_mais_vezes" para armazenar
# a quantidade da letra mais repetida até agora.
# Começo com 0 porque ainda não verifiquei nada.
qtd_apareceu_mais_vezes = 0

# Crio uma variável "letra_apareceu_mais_vezes" para guardar
# qual foi a letra que mais se repetiu até agora.
# Por enquanto deixo como string vazia.
letra_apareceu_mais_vezes = ''


# Agora começo um laço while para percorrer cada posição da string.
# Enquanto "i" for menor que o tamanho da frase, o loop continua.
while i < len(frase):
    # Pego a letra atual usando o índice "i".
    letra_atual = frase[i]

    # Se a letra atual for um espaço em branco, eu simplesmente ignoro.
    # Isso evita contar espaços como se fossem letras.
    if letra_atual == ' ':
        i += 1  # avanço o índice para a próxima letra
        continue  # volto para o início do while sem rodar o resto do código

    # Aqui eu uso o método .count() da string.
    # Ele conta quantas vezes a "letra_atual" aparece dentro da frase.
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    # Agora faço uma comparação:
    # Se a quantidade da letra atual for MAIOR do que a maior quantidade já vista até agora...
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        # Então atualizo a "quantidade máxima"
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        # E também salvo qual foi a letra que bateu esse recorde.
        letra_apareceu_mais_vezes = letra_atual

    # Por fim, avanço o índice para analisar a próxima letra na próxima repetição do while.
    i += 1


# Quando o while terminar, significa que percorri todas as letras.
# Agora posso mostrar o resultado final na tela:
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
