class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        l,r=0,n-1
        s=list(s)
        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
        return "".join(s)
            