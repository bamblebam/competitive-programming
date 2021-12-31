class Solution:
    def palindromePairs(self, words):
        ans = set()
        d = {word: idx for idx, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                if word[j:] == word[j:][::-1] and (suf := word[:j][::-1]) in d and i != (k := d[suf]):
                    ans.add((i, k))
                if word[:j] == word[:j][::-1] and (pre := word[j:][::-1]) in d and i != (k := d[pre]):
                    ans.add((k, i))
        return ans
