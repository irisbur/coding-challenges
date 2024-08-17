# Improved iterative solution.
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    c = 0
    a, b = 1, 2
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c


# Initial recursive solution.
def climb_stairs_recursive(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)