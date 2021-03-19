import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        count_dict = collections.Counter(nums)
        count_dict = dict(
            sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
        return list(count_dict.keys())[:k]


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3], k=2))
