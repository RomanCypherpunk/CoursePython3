def maskify(cc): #
    
    mascara = "#"*(len(cc)-4) + cc[-4:]
    print(f"O número do seu cartão é: {mascara}")
    return mascara


cartao = input("Digite o número do seu cartão: ")
maskify(cartao)