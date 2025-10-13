"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario = float(input("Que horas são? "))
    horario_am_pm = horario - 12

    dia = horario >= 6.00 and horario < 12.00
    tarde = horario >= 12.00 and horario < 18.00
    noite = horario >= 18.00 and horario < 6.00

    if dia:
        print(f"Bom dia! Agora são exatamente {horario_am_pm:.2f}!")
    elif tarde:
        print(f"Boa tarde! Agora são exatamente {horario_am_pm:.2f} da tarde!")
    else:
        print(f"Boa noite! Agora são exatamente {horario_am_pm:.2f} da noite!")

except:
    print("Erro, digite um horário válido. (Exemplo: 12.00)")
