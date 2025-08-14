# Aula 6: Conversão de Tipos de Dados em Python

# Convertendo para inteiro (int)
numero_str = "10"
numero_int = int(numero_str)  # Converte string para inteiro
print("String para int:", numero_int, type(numero_int))

# Convertendo para float
numero_int = 7
numero_float = float(numero_int)  # Converte inteiro para float
print("Int para float:", numero_float, type(numero_float))

# Convertendo para string
valor_float = 3.14
valor_str = str(valor_float)  # Converte float para string
print("Float para string:", valor_str, type(valor_str))

# Convertendo para booleano (bool)
# Qualquer valor diferente de zero ou string não vazia é True
valor1 = 0
valor2 = 1
valor3 = ""
valor4 = "Python"
print("0 para bool:", bool(valor1))         # False
print("1 para bool:", bool(valor2))         # True
print("String vazia para bool:", bool(valor3))  # False
print("String não vazia para bool:", bool(valor4))  # True

# Convertendo booleano para inteiro
bool_true = True
bool_false = False
print("True para int:", int(bool_true))   # 1
print("False para int:", int(bool_false)) # 0

# Convertendo booleano para string
print("True para string:", str(bool_true))   # "True"
print("False para string:", str(bool_false)) # "False"