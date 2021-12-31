class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0:
            return 0
        if len(prices)<=1:
            return 0
        
        # list of all the different inflection points where a trade can actually take place
        diffs=[prices[i+1]-prices[i] for i in range(len(prices)-1)]
        diffs=[sum(x) for _,x in groupby(diffs,key=lambda x:x<0)]
        n=len(diffs)+1
        
        if k>len(prices)//2:
            return sum(x for x in diffs if x>0)
        
        #the dp arrays
        dp=[[0]*(k+1) for _ in range(n-1)]
        mp=[[0]*(k+1) for _ in range(n-1)]
        dp[0][1],mp[0][1]=diffs[0],diffs[0]
        
        for i in range(1,n-1):
            for j in range(1,k+1):
                dp[i][j]=max(mp[i-1][j-1],dp[i-1][j])+diffs[i] # dp[i-1][j] considers the same contiguous array whie mp[i-1][j-1] considers a new one
                mp[i][j]=max(mp[i-1][j],dp[i][j])
        
        return max(mp[-1])