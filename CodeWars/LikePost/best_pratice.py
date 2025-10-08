# Aqui eu defino uma função chamada "likes", que vai receber uma lista chamada "names".
# Essa lista contém os nomes das pessoas que curtiram (deram like) em alguma publicação.
def likes(names):
    # Primeiro, pego o tamanho da lista, ou seja, quantas pessoas curtiram.
    n = len(names)

    # A ideia dessa função é retornar uma frase diferente dependendo da quantidade de pessoas.
    # Para isso, eu uso um dicionário (que é uma estrutura de chave:valor).
    # Cada chave representa um número de curtidas e o valor é a frase correspondente.
    # Assim, posso acessar a frase certa de forma prática.
    return {
        # Caso 0 curtidas → ninguém curtiu
        0: 'no one likes this',

        # Caso 1 curtida → apenas uma pessoa curtiu, então uso o singular "likes"
        1: '{} likes this',

        # Caso 2 curtidas → duas pessoas curtiram, então uso o plural "like"
        2: '{} and {} like this',

        # Caso 3 curtidas → três pessoas curtiram, então listo os três nomes
        3: '{}, {} and {} like this',

        # Caso 4 ou mais curtidas → mostro os dois primeiros nomes e digo quantos "outros" curtiram
        4: '{}, {} and {others} others like this'
    # Aqui vem a parte inteligente:
    # uso min(4, n) para garantir que a chave nunca passe de 4.
    # Exemplo: se tiver 10 pessoas, o min(4, 10) = 4 → usa o formato do caso "4 ou mais".
    }[min(4, n)].format(
        # Agora, preencho os espaços {} com os primeiros nomes da lista.
        # O operador * desempacota a lista "names[:3]", ou seja, envia até 3 nomes separadamente.
        *names[:3],

        # Aqui defino o valor do parâmetro "others", que só será usado no caso de 4 ou mais curtidas.
        # "others" representa o número de pessoas extras além das duas primeiras mostradas.
        others=n - 2 if n > 3 else 1
    )

likes(["Enzo", "João", "Pedro", "Davi", "Paulo"])
# 💡 Resumindo o raciocínio:
# - Eu usei um dicionário para escolher rapidamente o formato certo da frase.
# - Usei o método "format" para inserir os nomes nas posições corretas dos {}.
# - E usei o min(4, n) para evitar erros e simplificar a lógica.
#
# Exemplo prático:
# likes([]) → "no one likes this"
# likes(["Luiz"]) → "Luiz likes this"
# likes(["Luiz", "Maria"]) → "Luiz and Maria like this"
# likes(["Luiz", "Maria", "Ana"]) → "Luiz, Maria and Ana like this"
# likes(["Luiz", "Maria", "Ana", "João", "Pedro"]) → "Luiz, Maria and 3 others like this"
