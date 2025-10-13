"""
Iteráveis e Iteradores em Python
--------------------------------
Em Python, muitas coisas são "iteráveis" (strings, listas, ranges, etc).
Isso significa que elas podem ser percorridas **um elemento por vez**.

➡️ Conceitos importantes:
- Iterável: é o "objeto" que pode ser percorrido (ex: string, lista, range).
- Iterador: é quem sabe entregar um valor por vez do iterável.
- iter(objeto): me dá o iterador do objeto.
- next(iterador): me entrega o próximo valor do iterador.

O laço for, por baixo dos panos, usa exatamente esse mecanismo.
"""

# Aqui eu crio uma string chamada "texto".
# Strings são objetos do tipo "iterável".
texto = 'Luiz'  # <- esse é o iterável


# Normalmente, eu poderia transformar o texto em um iterador assim:
# iteratador = iter(texto)  # <- agora tenho um "objeto iterador"
#
# Depois, poderia usar um laço while + next() para ir pegando os valores:
#
# while True:
#     try:
#         letra = next(iteratador)   # Pega a próxima letra
#         print(letra)               # Mostra a letra
#     except StopIteration:
#         # Quando não há mais o que percorrer, o iterador levanta esse erro.
#         # Nesse momento, eu interrompo o loop manualmente.
#         break
#
# Esse processo é **exatamente o que o for faz por baixo dos panos**.


# Aqui estou usando o laço for de forma "normal".
# O for automaticamente chama iter() no texto
# e vai usando next() para pegar cada letra.
# Ou seja, ele percorre a string caractere por caractere.
for letra in texto:
    print(letra)
