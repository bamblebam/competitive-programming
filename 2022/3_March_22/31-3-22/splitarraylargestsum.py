class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        use binary search on the max sum
        use it to find the min sum where we can split the array into m parts
        """
        def helper(max_sum):
            curr=0
            splits=0
            for num in nums:
                if curr+num<=max_sum:
                    curr+=num
                else:
                    curr=num
                    splits+=1
            return splits+1
        
        l,r=max(nums),sum(nums)
        ans=0
        while l<=r:
            mid=(l+r)//2
            if helper(mid)<=m:
                r=mid-1
                ans=mid
            else:
                l=mid+1
        
        return ans