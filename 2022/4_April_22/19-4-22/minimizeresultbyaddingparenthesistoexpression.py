class Solution:
    def minimizeResult(self, s: str) -> str:
        n=len(s)
        best=float('inf')
        ans=""
        idx=s.index('+')
        for i in range(idx):
            for j in range(idx+2,n+1):
                x=eval("("+s[i:j]+")")
                if s[:i]:
                    x*=int(s[:i])
                if s[j:]:
                    x*=int(s[j:]) 
                if x<best:
                    ans=s[:i]+"("+s[i:j]+")"+s[j:]
                    best=x
        return ans