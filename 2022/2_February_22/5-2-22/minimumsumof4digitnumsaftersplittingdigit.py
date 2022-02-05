class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        nums=[int(num[i]) for i in range(len(num)) if num[i]!=0]
        if len(nums)<=2:
            return sum(nums)
        nums.sort()
        return nums[0]*10+nums[3]+nums[1]*10+nums[2]