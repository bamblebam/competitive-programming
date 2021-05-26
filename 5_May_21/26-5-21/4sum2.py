from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        dp = defaultdict(lambda: 0)
        ans = 0
        for c in nums3:
            for d in nums4:
                e = c+d
                dp[e] += 1
        for b in nums2:
            for a in nums1:
                f = a+b
                ans += dp[-f]
        return ans
