class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #simple binary search
        n=len(nums)
        l,r=0,n
        while l<r:
            mid=(l+r)//2
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid
        return l