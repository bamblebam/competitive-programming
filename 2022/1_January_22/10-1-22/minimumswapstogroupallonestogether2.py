class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #use sliding window to go over the array
        #the size of the window is the number of ones in the array.
        #the max number of ones in the window - total number of ones is the number of swaps that are required
        #for swapping problems try sliding window
        n=len(nums)
        ones=nums.count(1)
        nums=nums+nums
        prefix=[0]
        ans=0
        for num in nums:
            prefix.append(prefix[-1]+num)
        for i in range(n):
            ans=max(ans,prefix[i+ones]-prefix[i])
        return ones-ans