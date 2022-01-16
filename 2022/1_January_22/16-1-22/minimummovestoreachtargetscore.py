class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #go from the back decrementing and dividing
        #because when doubles are remaining and number is odd it is always better to divide
        ans=0
        while target!=1:
            if target%2:
                target-=1
                ans+=1
            elif not target%2 and maxDoubles:
                target/=2
                ans+=1
                maxDoubles-=1
            elif not maxDoubles:
                ans+=target-1
                target=1
        return int(ans)
                
            