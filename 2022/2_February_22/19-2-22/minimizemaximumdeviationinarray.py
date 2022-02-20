class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        use heap
        if it is odd number it can only be multiplied by 2 once but if it is even it can be divided multiple times
        go through the nums if odd multiply by 2 and put in heap else just put in heap
        also update the smallest num found while doing this
        then go over the heap and take the largest element and update the ans
        if it is divisible by 2 divide it and put it back in the heap also update the smallest
        if odd break because everything else would be smaller than it
        '''
        h=list()
        n=len(nums)
        smallest=float("inf")
        for num in nums:
            if num%2:
                h.append(-num*2)
                smallest=min(smallest,num*2)
            else:
                h.append(-num)
                smallest=min(smallest,num)
        heapify(h)

        ans=float("inf")
        while h:
            x=-heappop(h)
            ans=min(ans,x-smallest)
            if x%2==0:
                heappush(h,-x//2)
                smallest=min(smallest,x//2)
            else:
                break
        
        return ans