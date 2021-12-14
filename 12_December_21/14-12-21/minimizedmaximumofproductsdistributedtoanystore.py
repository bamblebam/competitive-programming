class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        #use binary search to get the number of stores needed for a particular amount of candies
        l,r=1,max(quantities)
        
        def helper(x):
            count=0
            for i in quantities:
                count+=(i+x-1)//x
            return count<=n
        
        while l<r:
            mid=(l+r)//2
            if helper(mid):
                r=mid
            else:
                l=mid+1
        
        return l