"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = str(input("Digite o seu CPF: "))
lista_cpf = []
lista_cpf_multiplicado = []
multiplicador = 10
primeiro_digito = 0

# Adiciona cada um dos 9 primeiros dígitos do CPF a uma lista
for digito in cpf[:9]:
    lista_cpf.append(int(digito))

# Multiplica todos os 9 primeiros digitos do CPF por 10 em contagem regressiva
for digito in lista_cpf:
    lista_cpf_multiplicado.append(digito * multiplicador)
    multiplicador -= 1

# Soma todos os resultados da lista multiplicada e multiplica por 10
total = sum(lista_cpf_multiplicado) * 10

# Obtêm o resto da divisão do total
resto_total = total % 11
primeiro_digito = 0 if resto_total > 9 else resto_total

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
lista_cpf_com_primeiro_digito_multiplicado = []
lista_cpf_com_primeiro_digito = []
multiplicador2 = 11
segundo_digito = 0

# Adiciona cada um dos 9 primeiros dígitos do CPF a uma lista com o primeiro digito
for digito in cpf[:9]:
    lista_cpf_com_primeiro_digito.append(int(digito))
lista_cpf_com_primeiro_digito.append(primeiro_digito)

# Multiplica todos os 9 primeiros digitos do CPF mais o primeiro digito por 11 em contagem regressiva
for digito in lista_cpf_com_primeiro_digito:
    lista_cpf_com_primeiro_digito_multiplicado.append(digito * multiplicador)
    multiplicador2 -= 1

# Soma todos os resultados da lista multiplicada e multiplica por 10
total2 = sum(lista_cpf_com_primeiro_digito_multiplicado) * 10

# Obtêm o resto da divisão do total
resto_total2 = total2 % 11
segundo_digito if resto_total2 < 9 else 0

# Mostra todo o processo
print(f"O CPF digitado foi: {cpf}")
print(f"O primeiro digito do CPF é: {primeiro_digito}")
print(f"O segundo digito do CPF é: {segundo_digito}")





