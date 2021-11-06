class Solution:
    def arrangeCoins(self, n: int) -> int:
        #can also use binary search or math intuition
        def coins(k):
            return k*(k+1)/2
        for k in range(2**31-1):
            if coins(k)>n:
                return k-1