import itertools
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        @lru_cache(None)
        def dfs(row, col):
            answer = 1
            for dx, dy in directions:
                new_row = row+dx
                new_col = col+dy
                if new_row >= 0 and new_col >= 0 and new_row < rows and new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    answer = max(answer, dfs(new_row, new_col)+1)
            return answer
        return max(dfs(i, j) for i, j in itertools.product(range(rows), range(cols)))
