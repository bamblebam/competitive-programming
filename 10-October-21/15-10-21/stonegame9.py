class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        #helper function checks for 2 cases if alice picks stone divisible by 3 or not.
        #check iterartively for each turn if there is a stone which when added to the sum is not divisible by 3, if not then whose turn it is will lose 
        #use counter for that
        n=len(stones)
        def helper(x):
            count=collections.Counter(i%3 for i in stones)
            if count[x]==0:
                return False
            curr=x
            count[x]-=1
            
            for i in range(n-1):
                found=False
                for j in range(3):
                    if (j+curr)%3!=0 and count[j]>0:
                        found=True
                        curr=(j+curr)%3
                        count[j]-=1
                        break
                if not found:
                    if i%2:
                        return False
                    return True
            return False
        return helper(1) or helper(2)
                    
        