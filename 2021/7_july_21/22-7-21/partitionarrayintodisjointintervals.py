class Solution:
    def partitionDisjoint(self, nums) -> int:
        n=len(nums)
        arr=reversed(nums)
        left_max=[nums[0]]+[0]*(n-1)
        right_min=[float('inf')]*(n-1)+[nums[-1]]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],nums[i])
        for i in range(n-2,-1,-1):
            right_min[i]=min(right_min[i+1],nums[i])
        for i in range(1,n):
            if left_max[i-1]<=right_min[i]:
                return i
        