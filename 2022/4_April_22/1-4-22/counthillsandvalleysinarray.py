class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        x=[i for i,j in list(groupby(nums))]
        n=len(x)
        ans=0
        for i in range(1,n-1):
            if (x[i]<x[i-1] and x[i]<x[i+1]) or (x[i]>x[i-1] and x[i]>x[i+1]):
                ans+=1
        return ans