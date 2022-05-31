class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        """
        use prefix and suffix arrays to keep track of the sides of the mountains
        """
        n=len(nums)
        suf=[0]*n
        pre=[0]*n
        
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                pre[i]=1+pre[i-1]
        
        nums.reverse()
        
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                suf[i]=1+suf[i-1]
        
        suf.reverse()
        
        ans=0
        for a,b in zip(pre,suf):
            if a==0 or b==0:
                continue
            ans=max(ans,a+b+1)
        
        return ans