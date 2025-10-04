# Primeiro eu crio uma variável chamada "contador" e dou a ela o valor 0.
# Essa variável vai funcionar como um "marcador" para contar quantas vezes o laço já rodou.
contador = 0 


# Agora começo um laço "while".
# A condição aqui é: enquanto contador < 10, o código dentro do while será executado.
# Ou seja, o loop vai rodar até que o contador chegue a 10.
while contador < 10:
    contador += 1  
    print(contador)


# Esse print está fora do laço, então só vai ser executado quando o while terminar.
# Ou seja, quando a condição contador < 10 não for mais verdadeira (quando contador for 10).
print("Acabou.")
