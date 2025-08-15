"""
Aula: Variáveis e Tipos de Dados em Python

Neste exemplo, vamos aprender como declarar variáveis para armazenar informações pessoais
e como exibi-las utilizando a função print(). Também veremos como utilizar expressões
lógicas para determinar se uma pessoa é maior de idade.

Variáveis utilizadas:
    - nome (str): Primeiro nome da pessoa.
    - sobrenome (str): Sobrenome da pessoa.
    - idade (int): Idade em anos.
    - altura (float): Altura em metros.
    - ano_nascimento (int): Ano de nascimento.
    - maior_idade (bool): True se idade >= 18, caso contrário False.
"""

# Declarando variáveis com informações pessoais
nome = "Carlos"              # str: primeiro nome
sobrenome = "Silva"          # str: sobrenome
idade = 30                   # int: idade em anos
altura = 1.75                # float: altura em metros
ano_nascimento = 1993        # int: ano de nascimento

# Verificando se a pessoa é maior de idade
maior_idade = idade >= 18    # bool: True se idade >= 18

# Exibindo as informações na tela
print("Informações pessoais:")
print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} m")
print(f"Ano de nascimento: {ano_nascimento}")
print(f"É maior de idade? {maior_idade}")
