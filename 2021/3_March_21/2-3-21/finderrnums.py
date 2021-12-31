class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        missing, double = 0, 0
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    double = nums[i]
            if i+1 not in nums:
                missing = i+1
        return [double, missing]


sol = Solution()
print(sol.findErrorNums([2, 2, 1]))
