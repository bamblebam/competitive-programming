class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=list()
        num1,num2=num1[::-1],num2[::-1]
        if len(num1)<len(num2):
            num1,num2=num2,num1
        n1,n2=len(num1),len(num2)
        carry=0
        for i in range(n2):
            x,y=int(num1[i]),int(num2[i])
            z=str(x+y+int(carry))
            carry=0
            add=z[-1]
            if len(z)>1:
                carry=z[0]
            ans.append(add)
        for i in range(n2,n1):
            x=int(num1[i])
            z=str(x+int(carry))
            carry=0
            add=z[-1]
            if len(z)>1:
                carry=z[0]
            ans.append(add)
        if carry:
            ans.append(str(carry))
        return "".join(reversed(ans))
            