class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums=Counter(nums)
        ans=list()
        for num in nums:
            if nums[num]==1 and nums[num-1]==0 and nums[num+1]==0:
                ans.append(num)
        return ans