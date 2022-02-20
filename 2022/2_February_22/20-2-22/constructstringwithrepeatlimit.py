class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count=Counter(s)
        count=list(sorted(count.items(),key=lambda x:x[0],reverse=True))
        ans=""
        while count:
            k,v=count[0]
            if v<=repeatLimit:
                ans+=k*v
                count.pop(0)
                continue
            if v>repeatLimit:
                ans+=k*repeatLimit
                count[0]=(count[0][0],count[0][1]-repeatLimit)
                if len(count)<=1:
                    break
                nk,nv=count[1]
                ans+=nk
                nv-=1
                if nv==0:
                    count.pop(1)
                else:
                    count[1]=(count[1][0],count[1][1]-1)
        
        return ans
                