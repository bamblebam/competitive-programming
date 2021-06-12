from functools import lru_cache


class Solution:
    def stoneGame(self, piles) -> bool:
        n = len(piles)

        @lru_cache(None)
        def solve(left, right):
            if left == right:
                return 0
            parity = (right-left-n) % 2
            if parity:
                return max(piles[left]+solve(left+1, right), piles[right]+solve(left, right-1))
            else:
                return min(-piles[left]+solve(left+1, right), -piles[right]+solve(left, right-1))
        return solve(0, n-1) > 0
