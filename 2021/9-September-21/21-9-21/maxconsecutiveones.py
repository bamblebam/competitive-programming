class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        temp = 0
        for i in range(n):
            if i == 0 and nums[i] == 1:
                temp += 1
            elif nums[i] == 1 and nums[i] == nums[i-1]:
                temp += 1
            elif nums[i] == 1:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(temp, ans)
        return ans
