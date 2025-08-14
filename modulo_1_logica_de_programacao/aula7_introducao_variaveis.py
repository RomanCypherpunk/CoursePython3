# Aula 7: Introdução a Variáveis em Python

# O que são variáveis?
# Variáveis são espaços na memória do computador usados para armazenar valores que podem ser utilizados e modificados ao longo do programa.

# Como criar uma variável em Python?
# Basta escolher um nome e usar o sinal de igual (=) para atribuir um valor.

# Exemplos de variáveis:

nome = "Maria"         # variável do tipo string (texto)
idade = 25             # variável do tipo inteiro (int)
altura = 1.68          # variável do tipo float (número decimal)
estudante = True       # variável do tipo booleano (True ou False)

# Exibindo os valores das variáveis:
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É estudante?", estudante)

# Regras para nomes de variáveis:
# - Devem começar com uma letra ou _
# - Podem conter letras, números e _
# - Não podem conter espaços ou caracteres especiais
# - Não podem ser palavras reservadas do Python (ex: if, for, print)

# Exemplos de nomes válidos:
meu_nome = "João"
idade2 = 30
_altura = 1.75

# Exemplos de nomes inválidos (não use!):
# 2idade = 20
# meu-nome = "Ana"
# print = "texto"

# Você pode mudar o valor de uma variável a qualquer momento:
idade = 26
print("Nova idade:", idade)

# Exercício:
# Crie três variáveis: cidade, ano_nascimento e aprovado.
# Atribua valores a elas e mostre os valores usando print().