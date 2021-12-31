import itertools


class WordFilter:

    def __init__(self, words):
        self.d = dict()
        for i, word in enumerate(words):
            for p, s in itertools.product(range(len(word)+1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get((prefix, suffix), -1)
