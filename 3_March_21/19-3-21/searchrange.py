class Solution:
    def searchRange(self, nums, target: int):
        l, r = 0, len(nums)-1
        count = 0
        while(l <= r and count < 17):
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
            else:
                start, end = mid, mid
                while(start >= 0 and nums[start] == nums[mid]):
                    start -= 1
                while(end < len(nums) and nums[end] == nums[mid]):
                    end += 1
                return [start+1, end-1]
            count += 1
        return [-1, -1]


sol = Solution()
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
