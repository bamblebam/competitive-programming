class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        #left and right are used to store the amount of plates that are to the left or right of a candle
        #prefix is the prefix sum where it is the number of plates till that idx
        #can also be done in nlogn time with bisect
        n=len(s)
        left=[-1]*n
        right=[-1]*n
        prefix=[0]
        
        #calculate the candle idx to the left
        for i in range(n):
            if s[i]=="|":
                left[i]=i
            else:
                if i>0:
                    left[i]=left[i-1]
        
        #calculate the candle idx to the right
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                right[i]=i
            else:
                if i<n-1:
                    right[i]=right[i+1]
        
        #calculate prefix sum of plates
        for i in range(n):
            if s[i]=="*":
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])
        
        #calculate ans for queries
        ans=list()
        for l,r in queries:
            r=left[r] #candle idx before the candle closest to r on left side
            l=right[l] #candle idx after the candle closest to l on right side
            if l>r:
                ans.append(0)
            else:
                ans.append(prefix[r+1]-prefix[l]) #normal prefix sum calc
        
        for i in range(len(ans)):
            if ans[i]<0:
                ans[i]=0
        
        return ans