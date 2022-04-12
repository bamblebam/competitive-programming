class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        First, we prepare the prefix sum array, so that we can compute subarray sums in O(1). Then, we move the boundary of the first subarray left to right. This is the first pointer - i.

For each point i, we find the minimum (j) and maximum (k) boundaries of the second subarray:

nums[j] >= 2 * nums[i]
nums[sz - 1] - nums[k] >= nums[k] - nums[i]
Note that in the code and examples below, k points to the element after the second array. In other words, it marks the start of the (shortest) third subarray. This makes the logic a bit simpler.

With these conditions, sum(0, i) <= sum(i + 1, j), and sum(i + 1, k - 1) < sum(k, n). Therefore, for a point i, we can build k - j subarrays satisfying the problem requirements.

Final thing is to realize that j and k will only move forward, which result in a linear-time solution.

for each i check whether the min sum of second arr is greater then max of 1st and min sum of 3rd arr is greater than max of 2nd
        """
        n,res,j,k=len(nums),0,0,0
        mod=10**9+7
        nums=list(accumulate(nums))
        for i in range(n-2):
            while j<=i or (j<n-1 and nums[j]-nums[i]<nums[i]):
                j+=1
            while k<j or (k<n-1 and nums[k]-nums[i]<=nums[-1]-nums[k]):
                k+=1
            res+=k-j
            res%=mod
        return res