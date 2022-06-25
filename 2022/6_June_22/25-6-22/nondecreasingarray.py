class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/non-decreasing-array/discuss/1190833/Python-O(n)-solution-explained
        """
        flag=-1
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if flag!=-1:
                    return False
                flag=i
        return flag in [-1,0,n-2] or nums[flag-1]<=nums[flag+1] or nums[flag]<=nums[flag+2]