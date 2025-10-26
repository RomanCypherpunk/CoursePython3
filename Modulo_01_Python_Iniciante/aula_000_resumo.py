# GUIA COMPLETO DE PYTHON PARA INICIANTES
# ========================================
# Este documento cobre todos os conceitos fundamentais da programação Python
# Desenvolvido para quem está começando a programar do zero

"""
ÍNDICE DO CONTEÚDO:
1. Introdução e Conceitos Básicos
2. Variáveis e Tipos de Dados
3. Operadores
4. Entrada e Saída de Dados
5. Estruturas Condicionais
6. Estruturas de Repetição (Loops)
7. Estruturas de Dados
8. Funções
9. Manipulação de Strings
10. Tratamento de Erros
11. Exercícios Práticos
"""

# ========================================
# 1. INTRODUÇÃO E CONCEITOS BÁSICOS
# ========================================

"""
LÓGICA DE PROGRAMAÇÃO:
A lógica de programação é a forma como organizamos nossos pensamentos
para resolver problemas através de instruções que o computador pode executar.

Conceitos fundamentais:
- Algoritmo: Sequência de passos para resolver um problema
- Programa: Algoritmo escrito em uma linguagem de programação
- Sintaxe: Regras da linguagem de programação
- Semântica: Significado das instruções
"""

# Primeiro programa em Python
print("Olá, mundo!")  # Exibe texto na tela
print("Bem-vindo ao mundo da programação!")

# Comentários são importantes para documentar o código
# Use # para comentários de uma linha

"""
Use três aspas duplas para
comentários de múltiplas linhas
ou documentação de funções
"""

# ========================================
# 2. VARIÁVEIS E TIPOS DE DADOS
# ========================================

"""
VARIÁVEIS:
Variáveis são "caixas" que armazenam dados na memória do computador.
Em Python, não precisamos declarar o tipo da variável explicitamente.
"""

# Tipos básicos de dados
nome = "João"              # String (texto)
idade = 25                 # Integer (número inteiro)
altura = 1.75             # Float (número decimal)
esta_estudando = True     # Boolean (verdadeiro/falso)

# Exibindo os valores e tipos
print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Estudando: {esta_estudando} (tipo: {type(esta_estudando)})")

# Múltiplas atribuições
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Variáveis do mesmo valor
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# ========================================
# 3. OPERADORES
# ========================================

print("\n=== OPERADORES ===")

# OPERADORES ARITMÉTICOS
num1 = 10
num2 = 3

print("Operadores Aritméticos:")
print(f"{num1} + {num2} = {num1 + num2}")    # Adição
print(f"{num1} - {num2} = {num1 - num2}")    # Subtração
print(f"{num1} * {num2} = {num1 * num2}")    # Multiplicação
print(f"{num1} / {num2} = {num1 / num2}")    # Divisão
print(f"{num1} // {num2} = {num1 // num2}")  # Divisão inteira
print(f"{num1} % {num2} = {num1 % num2}")    # Módulo (resto)
print(f"{num1} ** {num2} = {num1 ** num2}")  # Exponenciação

# OPERADORES DE COMPARAÇÃO
print("\nOperadores de Comparação:")
print(f"{num1} == {num2}: {num1 == num2}")   # Igual
print(f"{num1} != {num2}: {num1 != num2}")   # Diferente
print(f"{num1} > {num2}: {num1 > num2}")     # Maior
print(f"{num1} < {num2}: {num1 < num2}")     # Menor
print(f"{num1} >= {num2}: {num1 >= num2}")   # Maior ou igual
print(f"{num1} <= {num2}: {num1 <= num2}")   # Menor ou igual

# OPERADORES LÓGICOS
a_bool = True
b_bool = False

print("\nOperadores Lógicos:")
print(f"{a_bool} and {b_bool} = {a_bool and b_bool}")  # E lógico
print(f"{a_bool} or {b_bool} = {a_bool or b_bool}")    # OU lógico
print(f"not {a_bool} = {not a_bool}")                  # NÃO lógico

# OPERADORES DE ATRIBUIÇÃO
numero = 10
print(f"\nValor inicial: {numero}")

numero += 5   # Equivale a: numero = numero + 5
print(f"Após +=5: {numero}")

numero -= 3   # Equivale a: numero = numero - 3
print(f"Após -=3: {numero}")

numero *= 2   # Equivale a: numero = numero * 2
print(f"Após *=2: {numero}")

numero /= 4   # Equivale a: numero = numero / 4
print(f"Após /=4: {numero}")

# ========================================
# 4. ENTRADA E SAÍDA DE DADOS
# ========================================

print("\n=== ENTRADA E SAÍDA ===")

# Função print() - Saída de dados
print("Texto simples")
print("Múltiplos", "valores", "separados")
print("Valor:", 42)

# Formatação de strings
nome_usuario = "Maria"
idade_usuario = 30
print(f"Olá, {nome_usuario}! Você tem {idade_usuario} anos.")  # f-string (recomendado)
print("Olá, {}! Você tem {} anos.".format(nome_usuario, idade_usuario))  # format()
print("Olá, %s! Você tem %d anos." % (nome_usuario, idade_usuario))  # % formatting

# Função input() - Entrada de dados
print("\n--- Exemplo de entrada (descomente para testar) ---")
# nome_input = input("Digite seu nome: ")
# idade_input = int(input("Digite sua idade: "))  # Converte para inteiro
# print(f"Olá, {nome_input}! Você tem {idade_input} anos.")

# ========================================
# 5. ESTRUTURAS CONDICIONAIS
# ========================================

print("\n=== ESTRUTURAS CONDICIONAIS ===")

"""
Estruturas condicionais permitem que o programa tome decisões
baseadas em condições específicas.
"""

# IF simples
numero = 10
if numero > 0:
    print("O número é positivo")

# IF-ELSE
numero = -5
if numero > 0:
    print("O número é positivo")
else:
    print("O número é negativo ou zero")

# IF-ELIF-ELSE
nota = 85
if nota >= 90:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
else:
    print("Conceito: F")

# Condições compostas
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
elif idade >= 18:
    print("Precisa tirar a carteira")
else:
    print("Não pode dirigir ainda")

# Operador ternário (if inline)
numero = 15
resultado = "Par" if numero % 2 == 0 else "Ímpar"
print(f"{numero} é {resultado}")

# ========================================
# 6. ESTRUTURAS DE REPETIÇÃO (LOOPS)
# ========================================

print("\n=== ESTRUTURAS DE REPETIÇÃO ===")

"""
Loops permitem executar um bloco de código repetidamente.
Python oferece dois tipos principais: for e while.
"""

# LOOP FOR
print("Loop FOR:")

# For com range()
print("Contando de 1 a 5:")
for i in range(1, 6):  # range(início, fim) - fim não incluso
    print(f"Número: {i}")

# For com range() e step
print("Números pares de 0 a 10:")
for i in range(0, 11, 2):  # range(início, fim, passo)
    print(i, end=" ")
print()  # Nova linha

# For iterando sobre string
palavra = "Python"
print(f"Letras da palavra '{palavra}':")
for letra in palavra:
    print(letra, end=" ")
print()

# LOOP WHILE
print("\nLoop WHILE:")

# While básico
contador = 1
print("Contando até 5 com while:")
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Importante! Atualizar a variável de controle

# While com condição de parada
print("Digite números (0 para parar):")
# Simulação (descomente para testar interativamente)
"""
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        print(f"Você digitou: {numero}")
print("Programa encerrado!")
"""

# CONTROLE DE FLUXO EM LOOPS
print("Exemplo de break e continue:")
for i in range(1, 11):
    if i == 5:
        continue  # Pula a iteração quando i=5
    if i == 8:
        break     # Para o loop quando i=8
    print(i, end=" ")
print("\nLoop encerrado!")

# LOOP ANINHADO
print("\nLoop aninhado (tabuada):")
for i in range(1, 4):
    print(f"Tabuada do {i}:")
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)

# ========================================
# 7. ESTRUTURAS DE DADOS
# ========================================

print("\n=== ESTRUTURAS DE DADOS ===")

"""
Estruturas de dados são formas de organizar e armazenar dados.
Python oferece várias estruturas built-in.
"""

# LISTAS (ARRAYS)
print("LISTAS:")
# Lista é uma coleção ordenada e mutável
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Lista de frutas: {frutas}")

# Acessando elementos (índice começa em 0)
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")  # Índice negativo conta do final

# Modificando elementos
frutas[1] = "manga"
print(f"Lista após modificação: {frutas}")

# Métodos de lista
frutas.append("pêra")          # Adiciona no final
print(f"Após append: {frutas}")

frutas.insert(1, "kiwi")       # Insere em posição específica
print(f"Após insert: {frutas}")

fruta_removida = frutas.pop()  # Remove e retorna o último
print(f"Fruta removida: {fruta_removida}")
print(f"Lista atual: {frutas}")

frutas.remove("kiwi")          # Remove por valor
print(f"Após remover kiwi: {frutas}")

# Operações com listas
numeros = [1, 2, 3, 4, 5]
print(f"Números: {numeros}")
print(f"Comprimento: {len(numeros)}")
print(f"Soma: {sum(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")

# Slicing (fatiamento)
print(f"Primeiros 3: {numeros[:3]}")
print(f"Últimos 2: {numeros[-2:]}")
print(f"Do meio: {numeros[1:4]}")

# Lista comprehension (compreensão de lista)
quadrados = [x**2 for x in range(1, 6)]
print(f"Quadrados: {quadrados}")

pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares: {pares}")

# TUPLAS
print("\nTUPLAS:")
# Tupla é uma coleção ordenada e imutável
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")
print(f"X: {coordenadas[0]}, Y: {coordenadas[1]}")

# Tupla com diferentes tipos
dados_pessoa = ("João", 25, True)
nome, idade, ativo = dados_pessoa  # Desempacotamento
print(f"Nome: {nome}, Idade: {idade}, Ativo: {ativo}")

# DICIONÁRIOS
print("\nDICIONÁRIOS:")
# Dicionário é uma coleção de pares chave-valor
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheira"
}

print(f"Dicionário pessoa: {pessoa}")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa.get('idade')}")  # Método get() é mais seguro

# Modificando e adicionando
pessoa["idade"] = 31
pessoa["email"] = "maria@email.com"
print(f"Pessoa atualizada: {pessoa}")

# Iterando sobre dicionário
print("Iterando sobre o dicionário:")
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

# Ou usando items()
for chave, valor in pessoa.items():
    print(f"{chave} -> {valor}")

# CONJUNTOS (SETS)
print("\nCONJUNTOS:")
# Conjunto é uma coleção não-ordenada de elementos únicos
numeros_set = {1, 2, 3, 4, 5, 3, 2, 1}  # Duplicatas são removidas
print(f"Conjunto: {numeros_set}")

# Operações de conjunto
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"União: {set1 | set2}")
print(f"Interseção: {set1 & set2}")
print(f"Diferença: {set1 - set2}")

# ========================================
# 8. FUNÇÕES
# ========================================

print("\n=== FUNÇÕES ===")

"""
Funções são blocos de código reutilizáveis que executam tarefas específicas.
Elas ajudam a organizar o código e evitar repetição.
"""

# Função simples
def saudacao():
    """Função que exibe uma saudação"""
    print("Olá! Como você está?")

# Chamando a função
saudacao()

# Função com parâmetros
def saudacao_personalizada(nome):
    """Função que recebe um nome e exibe saudação personalizada"""
    print(f"Olá, {nome}! Como você está?")

saudacao_personalizada("Carlos")

# Função com múltiplos parâmetros
def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    area = largura * altura
    return area

resultado = calcular_area_retangulo(5, 3)
print(f"Área do retângulo: {resultado}")

# Função com parâmetro padrão
def saudacao_completa(nome, tratamento="Sr./Sra."):
    """Função com parâmetro padrão"""
    return f"Olá, {tratamento} {nome}!"

print(saudacao_completa("Silva"))
print(saudacao_completa("Maria", "Dra."))

# Função com múltiplos retornos
def operacoes_basicas(a, b):
    """Retorna múltiplas operações entre dois números"""
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else 0
    return soma, subtracao, multiplicacao, divisao

s, sub, m, d = operacoes_basicas(10, 3)
print(f"10 e 3: soma={s}, sub={sub}, mult={m}, div={d:.2f}")

# Função com *args (argumentos variáveis)
def somar_todos(*numeros):
    """Soma todos os números passados como argumentos"""
    return sum(numeros)

print(f"Soma de vários números: {somar_todos(1, 2, 3, 4, 5)}")

# Função com **kwargs (argumentos nomeados variáveis)
def exibir_informacoes(**info):
    """Exibe informações passadas como argumentos nomeados"""
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

print("Informações da pessoa:")
exibir_informacoes(nome="Ana", idade=28, cidade="Rio de Janeiro")

# ========================================
# 9. MANIPULAÇÃO DE STRINGS
# ========================================

print("\n=== MANIPULAÇÃO DE STRINGS ===")

"""
Strings são sequências de caracteres. Python oferece muitos métodos
para manipular e trabalhar com strings.
"""

texto = "  Python é Incrível!  "
print(f"Texto original: '{texto}'")

# Métodos básicos de string
print(f"Maiúsculo: {texto.upper()}")
print(f"Minúsculo: {texto.lower()}")
print(f"Título: {texto.title()}")
print(f"Sem espaços: '{texto.strip()}'")
print(f"Comprimento: {len(texto)}")

# Verificações
print(f"Contém 'Python': {texto.find('Python') != -1}")
print(f"Começa com '  Py': {texto.startswith('  Py')}")
print(f"Termina com '!  ': {texto.endswith('!  ')}")

# Substituição
novo_texto = texto.replace("Incrível", "Fantástico")
print(f"Texto substituído: {novo_texto}")

# Divisão e junção
frase = "Python,Java,JavaScript,C++"
linguagens = frase.split(",")
print(f"Lista de linguagens: {linguagens}")

nova_frase = " | ".join(linguagens)
print(f"Frase juntada: {nova_frase}")

# Formatação avançada
nome = "Pedro"
idade = 25
salario = 5000.50

# f-strings (Python 3.6+)
print(f"Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}")

# Método format()
print("Nome: {}, Idade: {}, Salário: R$ {:.2f}".format(nome, idade, salario))

# Strings multilinha
texto_longo = """
Este é um texto
que ocupa múltiplas
linhas do código.
"""
print(texto_longo)

# ========================================
# 10. TRATAMENTO DE ERROS
# ========================================

print("\n=== TRATAMENTO DE ERROS ===")

"""
Tratamento de erros permite que o programa continue executando
mesmo quando encontra situações inesperadas.
"""

# Try-except básico
try:
    numero = int("abc")  # Vai gerar erro
except ValueError:
    print("Erro: Não foi possível converter para número")

# Try-except com múltiplas exceções
try:
    resultado = 10 / 0
    lista = [1, 2, 3]
    print(lista[10])
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except IndexError:
    print("Erro: Índice fora dos limites da lista")

# Try-except-else-finally
def dividir_numeros(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")
        return None
    except TypeError:
        print("Erro: Tipos inválidos para divisão")
        return None
    else:
        print("Divisão realizada com sucesso")
        return resultado
    finally:
        print("Operação de divisão finalizada")

print(f"Resultado: {dividir_numeros(10, 2)}")
print(f"Resultado: {dividir_numeros(10, 0)}")

# Função para validar entrada
def obter_numero_valido():
    """Solicita um número até que seja válido"""
    while True:
        try:
            # entrada = input("Digite um número: ")
            # numero = float(entrada)  # Descomente para testar
            numero = 42  # Valor fixo para demonstração
            return numero
        except ValueError:
            print("Por favor, digite um número válido!")
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário")
            return None

# ========================================
# 11. EXERCÍCIOS PRÁTICOS
# ========================================

print("\n=== EXERCÍCIOS PRÁTICOS ===")

"""
Vamos aplicar os conceitos aprendidos em alguns exercícios práticos.
"""

# Exercício 1: Calculadora simples
def calculadora_simples(num1, operador, num2):
    """Calculadora com operações básicas"""
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operador inválido"

print("Exercício 1 - Calculadora:")
print(f"5 + 3 = {calculadora_simples(5, '+', 3)}")
print(f"10 - 4 = {calculadora_simples(10, '-', 4)}")
print(f"6 * 7 = {calculadora_simples(6, '*', 7)}")
print(f"15 / 3 = {calculadora_simples(15, '/', 3)}")

# Exercício 2: Verificador de números primos
def eh_primo(numero):
    """Verifica se um número é primo"""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("\nExercício 2 - Números primos até 20:")
primos = [num for num in range(1, 21) if eh_primo(num)]
print(f"Números primos: {primos}")

# Exercício 3: Contador de palavras
def contar_palavras(texto):
    """Conta a frequência de palavras em um texto"""
    palavras = texto.lower().split()
    contador = {}
    
    for palavra in palavras:
        # Remove pontuação básica
        palavra_limpa = palavra.strip('.,!?;:"')
        if palavra_limpa in contador:
            contador[palavra_limpa] += 1
        else:
            contador[palavra_limpa] = 1
    
    return contador

texto_exemplo = "Python é incrível. Python é fácil de aprender. Programar em Python é divertido."
print(f"\nExercício 3 - Contador de palavras:")
print(f"Texto: {texto_exemplo}")
resultado_contagem = contar_palavras(texto_exemplo)
for palavra, frequencia in resultado_contagem.items():
    print(f"'{palavra}': {frequencia}")

# Exercício 4: Gerador de sequência Fibonacci
def fibonacci(n):
    """Gera os primeiros n números da sequência Fibonacci"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        proximo = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(proximo)
    
    return fib_sequence

print(f"\nExercício 4 - Fibonacci (primeiros 10 números):")
fib_numeros = fibonacci(10)
print(f"Sequência: {fib_numeros}")

# Exercício 5: Organizador de notas de estudantes
def processar_notas_estudantes():
    """Sistema simples para gerenciar notas de estudantes"""
    estudantes = {
        "Ana": [85, 92, 78, 96],
        "Bruno": [76, 88, 92, 85],
        "Carlos": [92, 95, 87, 91],
        "Diana": [78, 85, 88, 82]
    }
    
    print("\nExercício 5 - Sistema de Notas:")
    print("Relatório de Desempenho dos Estudantes")
    print("-" * 40)
    
    for nome, notas in estudantes.items():
        media = sum(notas) / len(notas)
        nota_maxima = max(notas)
        nota_minima = min(notas)
        
        if media >= 90:
            conceito = "A"
        elif media >= 80:
            conceito = "B"
        elif media >= 70:
            conceito = "C"
        else:
            conceito = "D"
        
        print(f"Estudante: {nome}")
        print(f"  Notas: {notas}")
        print(f"  Média: {media:.1f}")
        print(f"  Maior nota: {nota_maxima}")
        print(f"  Menor nota: {nota_minima}")
        print(f"  Conceito: {conceito}")
        print()

processar_notas_estudantes()

# ========================================
# DICAS FINAIS E BOAS PRÁTICAS
# ========================================

print("=== DICAS FINAIS ===")

"""
BOAS PRÁTICAS EM PYTHON:

1. Nomenclatura:
   - Use nomes descritivos para variáveis e funções
   - snake_case para variáveis e funções: minha_variavel
   - PascalCase para classes: MinhaClasse
   - MAIÚSCULAS para constantes: PI = 3.14159

2. Comentários:
   - Comente código complexo
   - Use docstrings para documentar funções
   - Mantenha comentários atualizados

3. Estrutura do código:
   - Uma função deve fazer apenas uma coisa
   - Evite funções muito longas (máximo ~20 linhas)
   - Use espaços em branco para separar blocos lógicos

4. Tratamento de erros:
   - Sempre trate erros esperados
   - Use try-except para código que pode falhar
   - Não ignore erros silenciosamente

5. Eficiência:
   - Use compreensões de lista quando apropriado
   - Evite loops desnecessários
   - Conheça as estruturas de dados adequadas para cada situação

6. Legibilidade:
   - Código é lido mais vezes do que é escrito
   - Prefira clareza à concisão excessiva
   - Use f-strings para formatação de strings
"""

print("Parabéns! Você completou o guia básico de Python!")
print("Continue praticando e explorando mais recursos da linguagem.")
print("Recursos para continuar estudando:")
print("- Documentação oficial: https://docs.python.org/")
print("- Python.org: https://python.org/")
print("- Exercícios práticos: HackerRank, LeetCode, Exercism")

# Exemplo de execução das funções principais
if __name__ == "__main__":
    print(f"\nExemplo de execução:")
    print(f"Área de um retângulo 4x6: {calcular_area_retangulo(4, 6)}")
    print(f"15 é primo? {eh_primo(15)}")
    print(f"17 é primo? {eh_primo(17)}")