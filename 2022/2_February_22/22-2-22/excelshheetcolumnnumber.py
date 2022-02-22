class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        vals={x:i+1 for i,x in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        ans=0
        columnTitle=columnTitle[::-1]
        for i,x in enumerate(columnTitle):
            ans+=vals[x]*26**i
        return ans