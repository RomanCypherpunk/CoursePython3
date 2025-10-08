def likes(names):
    n = len(names)
    others = len(names) - 2
    return {
        0: "Ninguém curtiu isso.",
        1: "{} curtiu isso.",
        2: "{} e {} curtiu isso.",
        3: "{}, {} e {} curtiu isso.",
        4: "{}, {} e mais {} curtiram isso.",
    }[min(4, n)].format(*names[:3])



likes(["Enzo", "João", "Pedro", "Davi", "Paulo"])