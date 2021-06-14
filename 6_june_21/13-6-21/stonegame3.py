from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def solve(start):
            if start >= n:
                return 0
            best = -float('inf')
            best = max(best, stoneValue[start]-solve(start+1))
            if start+1 < n:
                best = max(best, stoneValue[start] +
                           stoneValue[start+1]-solve(start+2))
            if start+2 < n:
                best = max(
                    best, stoneValue[start]+stoneValue[start+1]+stoneValue[start+2]-solve(start+3))
            return best
        ans = solve(0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
