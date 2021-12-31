class Solution:
    def numTilings(self, n: int) -> int:
        #use dp to calculate the last 3 states
        #can also be solved using matrix exponation
        mod=10**9+7
        fcurr=2
        fprev=1
        pcurr=1
        
        if n<3:
            return n
        
        for i in range(3,n+1):
            temp=fcurr
            fcurr=(fprev+fcurr+2*pcurr)%mod
            pcurr=(fprev+pcurr)%mod
            fprev=temp
        
        return fcurr