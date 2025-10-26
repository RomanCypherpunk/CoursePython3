"""
Interpolação básica de strings
---------------------------------
Aqui estou estudando uma forma "antiga" de formatar strings em Python,
usando o operador %.

Esse método ainda funciona até hoje e é bem útil para aprender como
a interpolação de strings evoluiu ao longo do tempo em Python.
"""

# Primeiro eu crio uma variável chamada "nome" e guardo nela uma string.
# Isso vai representar o nome da pessoa que será exibido na mensagem.
nome = 'Luiz'

# Depois eu crio uma variável "preco" que guarda um número do tipo float.
# Coloquei várias casas decimais para poder testar a formatação mais tarde.
preco = 1000.95897643

# Agora eu uso a interpolação com % para criar uma mensagem formatada.
# '%s' -> significa que vou colocar uma string no lugar
# '%.2f' -> significa que vou colocar um número float com 2 casas decimais
# O % (nome, preco) no final substitui as marcações na ordem:
#   %s será substituído por "nome"
#   %.2f será substituído por "preco"
variavel = '%s, o preço é R$%.2f' % (nome, preco)

# Aqui eu mando imprimir a frase final já formatada.
# Exemplo do resultado: "Luiz, o preço é R$1000.96"
print(variavel)


# Outro exemplo de interpolação:
# '%d' -> insere um número inteiro (decimal)
# '%X' -> insere um número inteiro em hexadecimal (letras maiúsculas)
# '%08X' -> significa que o número hexadecimal será exibido em 8 dígitos,
#           preenchendo com zeros à esquerda se for menor.
# Nesse caso estou convertendo o número 1500 para hexadecimal.
print('O hexadecimal de %d é %08X' % (1500, 1500))
# Resultado: "O hexadecimal de 1500 é 000005DC"
# (5DC é a representação hexadecimal de 1500)
