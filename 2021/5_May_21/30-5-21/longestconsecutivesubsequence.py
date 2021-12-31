class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        ans = 1
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                current_num = num
                temp = 1
                while current_num+1 in nums_set:
                    current_num += 1
                    temp += 1
                ans = max(ans, temp)
        return ans
