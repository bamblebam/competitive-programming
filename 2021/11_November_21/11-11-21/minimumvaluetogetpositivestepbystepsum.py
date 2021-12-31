class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #use prefix sum to find the minimum sum.
        #the value required is the one that will make it 1 on addition
        prefix_sum=[0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        x=min(prefix_sum)
        if x>=0:
            return 1
        return x*-1 +1