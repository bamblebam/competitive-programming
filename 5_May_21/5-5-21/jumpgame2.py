import itertools


class Solution:
    def jump(self, nums) -> int:
        d = list(itertools.accumulate(
            [i+num for i, num in enumerate(nums)], max))
        index, count = 0, 0
        while index < len(nums)-1:
            index = d[index]
            count += 1
        return count
