import collections
import functools


class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words = list(set(words))
        def Trie(): return collections.defaultdict(Trie)
        trie = Trie()
        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]
        return sum(len(word)+1 for i, word in enumerate(words) if len(nodes[i]) == 0)
