class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        """
        use bitmasks
        go over all the possible 2^12 cases where 1 means take and 0 means not take
        check if for that particular mask the score and the arrows used are less than alice
        go through all the masks and get the mask with the highest score
        generate the ans array for that mask
        """
        n=len(aliceArrows)
        
        def validMask(mask):
            score=0
            count=0
            for i in range(n):
                if mask&1<<i:
                    score+=i
                    count+=aliceArrows[i]+1
            if count<=numArrows:
                return score
            return 0
        
        def generateArray(mask):
            ans=[0]*n
            arrows=numArrows
            for i in range(n):
                if mask&1<<i:
                    ans[i]=aliceArrows[i]+1
                    arrows-=aliceArrows[i]+1
            ans[0]+=arrows
            return ans
        
        best=0
        r=0
        for i in range(1<<n):
            curr=validMask(i)
            if curr>best:
                best=curr
                r=i
        
        return generateArray(r)
            