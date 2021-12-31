class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for _ in range(m)]
        # go through the entire grid and add them to the dp matrix if element is at top row only left side will contribute if at 1st col only top will. else choose the min route from top or left.
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0 and j!=0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif i!=0 and j==0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        print(dp)
        return dp[m-1][n-1]