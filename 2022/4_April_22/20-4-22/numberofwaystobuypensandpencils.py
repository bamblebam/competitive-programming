class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans=0
        num_pens=total//cost1
        for i in range(num_pens+1):
            x=total-i*cost1
            num_pencils=x//cost2
            ans+=num_pencils+1
        return ans