"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input("Digite um número inteiro: "))
    numero_par = numero % 2 == 0

    if numero_par:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

except ValueError:
    print("Erro. Digite um número inteiro válido.")
