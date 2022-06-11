class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        indices=dict()
        n=len(s)
        
        i=0
        for j in range(n):
            if s[j] in indices:
                i=max(i,indices[s[j]])
            ans=max(ans,j-i+1)
            indices[s[j]]=j+1
        
        return ans
                
        