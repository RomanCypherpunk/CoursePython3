def get_middle(s):
    meio = len(s) // 2
    return s[meio - 1:meio + 1] if len(s) % 2 == 0 else s[meio]

print(get_middle("teste"))