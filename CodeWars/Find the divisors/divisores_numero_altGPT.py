import math

def divisores():
    try:
        numero = int(input("Digite um número: "))
        
        # Trata números inválidos
        if numero <= 0:
            print("Digite um número positivo maior que zero!")
            return
        
        print(f"O número digitado é {numero}.")

        if numero == 1:
            print("O número 1 não tem divisores além dele mesmo.")
            return

        # Busca divisores até a raiz quadrada
        raiz_numero = int(math.sqrt(numero))
        lista_divisores = []
        
        for n in range(2, raiz_numero + 1):
            if numero % n == 0:
                lista_divisores.append(n)
        
        # Verifica se é primo (fora do loop!)
        if len(lista_divisores) == 0:
            print(f"O número {numero} é primo, não contém divisores.")
        else:
            lista_divisores.sort()  # Ordena a lista
            print(f"Os divisores de {numero} são: {lista_divisores}")
    
    except ValueError:
        print("Digite um número inteiro válido!")

divisores()