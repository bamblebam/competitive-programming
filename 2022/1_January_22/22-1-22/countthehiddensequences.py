class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix=[0]
        for num in differences:
            prefix.append(prefix[-1]+num)
        prefix=prefix[1:]
        mx,mn=max(prefix),min(prefix)
        count=0
        for i in range(lower,upper+1):
            if lower<=i+mx<=upper and lower<=i+mn<=upper:
                count+=1
        return count