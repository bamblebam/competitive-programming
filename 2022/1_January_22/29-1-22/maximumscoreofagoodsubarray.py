class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def helper(nums,k):
            left=list(accumulate(nums[:k+1][::-1],min))[::-1]
            right=list(accumulate(nums[k:],min))
            ans=0
            for j in range(len(right)):
                i=bisect_left(left,right[j])
                ans=max(ans,(j-i+k+1)*right[j])
            return ans
        return max(helper(nums,k),helper(nums[::-1],n-k-1))