"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

compras = []
compras_enumerada = enumerate(compras)

while True:
    print("")
    print("Digite a operação desejada: ")
    operacao = input("[I]: Inserir / [A]: Apagar / [L]: Listar / [S]: Sair ").upper() # Recebe a operação do usuário

    # -------------------------------- OPERAÇÃO INSERIR --------------------------------
    if operacao == "I":
        item = str(input("Digite o item que deseja inserir: "))
        compras.append(item) # Adiciona o item na lista de compras
        print(f"{item} foi inserido na lista de compras.")

    # -------------------------------- OPERAÇÃO APAGAR --------------------------------
    if operacao == "A":
        if not compras: # Encerra a operação se a lista de compras estiver vazia
            print("Lista está vazia, não há o que apagar.")

        else:
            for indice, item in compras_enumerada: # Exibe a lista de compras através de lista enumerada
                print(indice, item)

            # Tratamento de erros para caso o usuário insira um índice errado para remover
            try:
                item = int(input("Digite o índice do item que deseja apagar da lista: ")) # Recebe o índice para remover na lista
                compras.pop(item)
                print(f"Item removido da lista de compras.")

            except ValueError:
                print("Digite um índice válido! (Exemplo: 1)")
    
    # -------------------------------- OPERAÇÃO LISTAR --------------------------------
    if operacao == "L":
        if not compras: # Encerra a operação se a lista de compras estiver vazia
            print("Lista está vazia, não há o que listar.")

        else:
            print("Lista de compras atualizada:")
            for indice, item in compras_enumerada: # Exibe a lista de compras através de lista enumerada
                print(indice, item)

    # -------------------------------- OPERAÇÃO SAIR --------------------------------
    if operacao == "S":
        print("Fim!")
        break