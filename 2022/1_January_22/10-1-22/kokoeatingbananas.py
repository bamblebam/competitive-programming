class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use binary search on k
        #try to check whether this many bananas can be eaten in h hours if limit is k
        def helper(x):
            count=0
            for bananas in piles:
                if x>=bananas:
                    count+=1
                else:
                    if bananas%x!=0:
                        count+=bananas//x + 1
                    else:
                        count+=bananas//x
            return count<=h
        
        l,r=0,max(piles)
        while l<=r:
            mid=(l+r)//2
            if mid==0:
                return 1
            if helper(mid):
                r=mid-1
            else:
                l=mid+1
        
        return l