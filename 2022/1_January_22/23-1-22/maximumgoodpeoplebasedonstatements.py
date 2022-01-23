class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        #use bitmask brute force subset thing
        #check for all possible combinations of good and bad people
        #only statements of good people count since they are always true
        #if there is a contradiction that particular mask cannot be true so give false
        
        n=len(statements)
        def check(mask):
            good=list()
            for i in range(n):
                if mask&(1<<i):
                    good.append(True)
                else:
                    good.append(False)
            for i in range(n):
                if good[i]:
                    for j in range(n):
                        if statements[i][j]==0 and good[j]==1:
                            return False
                        if statements[i][j]==1 and good[j]==0:
                            return False
            return True
        
        ans=0
        for i in range(1,1<<n):
            count=0
            if check(i):
                for j in range(n):
                    if i&(1<<j):
                        count+=1
            ans=max(ans,count)
        
        return ans
        