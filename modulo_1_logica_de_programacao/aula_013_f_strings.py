# Definindo as variáveis
nome = 'Enzo Xavier'
altura = 1.75
peso = 74.5
imc = peso / altura ** 2

# Usando f-strings para formatar strings de forma simples e legível
# Basta colocar um 'f' antes das aspas e usar chaves {} para inserir variáveis ou expressões

# Exemplo básico:
print(f'O nome é {nome}')

# Também é possível formatar números, como limitar casas decimais:
print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}')

# Explicando a formatação:
# {altura:.2f} -> mostra a altura com 2 casas decimais
# {imc:.2f}    -> mostra o IMC com 2 casas decimais

# Você pode criar várias linhas usando f-strings:
mensagem = (
    f'{nome} tem {altura:.2f} de altura,\n'
    f'pesa {peso} quilos e seu IMC é {imc:.2f}'
)
print(mensagem)

