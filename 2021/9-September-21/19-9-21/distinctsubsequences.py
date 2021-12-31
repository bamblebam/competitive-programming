class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @lru_cache(None)
        def dp(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if s[i] == t[j]:
                return dp(i+1, j)+dp(i+1, j+1)
            return dp(i+1, j)
        return dp(0, 0)
