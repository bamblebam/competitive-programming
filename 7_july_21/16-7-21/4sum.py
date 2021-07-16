from collections import defaultdict


class Solution:
    def fourSum(self, nums, target: int):
        n = len(nums)
        ab = defaultdict(set)
        output = set()
        for i in range(n):
            for j in range(i+1, n):
                ab[nums[i]+nums[j]].add((nums[i], nums[j], j))

        for k in range(n):
            for l in range(k+1, n):
                if target-nums[k]-nums[l] in ab:
                    for a, b, j in ab[target-nums[k]-nums[l]]:
                        if k > j:
                            output.add(tuple(sorted((a, b, nums[k], nums[l]))))
        return list(output)
