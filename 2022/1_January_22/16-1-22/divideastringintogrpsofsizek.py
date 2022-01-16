class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=list()
        n=len(s)
        for i in range(0,n,k):
            x=s[i:i+k]
            if len(x)<k:
                x+=fill*(k-len(x))
            ans.append(x)
        return ans