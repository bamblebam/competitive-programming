class Solution:
    def longestOnes(self, nums, k: int) -> int:
        n=len(nums)
        ans=min(k,n)
        left,right=0,0
        count=0
        while right<n:
            if nums[right]==0:
                count+=1
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            ans=max(ans,right-left+1)
            right+=1
        return ans
            
                