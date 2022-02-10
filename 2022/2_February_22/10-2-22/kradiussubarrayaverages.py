class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if k>n//2:
            return [-1]*n
        count=0
        ans=list()
        for i in range(n):
            count+=nums[i]
            if i>=2*k:
                ans.append(count//(2*k+1))
                count-=nums[i-2*k]
        ans=[-1]*k+ans+[-1]*k
        return ans
            