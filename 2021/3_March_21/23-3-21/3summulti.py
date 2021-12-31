import collections
import math


class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        nums = set(arr)
        nums_list = list(nums)
        combinations = set()
        count = collections.Counter(arr)
        answer = 0
        for i in range(len(nums_list)):
            for j in range(i, len(nums_list)):
                if target-(nums_list[i]+nums_list[j]) in nums:
                    combinations.add(
                        tuple(sorted([target-(nums_list[i]+nums_list[j]), nums_list[i], nums_list[j]])))
        for cand in combinations:
            count2 = collections.Counter(cand)
            answer2 = 1
            for key, item in count2.items():
                answer2 *= math.comb(count[key], item)
            answer += answer2
        return answer % (10**9 + 7)


sol = Solution()
print(sol.threeSumMulti(arr=[], target=5))
