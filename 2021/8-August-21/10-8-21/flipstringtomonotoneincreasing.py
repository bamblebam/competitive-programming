class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        flips=0
        ones=s.count("1")
        ans=ones
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                flips+=1
            else:
                ones-=1
            ans=min(ones+flips,ans)
        return ans