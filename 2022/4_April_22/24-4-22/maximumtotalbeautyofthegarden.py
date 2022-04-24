class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        """
        use binary search to find the maximum number of flowers each bed can have before a right bound
        use this to calculate the partial bed score
        start from the end check if 1 full and other partial then 2 full and others partial and so on
        do this until you run out of newFlowers
        """
        flowers.sort()
        n=len(flowers)
        if flowers[0]>=target:
            return full*n
        
        prefix=[0]
        for x in flowers:
            prefix.append(prefix[-1]+x)
        
        def helper(flowersLeft,rightBound):
            if rightBound<0:
                return 0
            left,right=0,rightBound
            while left<right:
                mid=(left+right)//2
                if (prefix[mid+1]+flowersLeft)//(mid+1)>=flowers[mid+1]:
                    left=mid+1
                else:
                    right=mid
            #return the partial min
            return min(target-1,(prefix[left+1]+flowersLeft)//(left+1))
        
        ans=helper(newFlowers,n-1)*partial #assuming all flower beds are partial
        
        for i in range(n-1,-1,-1):
            delta=max(0,target-flowers[i])
            newFlowers-=delta
            if newFlowers<0:
                break
            
            partialMin=helper(newFlowers,i-1)
            fullCount=n-i
            
            ans=max(ans,partialMin*partial+full*fullCount)
        
        return ans