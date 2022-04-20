class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans=float("-inf")
        diff=float('inf')
        for num in nums:
            x=abs(0-num)
            if x<diff:
                ans=num
                diff=x
            elif x==diff:
                ans=max(ans,num)
        return ans