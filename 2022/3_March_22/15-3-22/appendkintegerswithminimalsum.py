class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        m=nums[-1]
        s=nums[0]
        ans=0
        def helper(b,a):
            return a*(a+1)/2 - b*(b+1)/2
        if s!=1:
            x=s-1
            if k>=x:
                ans+=helper(0,x)
                k-=x
            else:
                ans+=helper(0,k)
                k=0
        if k==0:
            return int(ans)
        for i in range(1,n):
            x=nums[i]-nums[i-1]
            if x==0:
                continue
            if k>=x-1:
                ans+=helper(nums[i-1],nums[i]-1)
                k-=x-1
            else:
                ans+=helper(nums[i-1],k+nums[i-1])
                k=0
            if k==0:
                return int(ans)
        ans+=helper(m,k+m)
        return int(ans)
        