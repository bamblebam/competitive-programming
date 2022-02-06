class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        digits=list()
        num2=abs(num)
        while num2>0:
            digits.append(num2%10)
            num2//=10
        ans=""
        zeroes=0
        if num>0:
            flag=False
            digits.sort(reverse=True)
            while digits:
                x=digits.pop()
                if x==0:
                    zeroes+=1
                if x!=0 and not flag:
                    ans+=str(x)
                    ans+="0"*zeroes
                    flag=True
                elif x!=0 and flag:
                    ans+=str(x)
        else:
            digits.sort(reverse=True)
            ans="".join(list(map(str,digits)))
            ans=int(ans)*-1
        
        return int(ans)
                