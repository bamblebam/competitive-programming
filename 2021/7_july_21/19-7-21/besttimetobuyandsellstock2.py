class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1]-prices[i]
        return profit

#alternate solution
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         #use peak and value to discover the smaleest element first then greatest and so on
#         ans=0
#         n=len(prices)
#         peak=0
#         valley=prices[0]
#         i=1
#         while i<n:
#             while i<n and prices[i-1]>=prices[i]:
#                 valley=prices[i]
#                 i+=1
#             while i<n and prices[i-1]<prices[i]:
#                 peak=prices[i]
#                 i+=1
#             if peak>valley:
#                 ans+=peak-valley
#             peak=valley=0
#         return ans