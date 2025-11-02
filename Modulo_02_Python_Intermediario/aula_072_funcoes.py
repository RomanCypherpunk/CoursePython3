def multiplicador(*numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def parOuImpar(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"

print(multiplicador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(parOuImpar(999))
