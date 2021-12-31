import itertools


class Solution:
    def jump(self, nums) -> int:
        d = list(itertools.accumulate(
            [i+num for i, num in enumerate(nums)], max))
        index, count = 0, 0
        while index < len(nums)-1:
            index = d[index]
            count += 1
        return count

# alternate Solution
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n=len(nums)
#         nums[-1]=0
#         for i in range(n-2,-1,-1):
#             val=nums[i]
#             if val==0:
#                 nums[i]=float('inf')
#             else:
#                 nums[i]=min(nums[i:i+val+1])+1 if i==n-2 else min(nums[i+1:i+val+1])+1
#         return nums[0]