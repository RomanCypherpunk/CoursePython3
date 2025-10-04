"""
Repetições com while
------------------------
O while é uma estrutura de repetição em Python que significa "enquanto".
Ou seja: ele repete um bloco de código ENQUANTO a condição for verdadeira.

⚠️ Atenção: se a condição nunca se tornar falsa, o programa fica em um
"loop infinito", rodando sem parar.
"""

# Aqui eu inicio um contador com o valor 0.
# Ele vai ser usado para controlar o número de repetições do laço.
contador = 0


# Começo o laço while.
# A condição é: "enquanto contador for menor ou igual a 100".
# Isso significa que, no máximo, o contador pode chegar a 100.
while contador <= 100:
    # A cada vez que o laço roda, eu aumento o contador em 1.
    # Assim, o contador vai progredindo em direção ao limite (100).
    contador += 1


    # Primeiro caso especial:
    # Se o contador for igual a 6, eu NÃO quero mostrar o número 6.
    if contador == 6:
        print('Não vou mostrar o 6.')
        # A palavra "continue" faz o seguinte:
        # pula o restante do código abaixo e volta direto para o começo do while.
        continue


    # Segundo caso especial:
    # Se o contador estiver entre 10 e 27 (incluindo os dois),
    # eu também NÃO quero mostrar esses números.
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        # Uso novamente o "continue" para pular a execução do restante do laço.
        continue


    # Se o contador não entrou em nenhum dos "ifs" anteriores,
    # o número é exibido normalmente aqui.
    print(contador)


    # Terceiro caso especial:
    # Se o contador chegar a 40, eu quero parar o laço completamente.
    if contador == 40:
        # A palavra "break" interrompe o while de uma vez, sem continuar a repetição.
        break


# Quando o laço termina (seja porque chegou em 100 ou porque foi interrompido no 40),
# o programa segue normalmente e executa esse print final.
print('Acabou')
