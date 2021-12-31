class Solution:
    def recoverArray(self, nums):
        #check for all k in nums, k can only be in nums else it won't be possible
        #check if the num and num+k exist if they do then add num+k//2 to ans because our num is between num and num+k
        def check(nums, k):
            cnt, ans = Counter(nums), []
            for num in nums:
                if cnt[num] == 0: continue
                if cnt[num + k] == 0: return False, []
                cnt[num] -= 1
                cnt[num + k] -= 1
                ans += [num + k//2]
            return True, ans
            
        nums = sorted(nums)
        n = len(nums)
        for i in range(1, n):
            k = nums[i] - nums[0]
            if k != 0 and k % 2 == 0:
                a, b = check(nums, k)
                if a: return b