class Solution:
    def coinChange(self, coins, amount):
        dp = [0]+[float("inf")]*(amount+1)
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1


sol = Solution()
print(sol.coinChange(coins=[186, 419, 83, 408], amount=6249))
