class Solution:
    def triangleNumber(self, nums) -> int:
        nums, ans, n = sorted(nums), 0, len(nums)
        for i in range(2, n):
            left, right = 0, i-1
            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    ans += right-left
                    right -= 1
                else:
                    left += 1
        return ans
