class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            d1, d2 = dict(), dict()
            for w, p in zip(word, pattern):
                if w not in d1:
                    d1[w] = p
                if p not in d2:
                    d2[p] = w
                if (d1[w], d2[p]) != (p, w):
                    return False
            return True
        return filter(match, words)
