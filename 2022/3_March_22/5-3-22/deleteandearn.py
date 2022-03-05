class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        top down dp
        """
        count=Counter(nums)
        @cache
        def helper(num):
            if num==0:
                return 0
            if num==1:
                return count[1]
            return max(helper(num-1),helper(num-2)+num*count[num])
        return helper(max(nums))