from functools import lru_cache


class Solution:
    def longestStrChain(self, words) -> int:
        words_set = set(words)

        @lru_cache(None)
        def dp(word):
            if word not in words_set:
                return 0
            return max(dp(word[:i]+word[i+1:]) for i in range(len(word)))+1
        return max(dp(word) for word in words)
