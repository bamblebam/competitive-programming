class Solution:
    def sortColors(self, nums) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


sol = Solution()
print(sol.sortColors([2, 0, 2, 1, 1, 0]))
