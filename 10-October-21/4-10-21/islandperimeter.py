class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 4
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx = i+dx
                        ny = j+dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            count -= 1
                    perimeter += count
        return perimeter
