# Primeiro eu defino uma variável chamada "condicao" e dou a ela o valor True.
# Isso vai servir como "gatilho" para o meu laço while funcionar.
# Enquanto "condicao" for verdadeira, o laço vai continuar rodando.
condicao = True

# Aqui começo um laço de repetição usando "while".
# O while funciona assim: "enquanto a condição for verdadeira, execute o bloco de código abaixo".
# No caso, enquanto condicao == True, o loop continua.
while condicao:
    # Dentro do laço, eu uso a função input() para pedir ao usuário que digite algo.
    # O texto "Digite seu nome: " aparece na tela e o que o usuário escrever será guardado em "nome".
    nome = input("Digite seu nome: ")

    # Depois eu mostro o que a pessoa digitou.
    # Uso uma f-string (string formatada), que permite incluir variáveis direto dentro do texto.
    print(f"Seu nome é {nome}!")

    # Agora faço uma verificação: se a pessoa digitou exatamente "Sair",
    # eu quero interromper o laço e não perguntar mais nada.
    if nome == "Sair":
        # A palavra-chave "break" serve para parar o while imediatamente,
        # mesmo que a condição ainda seja verdadeira.
        break

# Esse print só vai ser executado depois que o laço terminar.
# Ou seja, ele só aparece quando o usuário digitar "Sair".
print("Saiu do laço.")
