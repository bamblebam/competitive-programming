class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        n=str(num)
        if n[-1]=="0":
            return False
        return True