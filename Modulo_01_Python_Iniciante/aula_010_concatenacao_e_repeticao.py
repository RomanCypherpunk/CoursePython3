# Aula 10: Concatenando e Repetindo Strings em Python

# Concatenando strings com o operador +
# Podemos unir várias strings usando o sinal de +
frase = "Python" + " " + "é" + " " + "legal"
print(frase)  # Saída: Python é legal

# Repetindo caracteres com o operador *
# O operador * permite repetir uma string várias vezes
letras_repetidas = 'A' * 10
print(letras_repetidas)  # Saída: AAAAAAAAAA

# Juntando nome e sobrenome em uma única string
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Saída: Maria Silva

# Concatenando texto com números
# Para juntar um número com uma string, precisamos converter o número para string
idade = 25
mensagem = "Idade: " + str(idade)
print(mensagem)  # Saída: Idade: 25

# Criando uma linha de separação usando repetição de caracteres
separador = "-" * 30
print(separador)  # Saída: ------------------------------

# Repetindo uma palavra várias vezes
# Podemos repetir uma palavra e remover espaços extras com strip()
saudacao = ("Oi! " * 3).strip()
print(saudacao)  # Saída: Oi! Oi! Oi!