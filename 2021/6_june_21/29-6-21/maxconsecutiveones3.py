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
            
# #alternate solution
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         ans=0
#         l,r=0,0
#         while r<n:
#             if nums[r]==1:
#                 r+=1
#                 ans=max(r-l,ans)
#             elif nums[r]==0 and k>0:
#                 r+=1
#                 k-=1
#                 ans=max(r-l,ans)
#             elif nums[r]==0:
#                 while k<=0:
#                     if nums[l]==0:
#                         k+=1
#                     l+=1
#                 ans=max(r-l,ans)
#         ans=max(r-l,ans)
#         return ans
                