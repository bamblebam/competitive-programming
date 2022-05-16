class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count=Counter()
        for i in range(0,31):
            for num in candidates:
                if num&1<<i:
                    count[i]+=1
        return max([v for v in count.values()])