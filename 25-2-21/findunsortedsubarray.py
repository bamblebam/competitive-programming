import sys


class Solution:
    def findUnsortedSubarray(self, nums):
        l, r, min, max, start, end = 0, len(
            nums)-1, sys.maxsize, -sys.maxsize, 0, -1
        while r >= 0:
            if max <= nums[l]:
                max = nums[l]
            else:
                end = l
            if min >= nums[r]:
                min = nums[r]
            else:
                start = r
            l += 1
            r -= 1
        return end-start+1


sol = Solution()
print(sol.findUnsortedSubarray([1, 2]))
