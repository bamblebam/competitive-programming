class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        if n <= 1:
            return nums[0]
        if nums[right] > nums[0]:
            return nums[0]
        while right >= left:
            mid = (right+left)//2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid+1
            else:
                right = mid-1
