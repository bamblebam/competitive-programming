class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        ans = maxval = minval = nums[0]
        for num in nums[1:]:
            maxval, minval = max(num, maxval*num, minval *
                                 num), min(num, maxval*num, minval*num)
            ans = max(ans, maxval)
        return ans
