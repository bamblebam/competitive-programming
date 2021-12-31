from collections import Counter


class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        n = len(nums)
        total = 0
        left = right = 0
        d = Counter()
        ans = 0
        while right < n:
            d[nums[right]] += 1
            total += nums[right]
            while d[nums[right]] > 1:
                d[nums[left]] -= 1
                total -= nums[left]
                left += 1
            ans = max(ans, total)
            right += 1
        return ans
