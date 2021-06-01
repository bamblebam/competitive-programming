class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col, grid):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1, col, grid) + dfs(row-1, col, grid) + dfs(row, col+1, grid) + dfs(row, col-1, grid)

        for i in range(n):
            for j in range(m):
                max_area = max(max_area, dfs(i, j, grid))
        return max_area
