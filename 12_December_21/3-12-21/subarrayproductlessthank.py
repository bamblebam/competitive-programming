class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #use sliding window
        n=len(nums)
        if k<=1:
            return 0
        l=0
        prod=1
        ans=0
        for r,num in enumerate(nums):
            prod*=num
            while prod>=k:
                prod/=nums[l]
                l+=1
            ans+=r-l+1
        return ans
