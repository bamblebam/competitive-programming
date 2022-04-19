from sortedcontainers import SortedList

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        use binary search to determine the maximum num of candies each child can get
        find mid and use that to find the number of piles any pile can be divided into
        if the num is less than k reduce mid else increase it
        """
        l,r=1,max(candies)
        ans=0
        while l<=r:
            mid=(l+r)//2
            c=sum(x//mid for x in candies)
            if c>=k:
                l=mid+1
                ans=max(ans,mid)
            else:
                r=mid-1
        return ans