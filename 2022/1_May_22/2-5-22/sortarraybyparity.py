class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        while l<r:
            if nums[l]%2 and not nums[r]%2:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            elif not nums[l]%2:
                l+=1
            elif nums[r]%2:
                r-=1
        return nums