class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans=list()
        col_start,row_start,col_end,row_end=s[0],s[1],s[3],s[4]
        for i in range(ord(col_start),ord(col_end)+1):
            x=chr(i)
            for j in range(int(row_start),int(row_end)+1):
                ans.append(x+str(j))
        return ans