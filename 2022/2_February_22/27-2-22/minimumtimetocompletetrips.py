class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        use binary search on the amount of time required to complete totalTrips
        in binary search if ans is greater than required r becomes mid
        if less l becomes mid+1
        l always less than r l<r
        '''
        def helper(x):
            ans=0
            for i in time:
                ans+=x//i
            return ans
        
        l,r=1,min(time)*totalTrips
        while l<r:
            mid=(l+r)//2
            x=helper(mid)
            if x>=totalTrips:
                r=mid
            else:
                l=mid+1
        return l