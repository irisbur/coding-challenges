# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version) -> bool:
    pass


# This is a variation of binary search.
def firstBadVersion(n: int) -> int:
    l, r = 1, n

    while l <= r:
        mid = l + ((r-l) // 2)

        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif isBadVersion(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l


