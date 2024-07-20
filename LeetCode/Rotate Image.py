def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    Main idea: we can swap between the rows and cloumns in place, meaning we need 
    O(n) space complexity
    """
    n = len(matrix)
    l, r = 0, n - 1
    while l < r:
        for i in range(r - l):
            t, b = l, r
            top_left = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = top_left
        l += 1
        r -= 1
