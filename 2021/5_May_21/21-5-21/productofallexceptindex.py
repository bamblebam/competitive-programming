class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        dpb, dpa = [1]*n, [1]*n
        for i in range(1, n):
            dpb[i] = dpb[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            dpa[i] = dpa[i+1]*nums[i+1]
        return [a*b for a, b in zip(dpa, dpb)]


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
