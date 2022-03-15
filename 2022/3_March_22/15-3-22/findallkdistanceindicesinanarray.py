class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        2 pointer for O(n) TC
        """
        n=len(nums)
        l,r=0,0
        count=0
        ans=list()
        while r<k+1 and r<n:
            if nums[r]==key:
                count+=1
            r+=1
        while l<n:
            if count>0:
                ans.append(l)
            if l-k>=0 and nums[l-k]==key:
                count-=1
            if r<n and nums[r]==key:
                count+=1
            l+=1
            r+=1
        return ans