class Solution:
    def minimumBuckets(self, street: str) -> int:
        #go through all test cases
        n=len(street)
        ans=0
        dp=[0]*n
        
        m=len(set(street))
        
        # if only dots
        if m==1 and street[0]==".":
            return 0
        #if only H
        if m==1 and street[0]=="H":
            return -1
        #if 3 H in row
        for i in range(1,n-2):
            if street[i-1]==street[i]==street[i+1]=="H":
                return -1
        #normal for loop for iterating over it
        for i in range(n):
            if street[i]==".":
                continue
            #if first elem is H the idx to the right should be . else it is invalid
            if street[i]=="H" and i==0:
                if street[i+1]!=".":
                    return -1
                dp[i+1]=1
                ans+=1
            #same for last H
            elif street[i]=="H" and i==n-1 and dp[i-1]!=1:
                if street[i-1]!=".":
                    return -1
                dp[i-1]=1
                ans+=1
            #if H in middle check if dp has anything in the left or right
            #if yes continue
            #else add bucket to the idx after H if possible else before H
            elif street[i]=="H":
                if dp[i-1]==1 or dp[i+1]==1:
                    continue
                else:
                    if street[i+1]==".":
                        dp[i+1]=1
                        ans+=1
                    elif street[i-1]==".":
                        dp[i-1]=1
                        ans+=1      
        return ans
            