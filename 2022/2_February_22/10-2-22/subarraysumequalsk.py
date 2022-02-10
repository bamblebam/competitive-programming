class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Use hashmap to store the sum and the amount of yime it appears
        if for a sum s sum s-k exists increment the ans by the amount that s-k has
        then it becomes similar to 2 sum problem
        '''
        
        n=len(nums)
        ans=0
        count=Counter([0])
        sum_=0
        for num in nums:
            sum_+=num
            ans+=count[sum_-k]
            count[sum_]+=1
        return ans