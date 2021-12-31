class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #Let us now sort our numbers and in sol[i] list keep the best solution, where the biggest number is equal to nums[i]. How can we find it? Look at all smaller numbers and if nums[i] is divisible by this smaller number, we can update solution. Let us go through example: nums = [4,5,8,12,16,20].

    # sol[0] = [4], the biggest divisible subset has size 1.
    # sol[1] = [5], because 5 % 4 != 0.
    # sol[2] = [4,8], because 8 % 4 = 0.
    # sol[3] = [4,12], because 12 % 4 = 0.
    # sol[4] = [4,8,16], because 16 % 8 = 0 and 16 % 4 = 0 and we choose 8, because it has longer set.
    # sol[5] = [4,20] (or [5,20] in fact, but it does not matter). We take [4,20], because it has the biggest length and when we see 5, we do not update it.
    # Finally, answer is [4,8,16].
        n=len(nums)
        nums.sort() #sort the nums because if sorted the smaller ones will always be divisible by the bigger one
        ans=[[num] for num in nums]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(ans[i])<len(ans[j])+1: #if the smaller num divides the bigger num and the len of the smaller num array is bigger than the bigger num array replace the bigger num array
                    ans[i]=ans[j]+[nums[i]]
        return max(ans,key=len)