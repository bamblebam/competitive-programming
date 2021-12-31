class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ans=0
        count=0
        for num in nums:
            if num==1:
                count+=1
                ans=max(count,ans)
            else:
                count=0
        return ans