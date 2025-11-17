def SplitStrings(s: str) -> list[str]:
    s += '_' if len(s) % 2 else s
    return [s[i : i + 2] for i in range(0, len(s), 2)]
