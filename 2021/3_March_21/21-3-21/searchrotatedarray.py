class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while(left < right):
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        start, right = left, len(nums)-1
        if nums[start] <= target and nums[right] >= target:
            left = start
        else:
            right = start
            left = 0
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1
