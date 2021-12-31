class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #take all powersets and compare with the maximum or
        max_or=0
        for num in nums:
            max_or|=num
        ans=0
        
        def powerset(s):
            return chain.from_iterable(combinations(s,r) for r in range(1,len(s)+1))
        
        def check_or(s):
            sum_or=0
            for num in s:
                sum_or|=num
            if sum_or==max_or:
                return True
            return False
        
        t=powerset(nums)
        for r in t:
            if check_or(r):
                ans+=1
        
        return ans
        