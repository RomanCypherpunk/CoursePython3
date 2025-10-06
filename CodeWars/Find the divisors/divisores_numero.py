import math

def divisors(n: int) -> list[int] | str:
    """
    Retorna uma lista dos divisores de n (exceto 1 e n) em ordem crescente.
    Se n for primo, retorna a string "(n) is prime".
    """
    if n <= 1:
        # A restrição do problema é n > 1, mas é bom adicionar uma verificação
        return "Input must be an integer greater than 1"

    divs = set()

    # Percorre de 2 até a raiz quadrada de n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            # Adiciona o par, que é n / i
            divs.add(n // i)

    if not divs:
        # Se nenhum divisor foi encontrado, o número é primo
        return f"{n} nenhum, {n} é um número primo."
    else:
        # Converte para lista e ordena
        return sorted(list(divs))
    
num_str = input("Digite um número: ")
num_int = int(num_str)
print(f"O numero informado é {num_int}.")
print(f"Os divisores de {num_int} são: {divisors(num_int)}")