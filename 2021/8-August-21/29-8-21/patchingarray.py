class Solution:
    def minPatches(self, nums, n: int) -> int:
        count, mx, idx = 0, 0, 0
        # while the max reach (mx) is less than the target (n) just check if the next num in nums is smaller than          the current reach if yes then update the reach and idx else update the ans
        while mx < n:
            if idx < len(nums) and nums[idx] <= mx+1:
                mx += nums[idx]
                idx += 1
            else:
                count += 1
                mx = 2*mx+1
        return count
