# Primeiro, pedimos ao usuário para digitar um número.
# Usamos a função input(), que exibe uma mensagem na tela e espera o usuário digitar algo.
# O valor digitado é sempre retornado como uma string (texto).
numero_1 = input("Digite um número: ")

# Em seguida, pedimos ao usuário para digitar outro número.
# Novamente, usamos input() para capturar o valor digitado.
numero_2 = input("Digite outro número: ")

# Agora, precisamos converter os valores digitados (que são strings) para números inteiros.
# Isso é necessário porque queremos somar os valores, e não é possível somar strings como números.
# Usamos a função int() para fazer essa conversão.
numero_1 = int(numero_1)
numero_2 = int(numero_2)

# Por fim, somamos os dois números e mostramos o resultado na tela.
# Usamos uma f-string para exibir a mensagem junto com o resultado da soma.
print(f"A soma dos números é: {numero_1 + numero_2}")