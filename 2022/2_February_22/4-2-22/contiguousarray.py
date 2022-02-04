class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        keep curr variable to stroe the diff between the 1s and 0s
        whenever you encounter a curr val for the first time put it in a dict with the idx
        dont update it as we need the earliest possible value
        when we get the same val of curr we use the dict to find the last idx where we got it and that is our ans
        '''
        ans=0
        seen={0:-1}
        curr=0
        for i,x in enumerate(nums):
            if x==1:
                curr+=1
            else:
                curr-=1
            if curr in seen:
                ans=max(ans,i-seen[curr])
            else:
                seen[curr]=i
        return ans