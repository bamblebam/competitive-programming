class Solution:
    def myAtoi(self, s: str) -> int:
        min_=-2**31
        max_=2**31-1
        x=""
        s=s.strip()
        first=False
        sign=False
        num=False
        for i in range(len(s)):
            
            if i>0 and (s[i] in "-+" and s[i-1]=="0"):
                break
            
            if s[i] not in "1234567890-+":
                break
                
            if num and s[i] not in "1234567890":
                break
            
            if (s[i]=="-" or s[i]=="+") and not sign:
                x+=s[i]
                sign=True
            elif (s[i]=="-" or s[i]=="+") and sign:
                break
            
            if s[i]=="0" and not first:
                continue
            
            if s[i] in "1234567890":
                x+=s[i]
                sign=True
                first=True
                num=True
                
        if not x or x=="-" or x=="+":
            return 0
        x=int(x)
        if x<0:
            return max(min_,x)
        if x>0:
            return min(max_,x)