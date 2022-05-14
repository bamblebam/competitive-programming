class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans=set()
        temp=list()
        ctr=0
        start=0
        for num in nums:
            if not num%p:
                ctr+=1
            while temp and ctr>k:
                x=temp.pop(0)
                if not x%p:
                    ctr-=1
            temp.append(num)
            n=len(temp)
            for i in range(n-1,-1,-1):
                ans.add(tuple(temp[i:]))

        return len(ans)