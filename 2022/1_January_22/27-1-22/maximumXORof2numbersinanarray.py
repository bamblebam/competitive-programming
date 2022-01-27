class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        mask=0
        for i in range(31,-1,-1):
            mask|=1<<i
            found={num&mask for num in nums}
            start=res|1<<i
            for pref in found:
                if start^pref in found:
                    res=start
                    break
        return res