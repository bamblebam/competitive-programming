class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        ref=Counter(p)
        count=Counter()
        ans=list()
        for i in range(n):
            if i>=m:
                if ref==count:
                    ans.append(i-m)
                count[s[i-m]]-=1
            count[s[i]]+=1
        if count==ref:
            ans.append(i-m+1)
        return ans