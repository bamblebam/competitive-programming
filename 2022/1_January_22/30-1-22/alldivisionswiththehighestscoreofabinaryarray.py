class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        left=[0]
        for i in range(n):
            if nums[i]==0:
                left.append(left[-1]+1)
            else:
                left.append(left[-1])

        right=[0]
        for i in range(n-1,-1,-1):
            if nums[i]==1:
                right.append(right[-1]+1)
            else:
                right.append(right[-1])
        right=right[::-1]
        
        ans=list()
        mx=0
        for i in range(n+1):
            x=left[i]+right[i]
            if x>mx:
                mx=x
                ans=[i]
            elif x==mx:
                ans.append(i)
        
        return ans