def FindNextSquare():  
    while True: # Enquanto for um quadrado perfeito... 
        try: # Tente executar o código abaixo, senão conseguir, faz o tratamento de erros
            import math # Importa a biblioteca math

            num = float(input("Digite um número: ")) # Requisita o numero inicial
            
            # Tratamento para número negativo ou zero
            if num <= 0:
                print("Erro: Digite um número positivo maior que zero!")
                continue  # Volta para o início do loop
            
            raiz_num = float(math.sqrt(num)) # Checa a raiz desse numero
            prox_raiz = (raiz_num + 1) # Pega a próxima raiz exata
            prox_quadrado = pow(prox_raiz, 2) # Eleva a proxima raiz exata para achar o quadrado perfeito

            if raiz_num % 1 == 0: # Se a raiz do numero incial for inteiro, mostra o próximo quadrado
                print(f"O próximo quadrado perfeito é {prox_quadrado:.0f}") 
                break # Sai do loop
            
            else: # Senão...
                print(f"O número {num:.0f} não é um quadrado perfeito")

        except ValueError: # Tratamento para caso não inserir um número
            print("Digite um número válido!")

FindNextSquare()