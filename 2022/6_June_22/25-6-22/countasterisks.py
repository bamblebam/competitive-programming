class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        ans=0
        for c in s:
            if c=="|":
                count+=1
            if c=="*" and count%2==0:
                ans+=1
        return ans