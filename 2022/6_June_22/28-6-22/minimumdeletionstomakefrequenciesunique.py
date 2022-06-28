class Solution:
    def minDeletions(self, s: str) -> int:
        count=[0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        count.sort(reverse=True)
        
        ans=0
        maxFreq=len(s)
        
        for freq in count:
            if freq>maxFreq:
                ans+=freq-maxFreq
                freq=maxFreq
            maxFreq=max(0,freq-1)
        
        return ans