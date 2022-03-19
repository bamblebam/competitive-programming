class Solution:
    def halveArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        h=list()
        for num in nums:
            heappush(h,-num)
        total=sum(nums)
        half=total/2
        ans=0
        while total>half:
            x=-heappop(h)
            num=x/2
            total-=num
            heappush(h,-num)
            ans+=1
        return ans