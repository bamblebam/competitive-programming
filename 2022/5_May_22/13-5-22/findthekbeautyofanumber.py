class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        s=str(num)
        subs=[s[i:i+k] for i in range(len(s)-k+1)]
        for sub in subs:
            if int(sub)!=0 and num%int(sub)==0:
                ans+=1
        return ans
            