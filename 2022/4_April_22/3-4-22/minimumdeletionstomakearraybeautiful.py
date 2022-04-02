class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        """
        complex math stuff
        i+ans keeps track wherther the curr num is at even or odd idx after removal of other nums
        """
        n=len(nums)
        ans=0
        for i in range(n):
            if (i+ans)%2==0:
                if i+1<n and nums[i]==nums[i+1]:
                    ans+=1
        if (n-ans)%2:
            ans+=1
        return ans