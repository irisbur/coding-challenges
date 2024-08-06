def decrypt(code, k):
    decrypted = []
    n = len(code)
    for i in range(n):
        decoded = 0
        for j in range(abs(k)):
            if k > 0:
                decoded += code[(i + j + 1) % n]
            if k < 0:
                decoded += code[(i - j - 1) % n]
        decrypted.append(decoded)
    return decrypted
