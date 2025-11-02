# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

# -------------- PERGUNTA 1 --------------------
pergunta1_opcoes = enumerate(perguntas[0]['Opções'])

# Apresenta as questões
print(perguntas[0]['Pergunta'])
for indice, opcoes in pergunta1_opcoes:
    print(f"{indice}) {opcoes}")

#Recebe a resposta e valida se está correta
pergunta1_resposta = input("Digite sua resposta: ")
if pergunta1_resposta == perguntas[0]['Resposta']:
    print("Acertou ✅")
    acertos += 1
else:
    print("Errou ❌")


# -------------- PERGUNTA 2 --------------------
pergunta2_opcoes = enumerate(perguntas[1]['Opções'])

# Apresenta as questões
print(perguntas[1]['Pergunta'])
for indice, opcoes in pergunta2_opcoes:
    print(f"{indice}) {opcoes}")

#Recebe a resposta e valida se está correta
pergunta2_resposta = input("Digite sua resposta: ")
if pergunta2_resposta == perguntas[1]['Resposta']:
    print("Acertou ✅")
    acertos += 1
else:
    print("Errou ❌")


# -------------- PERGUNTA 3 --------------------
pergunta3_opcoes = enumerate(perguntas[2]['Opções'])

# Apresenta as questões
print(perguntas[2]['Pergunta'])
for indice, opcoes in pergunta3_opcoes:
    print(f"{indice}) {opcoes}")

#Recebe a resposta e valida se está correta
pergunta3_resposta = input("Digite sua resposta: ")
if pergunta3_resposta == perguntas[2]['Resposta']:
    print("Acertou ✅")
    acertos += 1
else:
    print("Errou ❌")


# -------------- RESULTADO / NOTAS --------------------
print(f"Você acertou {acertos} de 3 perguntas.")