# Aula 1: Comentários, Impressão e Separadores em Python

# Comentários de linha única começam com o símbolo #
# Eles servem para explicar o código e não são executados pelo Python

# Comentário de linha única

"""
Comentários de múltiplas linhas podem ser feitos usando três aspas duplas.
Eles são úteis para documentar blocos maiores de código ou explicar funções.
"""

'''
Também é possível usar três aspas simples para comentários de múltiplas linhas.
'''

# Variáveis em Python
a = 1  # Aqui estamos criando uma variável chamada 'a' e atribuindo o valor 1 a ela

# Função print() - Exibe informações na tela
# Podemos imprimir vários valores separados por vírgulas
# O parâmetro 'sep' define o separador entre os valores impressos

print(12, 34, sep=" TESTE ")  # Saída: 12 TESTE 34
print(56, 78, sep=" TESTE ")  # Saída: 56 TESTE 78

# Concatenando valores: para juntar números e textos, convertemos o número para string
print(str(a) + "b")  # Saída: 1b
