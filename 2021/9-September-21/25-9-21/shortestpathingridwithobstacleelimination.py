class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, 0, k)])
        seen = set()
        if k >= m+n-2:
            return m+n-2
        while queue:
            steps, x, y, k = queue.popleft()
            if x == m-1 and y == n-1:
                return steps
            for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                if 0 <= nx < m and 0 <= ny < n and k-grid[nx][ny] >= 0 and (nx, ny, k-grid[nx][ny]) not in seen:
                    queue.append((steps+1, nx, ny, k-grid[nx][ny]))
                    seen.add((nx, ny, k-grid[nx][ny]))
        return -1
