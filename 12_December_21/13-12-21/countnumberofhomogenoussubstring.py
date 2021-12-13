class Solution:
    def countHomogenous(self, s: str) -> int:
        n=len(s)
        mod=10**9+7
        ans=0
        count=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                ans+=count*(count+1)/2
                count=1
        ans+=count*(count+1)/2
        return int(ans)%mod