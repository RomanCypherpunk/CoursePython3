"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
numero_letras_nome = int(len(nome))
nome_invertido = str(nome[::-1])
primeira_letra_nome = str(nome[0])

if nome and idade:
    if '' in nome:
        print(f"Seu nome é {nome}.")
        print(f"Sua idade é {idade}.")
        print(f"Seu nome contém {numero_letras_nome} letras.")
        print(f"Seu nome invertido é {nome_invertido}")
        print(f"A primeira letra do seu nome é {primeira_letra_nome}")
        print(f"Seu nome contém espaços.")
    
    else:
        print(f"Seu nome é {nome}.")
        print(f"Sua idade é {idade}.")
        print(f"Seu nome contém {numero_letras_nome} letras.")
        print(f"Seu nome invertido é {nome_invertido}")
        print(f"A primeira letra do seu nome é {primeira_letra_nome}")
        print(f"Seu nome não contém espaços.")  

else:
    print("Por favor, digite um nome e uma idade.")