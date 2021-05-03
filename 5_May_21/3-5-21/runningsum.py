import itertools


class Solution:
    def runningSum(self, nums):
        return list(itertools.accumulate(nums))
