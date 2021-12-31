class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = float('inf')
        r1_sum = [0]
        r2_sum = [0]
        for i in range(n):
            r1_sum.append(r1_sum[-1]+grid[0][i])
            r2_sum.append(r2_sum[-1]+grid[1][i])
        r1_sum = r1_sum[1:]
        # getting optimal path for robos
        for i in range(n):
            r2 = max(r1_sum[n-1]-r1_sum[i], r2_sum[i])
            ans = min(r2, ans)
        return ans
