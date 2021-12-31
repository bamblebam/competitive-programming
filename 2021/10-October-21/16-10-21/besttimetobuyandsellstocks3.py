import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #take the different valley and peak pairs and add them to the heap.
        # #take the largest 2 gaps in case of 2 transactions, if k transactions take k gaps
        # diffs=list()
        # i=0
        # n=len(prices)
        # peak,valley=prices[0],prices[0]
        # while i<n-1:
        #     while i<n-1 and prices[i]>=prices[i+1]:
        #         i+=1
        #     valley=prices[i]
        #     while i<n-1 and prices[i]<=prices[i+1]:
        #         i+=1
        #     peak=prices[i]
        #     heapq.heappush(diffs,-(peak-valley))
        # if len(diffs)>2:
        #     a1=-heapq.heappop(diffs)
        #     a2=-heapq.heappop(diffs)
        #     return a1+a2
        # else:
        #     return -sum(diffs)
        
        #method-2 (dp)
        diffs=[prices[i+1]-prices[i] for i in range(len(prices)-1)]
        diffs=[sum(x) for _,x in groupby(diffs,key=lambda x:x<0)]
        n=len(diffs)+1 #number of buy/sell points in the array
        k=2 #number of transactions
        
        if k>len(prices)//2:
            return sum(x for x in diffs if x>0)
        
        dp=[[0]*(k+1) for _ in range(n-1)]
        mp=[[0]*(k+1) for _ in range(n-1)]
        
        dp[0][1],mp[0][1]=diffs[0],diffs[0]
        
        for i in range(1,n-1):
            for j in range(1,k+1):
                dp[i][j]=max(dp[i-1][j],mp[i-1][j-1])+diffs[i]
                mp[i][j]=max(dp[i][j],mp[i-1][j])
        
        return max(mp[-1])

#         if len(prices) <= 1: return 0
#         n, k = len(prices), 2

#         B = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
#         if k > len(prices)//2: return sum(x for x in B if x > 0)

#         dp = [[0]*(k+1) for _ in range(n-1)] 
#         mp = [[0]*(k+1) for _ in range(n-1)] 

#         dp[0][1], mp[0][1] = B[0], B[0]

#         for i in range(1, n-1):
#             for j in range(1, k+1):
#                 dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + B[i]
#                 mp[i][j] = max(dp[i][j], mp[i-1][j])

#         return max(mp[-1])