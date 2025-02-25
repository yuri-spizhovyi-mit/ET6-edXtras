def list_up_to(n: int) -> list:
    assert n >= 0, 'n must be greater than or equal to 0'

    if n == 0:
        return [0]
        
    return list_up_to(n - 1) + [n]

assert list_up_to(0) == [0]
assert list_up_to(2) == [0, 1, 2]
assert list_up_to(6) == [0, 1, 2, 3, 4, 5, 6]