class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        d = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                d[nums[j]-nums[i]].append(i)
        for i in range(n-3):
            for j in range(i+1, n-2):
                count += sum(k > j for k in d[nums[i]+nums[j]])
        return count
