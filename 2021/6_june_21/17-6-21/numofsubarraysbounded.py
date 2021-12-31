class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        ans = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if left <= num <= right:
                l, r = i, i
                while l >= 0 and (l-1) >= 0 and nums[l-1] < num:
                    l -= 1
                while r < n and (r+1) < n and nums[r+1] <= num:
                    r += 1
                left_el, right_el = i-l, r-i
                temp = 1+left_el+right_el+left_el*right_el
                print(i, l, r, left_el, right_el, temp)
                ans += temp
        return ans
