import heapq


class Solution:
    def swimInWater(self, grid) -> int:
        n, h, vis, ans = len(grid), [(grid[0][0], 0, 0)], set((0, 0)), 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(n*n):
            val, x, y = heapq.heappop(h)
            ans = max(ans, val)
            if x == n-1 and y == n-1:
                return ans
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vis:
                    heapq.heappush(h, (grid[nx][ny], nx, ny))
                    vis.add((nx, ny))
        return ans+1
