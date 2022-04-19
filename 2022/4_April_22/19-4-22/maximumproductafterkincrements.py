class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        h=list()
        for num in nums:
            heappush(h,num)
        while k!=0:
            x=heappop(h)
            heappush(h,x+1)
            k-=1
        ans=1
        mod=10**9+7
        for num in h:
            ans*=num
            ans%=mod
        return ans