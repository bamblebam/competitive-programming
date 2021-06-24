from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7

        @lru_cache(None)
        def helper(moves, row, col):
            if moves < 0:
                return 0
            if row == m or col == n or row < 0 or col < 0:
                return 1
            total = helper(moves-1, row, col-1)+helper(moves-1, row,
                                                       col+1)+helper(moves-1, row-1, col)+helper(moves-1, row+1, col)
            return total % mod
        return helper(maxMove, startRow, startColumn)
