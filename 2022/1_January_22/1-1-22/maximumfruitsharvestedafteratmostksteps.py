class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        #use prefix sum to get the cumulative amount of fruits
        #the length of prefix array will be 2*10**5 as that is the maximum number of steps one can take
        #find the idx in fruits where the startpos would be using bisect, everything to the left will undergo one traversal and everything to the right will go another
        #update the ans with the max so far
        n=len(fruits)
        nk=2*10**5+1
        prefix=[0]*nk
        
        #prefix sum
        x=0
        for i in range(nk):
            if x>n-1:
                prefix[i]=prefix[i-1]
                continue
            if fruits[x][0]==i and i==0:
                prefix[i]=fruits[x][1]
                x+=1
                continue
            if fruits[x][0]==i:
                prefix[i]=fruits[x][1]+prefix[i-1]
                x+=1
            else:
                if i-1<0:
                    continue
                prefix[i]=prefix[i-1]
                 
        prefix=[0]+prefix
        
        #finding the idx of startPos
        ans=0
        idx=bisect_left(fruits,[startPos,0])
        
        #left side traversal
        for i in range(idx-1,-1,-1):
            l=fruits[i][0]
            if (startPos-l)>k:#we cant traverse more than k steps in any direction
                break
            if (startPos-l)*2>=k:#if the amount of steps is less than the direction we moved in ie we cant reach the startpos again
                r=startPos
            else:
                r=startPos+(k-2*(startPos-l))#the idx where we will end our journey
            r=min(r,nk-1)
            x=prefix[r+1]-prefix[l]
            ans=max(ans,x)
        
        #right side traversal
        for i in range(idx,len(fruits)):
            r=fruits[i][0]
            if (r-startPos)>k:
                break
            if (r-startPos)*2>=k:
                l=startPos
            else:
                l=startPos-(k-2*(r-startPos))
            l=max(l,0)
            x=prefix[r+1]-prefix[l]
            ans=max(ans,x)
        
        return ans
            