import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


sol = Solution()
print(sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
