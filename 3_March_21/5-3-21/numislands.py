class Solution:
    def helper(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return None
        grid[i][j] = '0'
        self.helper(grid, i-1, j)
        self.helper(grid, i+1, j)
        self.helper(grid, i, j-1)
        self.helper(grid, i, j+1)

    def numIslands(self, grid) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    answer += 1
                    self.helper(grid, i, j)
        return answer
