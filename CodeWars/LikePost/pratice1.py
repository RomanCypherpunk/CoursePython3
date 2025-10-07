def likes(lista):
    if len(lista) == 0:
        return "no one likes this"

    elif len(lista) == 1:
        return f"{lista[0]} likes this"

    elif len(lista) == 2:
        return f"{lista[0]} and {lista[1]} like this"

    elif len(lista) == 3:
        return f"{lista[0]}, {lista[1]} and {lista[2]} like this"

    else:
        curtidas = len(lista) - 2
        return f"{lista[0]}, {lista[1]} and {curtidas} others like this"

likes([])

