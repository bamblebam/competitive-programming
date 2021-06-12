from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones) -> int:
        n = len(stones)
        prefix = [0]+list(accumulate(stones))
        is_cached = [[False]*n for _ in range(n)]
        cache = [[0]*n for _ in range(n)]

        def solve(left, right):
            if left == right:
                return 0

            if is_cached[left][right]:
                return cache[left][right]

            op1 = prefix[right+1]-prefix[left+1]-solve(left+1, right)
            op2 = prefix[right]-prefix[left]-solve(left, right-1)
            is_cached[left][right] = True
            cache[left][right] = max(op1, op2)
            return cache[left][right]
        return solve(0, n-1)
