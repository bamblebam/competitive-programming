class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, 1
        while l < n:
            if l % 2 == nums[l] % 2:
                l += 1
                continue
            r = l+1
            parity = 0
            if l % 2:
                parity = 1
            else:
                parity = -1
            while r < n:
                if parity == 1 and not r % 2 and nums[r] % 2:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    break
                elif parity == -1 and r % 2 and not nums[r] % 2:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    break
                r += 1
        return nums
