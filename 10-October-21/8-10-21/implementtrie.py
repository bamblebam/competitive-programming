class Trie:

    def __init__(self):
        self.trie = defaultdict(dict)

    def insert(self, word: str) -> None:
        root = self.trie
        for i, letter in enumerate(word):
            if letter in root:
                root = root[letter]
            else:
                root[letter] = dict()
                root = root[letter]
            if i == len(word)-1:
                if 'end' in root:
                    root['end'].append(word)
                else:
                    root['end'] = [word]

    def search(self, word: str) -> bool:
        root = self.trie
        for i, letter in enumerate(word):
            if letter not in root:
                return False
            root = root[letter]
            if i == len(word)-1 and 'end' in root and word in root['end']:
                return True
        return False

    def startsWith(self, word: str) -> bool:
        root = self.trie
        for i, letter in enumerate(word):
            if letter not in root:
                return False
            root = root[letter]
            if i == len(word) and word in root['end']:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
