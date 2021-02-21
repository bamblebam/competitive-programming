import sys


class Solution:
    def increasingTriplet(self, nums):
        limit1 = sys.maxsize
        limit2 = sys.maxsize
        for num in nums:
            if num <= limit1:
                limit1 = num
            elif num <= limit2:
                limit2 = num
            else:
                return True
        return False


sol = Solution()
print(sol.increasingTriplet([5, 4, 3, 2, 1]))
