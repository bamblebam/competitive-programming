class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        profit = 0
        minprice = float('inf')
        for i in range(n):
            minprice = min(minprice, prices[i])
            profit = max(profit, prices[i]-minprice)
        return profit
