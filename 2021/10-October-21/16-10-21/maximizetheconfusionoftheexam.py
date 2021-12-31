class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # use sliding window twice to check for the number of T's and F's you can invert and use that to find the longest substring
        ans=0
        n=len(answerKey)
        m=k
        #converting F to T
        l,r=0,0
        count=0
        while r<n:
            # print(answerKey[r],count,m,l,r)
            if m<=0 and answerKey[r]=='F':
                if answerKey[l]=='F':
                    m+=1
                ans=max(ans,count)
                count-=1
                l+=1
            else:
                if answerKey[r]=='F' and m>0:
                    m-=1
                    count+=1
                elif answerKey[r]=='T':
                    count+=1
                r+=1
        ans=max(ans,count)
        
        #converting T to F
        l,r=0,0
        count=0
        m=k
        while r<n:
            # print(answerKey[r],count,m,l,r)
            if m<=0 and answerKey[r]=='T':
                if answerKey[l]=='T':
                    m+=1
                ans=max(ans,count)
                count-=1
                l+=1
            else:
                if answerKey[r]=='T' and m>0:
                    m-=1
                    count+=1
                elif answerKey[r]=='F':
                    count+=1
                r+=1
        ans=max(ans,count)
        return ans
                
                