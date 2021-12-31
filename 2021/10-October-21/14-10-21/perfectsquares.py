class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]
        while len(dp)<=n:
            x=float('inf')
            for i in range(1,int(len(dp)**0.5)+1):
                x=min(x,dp[len(dp)-i*i]+1)
            dp.append(x)
        return dp[-1]
