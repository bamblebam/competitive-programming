class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustsnobody=set(range(1,n+1))
        trustedbyeverybody={k:0 for k in range(1,n+1)}
        
        for a,b in trust:
            if a in trustsnobody:
                trustsnobody.remove(a)
            trustedbyeverybody[b]+=1
        
        trustedbyeverybody={k for k in trustedbyeverybody.keys() if trustedbyeverybody[k]==n-1}
        
        ans=list(trustsnobody.intersection(trustedbyeverybody))
        if ans:
            return ans[0]
        return -1