class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        #this is basically longest increasing subsequence problem
        #split the arr into k smaller arrays like 0,k,2k and 1,k+1,2k+1, and so on
        #find the length of the longest common subsequence
        #those many elements are already in place only the remaining need to be changed, so do that
        #the sum of all those arrs is the ans
        def helper(nums):
            n=len(nums)
            best=list()
            for num in nums:
                idx=bisect_left(best,num+1)
                if idx>=len(best):
                    best.append(num)
                else:
                    best[idx]=num
            return n-len(best)
        
        ans=0
        for i in range(k):
            ans+=helper(arr[i::k])
        
        return ans