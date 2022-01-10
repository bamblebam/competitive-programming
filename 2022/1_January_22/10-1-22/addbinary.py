class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        if len(b)<len(a):
            a,b=b,a
        ans=""
        a=a[::-1]
        b=b[::-1]
        for i in range(len(b)):
            num1=int(b[i])
            num2=0
            if i<len(a):
                num2=int(a[i])
            x=0
            t=num1+num2+carry
            if t==2:
                x=0
                carry=1
            elif t==3:
                x=1
                carry=1
            elif t==1:
                x=1
                carry=0
            elif t==0:
                x=0
                carry=0
            ans+=str(x)
        if carry==1:
            ans+=str(carry)
        return ans[::-1]