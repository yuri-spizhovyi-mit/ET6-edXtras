"""
1. Behavior: unit tests, documentation, function name, type hints
2. Implementation: comment what each line of code does
3. Strategy pt. 1 - purpose: comment why each line of code exists
4. Strategy pt. 2 - connections: describe how different lines interact
5. strategy pt. 3 - goals: summarize the strategy using sub-goals
"""


def a(b: list[int] = []) -> list[int]:
    """ """
    c = 0
    d = 0
    e = 0

    while e < len(b):
        f = e
        while e + 1 < len(b) and b[e] == b[e + 1]:
            e += 1
        g = e - f + 1
        if g > c:
            c = g
            d = f
        e += 1

    return b[d : d + c] if c > 0 else []
