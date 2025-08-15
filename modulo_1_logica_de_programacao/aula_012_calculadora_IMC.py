# Calculadora de IMC (Índice de Massa Corporal)
# Este programa calcula o IMC de uma pessoa a partir de seus dados pessoais.

# Dados pessoais
nome = "Enzo Xavier"
idade = 20
altura_metros = 1.75
peso_kg = 74.5

# Cálculo do IMC
imc = round(peso_kg / (altura_metros ** 2), 1)

# Exibição dos resultados
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura_metros} m")
print(f"Peso: {peso_kg} kg")
print(f"IMC: {imc}")