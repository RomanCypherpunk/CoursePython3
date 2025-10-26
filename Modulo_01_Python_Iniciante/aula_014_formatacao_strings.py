# Definindo algumas variáveis
a = 'AAAAA'      # Variável 'a' recebe uma string
b = 'BBBBBB'     # Variável 'b' recebe outra string
c = 1.1          # Variável 'c' recebe um número float

# Criando uma string com placeholders para formatação
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

# Usando o método format para substituir os placeholders pelos valores das variáveis
formato = string.format(
    nome1=a,    # Substitui {nome1} por 'a'
    nome2=b,    # Substitui {nome2} por 'b'
    nome3=c     # Substitui {nome3:.2f} por 'c' formatado com 2 casas decimais
)

# Exibindo o resultado final
print(formato)