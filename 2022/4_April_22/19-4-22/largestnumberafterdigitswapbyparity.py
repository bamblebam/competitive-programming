class Solution:
    def largestInteger(self, num: int) -> int:
        num=str(num)
        indices=dict()
        ans=''
        e,o=list(),list()
        for i,c in enumerate(num):
            indices[i]=int(c)%2
            if int(c)%2:
                heappush(o,-int(c))
            else:
                heappush(e,-int(c))
        for i in range(len(num)):
            if indices[i]:
                ans+=str(-heappop(o))
            else:
                ans+=str(-heappop(e))
        return ans
            