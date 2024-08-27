
# Note the edge cases, when I want to have <= and when I want <.
def my_sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    l, h = 0, x

    while l <= h:
        mid = l + ((h - l) // 2)
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            h = mid - 1

    return -1


print(my_sqrt(6))
