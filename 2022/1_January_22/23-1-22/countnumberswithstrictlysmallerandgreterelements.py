class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        l,r=nums[0],nums[-1]
        count=0
        for num in nums:
            if l<num<r:
                count+=1
        return count