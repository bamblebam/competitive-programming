class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #use binary search
        #before the single element all elements will have 1st one at even idx after single element they will have first one at odd idx
        #so if 1st elem is at even idx the single elem is to the right of it so update left else update right since the elem is at the left
        n=len(nums)
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            nei=mid-1 if mid%2 else mid+1
            if nums[mid]==nums[nei]:
                l=mid+1
            else:
                r=mid
        return nums[l]