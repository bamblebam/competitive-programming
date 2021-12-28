class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m=len(s)
        ans=[0]*m
        r,c=startPos
        count=0
        for i in range(m):
            if i:
                ans[i-1]=count
            count=0
            r,c=startPos
            for j in range(i,m):
                if s[j]=="U":
                    r-=1
                elif s[j]=="D":
                    r+=1
                elif s[j]=="L":
                    c-=1
                else:
                    c+=1
                    
                if 0<=r<n and 0<=c<n:
                    count+=1
                else:
                    break
        ans[-1]=count
        return ans
            