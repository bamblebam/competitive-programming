class Solution:
    def minMoves2(self, nums) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(nums), sorted(nums)[::-1]))//2
