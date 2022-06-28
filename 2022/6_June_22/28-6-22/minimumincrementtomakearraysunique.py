class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        same as problem 1647
        """
        nums.sort()
        n=len(nums)
        minNum=min(nums)
        ans=0
        
        for num in nums:
            if num<minNum:
                ans+=minNum-num
                num=minNum
            minNum=num+1
        
        return ans