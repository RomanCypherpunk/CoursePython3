def FindNextSquare(square):
    root = square ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1