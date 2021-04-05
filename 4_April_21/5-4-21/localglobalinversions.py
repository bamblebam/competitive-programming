class Solution:
    def isIdealPermutation(self, A) -> bool:
        max_ = -1
        for i in range(len(A)-2):
            max_ = max(max_, A[i])
            if max_ > A[i+2]:
                return False
        return True
