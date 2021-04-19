import itertools
import collections


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        answer = 0
        t = list(itertools.accumulate(nums))
        c = collections.Counter([0])
        for i in range(len(nums)):
            answer += c.get(t[i]-k, 0)
            c[t[i]] += 1
        return answer
