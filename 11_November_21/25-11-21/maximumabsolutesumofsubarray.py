class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #2 times kadanes algorithm. First to find the largest +ve sum, second to find largest minimum sum
        n=len(nums)
        sum1=mx1=0
        for i in range(n):
            sum1+=nums[i]
            sum1=max(0,sum1)
            mx1=max(mx1,sum1)
        sum2=mx2=0
        for i in range(n):
            sum2+=nums[i]
            sum2=min(sum2,0)
            mx2=min(mx2,sum2)
        return max(mx1,abs(mx2))