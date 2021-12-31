class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0]*(n+1)
        dp_max = [0]*(n+1)
        diff = [prices[i+1]-prices[i] for i in range(n-1)]
        for i in range(n-1):
            dp[i] = diff[i]+max(dp[i-1], dp_max[i-3])
            dp_max[i] = max(dp[i], dp_max[i-1])
        return dp_max[-3]
