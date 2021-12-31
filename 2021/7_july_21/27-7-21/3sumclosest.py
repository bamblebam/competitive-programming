class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        for i in range(n):
            low, high = i+1, n-1
            while low < high:
                sum_ = nums[i]+nums[low]+nums[high]
                if abs(target-sum_) < abs(diff):
                    diff = target-sum_
                if sum_ > target:
                    high -= 1
                elif sum_ < target:
                    low += 1
                if diff == 0:
                    break
        return target-diff
