from collections import Counter

class Solution:
    def minSetSize(self, arr) -> int:
        count=Counter(arr)
        count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        n=len(arr)
        m=n/2
        ans=0
        while m>0:
            item=count.pop(0)
            ans+=1
            m-=item[1]
        return ans
            
        