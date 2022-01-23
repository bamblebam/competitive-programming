class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod=10**9+7
        indices=[i for i,c in enumerate(corridor) if c=="S"]
        m=len(indices)
        if m<2 or m%2:
            return 0
        ans=1
        for i in range(m//2-1):
            ans*=(indices[2*i+2]-indices[2*i+1])
        return ans%mod
                