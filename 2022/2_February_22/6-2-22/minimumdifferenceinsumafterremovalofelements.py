class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        use heaps to keep track of the smallest sum at the left and largest sum at the right of n 
        the prefix array starts from left of midsection and when you find elem smaller than the smallest in lefty update it
        same with rigt but bigger elem
        then that will be the lsum and rsum for that particular n
        '''
        n=len(nums)//3
        left,right=list(),list()
        for i in range(n):
            left.append(-nums[i])
            right.append(nums[-i-1])
        heapify(left)
        heapify(right)
        
        lsum=-sum(left)
        rsum=sum(right)
        ans=lsum-rsum
        
        prefix=[lsum]
        suffix=[rsum]
        
        for i in range(n):
            curr=nums[n+i]
            leftc=-left[0]
            if curr<leftc:
                lsum+=(curr-leftc)
                heappush(left,-curr)
                heappop(left)
            prefix.append(lsum)
        
        for i in range(n):
            curr=nums[2*n-1-i]
            rightc=right[0]
            if curr>rightc:
                rsum+=(curr-rightc)
                heappush(right,curr)
                heappop(right)
            suffix.append(rsum)
        
        suffix.reverse()
        for l,r in zip(prefix,suffix):
            ans=min(ans,l-r)
        
        return ans
        
        
        
        
        