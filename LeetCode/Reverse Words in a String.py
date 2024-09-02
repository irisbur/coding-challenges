

def reverse_words(s: str) -> str:
    words = s.split()
    return ' '.join(words[::-1]).strip()


print(reverse_words("a good   example"))
