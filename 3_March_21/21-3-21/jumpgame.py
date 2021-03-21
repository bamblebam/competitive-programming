class Solution:
    def canJump(self, nums) -> bool:
        good_index = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]+i >= good_index:
                good_index = i
        return good_index == 0
