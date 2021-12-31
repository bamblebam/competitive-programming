class Solution:
    def maxPower(self, s: str) -> int:
        ans=0
        count=1
        n=len(s)
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                ans=max(ans,count)
                count=1
        ans=max(ans,count)
        return ans