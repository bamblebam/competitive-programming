class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            pos = nums[i]-1
            while 0 < nums[i] <= n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos = nums[i]-1
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
