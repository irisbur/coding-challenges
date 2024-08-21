class Node:
    def __init__(self):
        self.is_prefix = True
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.is_prefix = False

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_prefix == False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
