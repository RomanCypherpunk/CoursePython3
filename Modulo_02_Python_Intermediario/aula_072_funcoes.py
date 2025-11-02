def multiplicador(*numeros: int):
    resultado: int = 1
    for n in numeros:
        resultado *= n
    return resultado

def parOuImpar(numero: float):
    return f"{numero} é par" if numero % 2 == 0 else f"{numero} é ímpar"

print(multiplicador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(parOuImpar(999))
