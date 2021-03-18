class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        j = 2
        prev_diff = nums[1]-nums[0]
        answer = 2 if prev_diff != 0 else 1
        while j < len(nums):
            diff = nums[j]-nums[j-1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                answer += 1
                prev_diff = diff
            j += 1
        return answer


sol = Solution()
print(sol.wiggleMaxLength(nums=[0, 0, 0, 0]))
