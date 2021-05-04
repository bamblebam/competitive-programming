class Solution:
    def checkPossibility(self, nums) -> bool:
        count = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if count != -1:
                    return False
                count = i-1
        return count in [-1, 0, n-2] or nums[count-1] <= nums[count+1] or nums[count] <= nums[count+2]
