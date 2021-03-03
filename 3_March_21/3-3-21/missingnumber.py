class Solution:
    def missingNumber(self, nums) -> int:
        length = len(nums)
        original, given = (length+1)*length/2, sum(nums)
        return int(original-given)


sol = Solution()
print(sol.missingNumber([]))
