# similar to matchstick problem
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sum_ = sum(nums)/k
        if sum_ != sum(nums)//k:
            return False
        if max(nums) > sum_:
            return False

        @lru_cache(None)
        def helper(mask, subsets):
            total = 0
            for i in range(n-1, -1, -1):
                if not 1 << i & mask:
                    total += nums[i]
            if total > 0 and total % sum_ == 0:
                subsets += 1
            if subsets == k-1:
                return True

            ans = False
            curr = int(total/sum_)
            rem = sum_*(curr+1)-total

            for i in range(n-1, -1, -1):
                if nums[i] <= rem and mask & 1 << i:
                    if helper(mask ^ 1 << i, subsets):
                        ans = True
            return ans

        return helper((1 << n)-1, 0)
