from functools import lru_cache
from itertools import permutations


class Solution:
    def shortestSuperstring(self, words) -> str:
        @lru_cache(None)
        def connect(w1, w2):
            return [w2[i:] for i in range(len(w1)+1) if w1[-i:] == w2[:i] or not i][-1]
        n = len(words)
        dp = [[(float('inf'), "")]*n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = (len(words[i]), words[i])
        for i in range(1 << n):
            bits = [j for j in range(n) if i & 1 << j]
            for j, k in permutations(bits, 2):
                x = dp[i ^ 1 << j][k][1]+connect(words[k], words[j])
                dp[i][j] = min(dp[i][j], (len(x), x))
        return min(dp[-1])[1]
