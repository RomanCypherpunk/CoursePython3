"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
nome_curto = len(nome) <= 4
nome_medio = len(nome) > 4 and len(nome) < 7
nome_longo = len(nome) > 7

if nome_curto:
    print(f"Seu nome é {nome}, é um nome muito curto!")

elif nome_medio:
    print(f"Seu nome é {nome}, é um nome médio!")

elif nome_longo:
    print(f"Seu nome é {nome}, é um nome muito longo!")

else:
    print("Digite um nome válido.")