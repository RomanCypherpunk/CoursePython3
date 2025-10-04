"""
Repetições com while aninhado
------------------------------
Aqui eu estou estudando como usar o while para criar repetições
em "duas dimensões", como se fosse uma tabela de linhas e colunas.

- O laço externo controla as LINHAS
- O laço interno controla as COLUNAS

Esse tipo de estrutura é muito comum quando quero percorrer matrizes,
tabelas, grades de jogo (ex: tabuleiro do xadrez), etc.
"""

# Defino o número máximo de linhas que quero percorrer.
qtd_linhas = 5

# Defino também o número máximo de colunas.
qtd_colunas = 5


# Inicio a variável que vai representar a "linha atual".
linha = 1

# Aqui começa o laço externo (responsável pelas linhas).
# Enquanto a linha for menor ou igual ao número de linhas desejado, o loop roda.
while linha <= qtd_linhas:
    
    # Para cada linha, eu também começo a contagem das colunas do zero.
    coluna = 1

    # Esse é o laço interno (responsável pelas colunas).
    # Ele roda completamente TODAS as colunas de uma linha,
    # antes de voltar para o laço externo e passar para a próxima linha.
    while coluna <= qtd_colunas:
        # Aqui eu mostro a linha e a coluna atuais.
        # Uso f-string e a sintaxe {linha=} para mostrar o nome da variável e seu valor.
        print(f'{linha=} {coluna=}')
        
        # Depois de imprimir, aumento a coluna em +1.
        coluna += 1

    # Quando todas as colunas daquela linha acabam, eu aumento a linha em +1.
    # Assim, o programa volta para o começo do laço externo, agora na próxima linha.
    linha += 1


# Quando todas as linhas (e, consequentemente, todas as colunas) forem percorridas,
# o programa sai dos laços e executa o print abaixo.
print('Acabou')
