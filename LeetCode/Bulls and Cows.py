from collections import Counter


def get_hint(secret: str, guess: str) -> str:
    bulls = []
    cows = 0

    for i, c in enumerate(guess):
        if secret[i] == guess[i]:
            bulls.append(i)
    secret = [secret[i] for i in range(len(secret)) if i not in bulls]
    guess = [guess[i] for i in range(len(guess)) if i not in bulls]

    s_count = Counter(secret)
    for i, c in enumerate(guess):
        if guess[i] in s_count and s_count[guess[i]] > 0:
            s_count[guess[i]] -= 1
            cows += 1

    return str(len(bulls)) + "A" + str(cows) + "B"


print(get_hint(secret="1807", guess="7810"))

