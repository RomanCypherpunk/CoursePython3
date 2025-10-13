# Primeiro, preciso garantir que o usuário só continue quando digitar uma idade válida.
# Para isso, uso um loop infinito com 'while True', pois assim posso repetir a pergunta quantas vezes for necessário.
while True:
    # Aqui eu peço para o usuário digitar a idade.
    # O input sempre retorna uma string, então preciso converter depois.
    idade_str = input("Qual a sua idade? ")
    try:
        # Agora tento converter a string digitada para um número inteiro.
        # Se o usuário digitar algo que não seja número, isso vai dar erro.
        idade = int(idade_str)
        # Se a conversão der certo, uso 'break' para sair do loop.
        # Isso significa que finalmente tenho uma idade válida para trabalhar.
        break
    except ValueError:
        # Se o usuário digitar algo inválido (como letras ou símbolos),
        # o Python lança um erro do tipo ValueError.
        # Nesse caso, aviso o usuário e o loop repete a pergunta.
        print("Por favor, digite um número inteiro válido para a idade.")

# Agora que tenho certeza que a variável 'idade' é um número inteiro,
# posso fazer as verificações condicionais normalmente.

# Se a idade for maior que 18, informo que a pessoa é maior de idade.
if idade > 18:
    print("Você é maior de idade.")
# Se a idade for exatamente 18, aviso que acabou de completar 18 anos.
elif idade == 18:
    print("Você acabou de completar 18 anos!")
# Se não for nenhum dos casos acima, só pode ser menor de idade.
else:
    print("Você é menor de idade.")

# Dessa forma, garanto que o programa só segue em frente quando o usuário digita uma idade válida,
# e dou um retorno claro sobre a faixa