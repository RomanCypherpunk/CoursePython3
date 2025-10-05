"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
# Define a palavra secreta que o usuário tentará adivinhar.
palavra_secreta = 'perfume'

# Cria uma variável para armazenar as letras que o usuário já acertou.
letras_acertadas = ''

# Inicializa o contador de tentativas.
numero_tentativas = 0

# O loop continuará enquanto a palavra secreta não for completamente adivinhada.
while True:
    # Pede ao usuário para digitar uma letra.
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    # Garante que o usuário digite apenas uma letra.
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra digitada está na palavra secreta.
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Cria uma string temporária para exibir o progresso do usuário.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    # Exibe a palavra formada com as letras corretas e os asteriscos.
    print('Palavra formada:', palavra_formada)

    # Verifica se o usuário adivinhou a palavra inteira.
    if palavra_formada == palavra_secreta:
        # Limpa o terminal para uma melhor visualização (opcional).
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Exibe a mensagem de vitória e o número de tentativas.
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        
        # Zera as variáveis para um possível novo jogo.
        letras_acertadas = ''
        numero_tentativas = 0
        
        # Encerra o loop, finalizando o jogo.
        break