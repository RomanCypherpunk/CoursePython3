import math

def divisors(num):
    raiz_num = int(math.sqrt(num)) + 1
    lista = [a for a in range(2, raiz_num) if num%a == 0]
    if len(lista) == 0:
        return str(num) + " é primo, não tem divisores"
    return lista

num_str = input("Digite um número: ")
num_int = int(num_str)
print(f"O numero informado é {num_int}.")
print(f"Os divisores de {num_int} são: {divisors(num_int)}")

