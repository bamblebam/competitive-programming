class Solution:
    def twoSum(self, nums, target: int):
        nums_set = set(nums)
        for i, num in enumerate(nums):
            if target-num in nums_set and i != nums.index(target-num):
                return [i, nums.index(target-num)]
