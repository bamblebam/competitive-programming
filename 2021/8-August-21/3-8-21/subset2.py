from itertools import combinations,chain
class Solution:
    def subsetsWithDup(self, nums):
        set1 = set(chain.from_iterable(combinations(nums,i) for i in range(len(nums)+1)))
        set2=set()
        for s in set1:
            set2.add(tuple(sorted(s)))
        return set2