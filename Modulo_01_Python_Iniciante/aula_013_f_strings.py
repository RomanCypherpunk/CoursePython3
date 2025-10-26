# Aula: Utilizando f-strings para formatação de strings em Python

# Neste exemplo, vamos aprender como utilizar f-strings para inserir variáveis e formatar valores dentro de strings de maneira simples e eficiente.

# Definindo as variáveis principais
nome = 'Enzo Xavier'
altura = 1.75
peso = 74.5

# Calculando o IMC (Índice de Massa Corporal)
imc = peso / altura ** 2

# Exibindo o nome utilizando f-string
print(f'Nome: {nome}')

# Exibindo altura, peso e IMC, formatando os números para duas casas decimais
print(f'{nome} tem {altura:.2f}m de altura, pesa {peso}kg e seu IMC é {imc:.2f}')

# Também é possível criar mensagens em várias linhas usando f-strings
mensagem = (
    f'{nome} tem {altura:.2f}m de altura,\n'
    f'pesa {peso}kg e seu IMC é {imc:.2f}'
)
print(mensagem)

# Observação:
# - {altura:.2f} formata o valor da altura para duas casas decimais.
# - {imc:.2f} faz o mesmo para o IMC.
# - O '\n' serve para quebrar a linha na mensagem.
