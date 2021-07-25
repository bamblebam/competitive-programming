class Solution:
    def findIntegers(self, n: int) -> int:
        s=bin(n+1)[2:]
        n=len(s)
        dp=[1,2]+[0]*(n-2)
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
            
        ans,prev=0,0
        for i in range(n):
            if s[i]=='0':
                continue
            if prev==1:
                break
            if i>0 and s[i-1]=='1':
                prev=1
            ans+=dp[-i-1]
        return ans