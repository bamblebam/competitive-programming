class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix=list(accumulate(nums))
        n=len(nums)
        ans=0
        for i in range(n-1):
            if prefix[i]>=prefix[-1]-prefix[i]:
                ans+=1
        return ans