class Solution:
    def stoneGame(self, piles) -> bool:
        n=len(piles)
        def helper(arr):
            count=0
            if len(arr)<=0:
                return count
            if arr[0]>arr[-1]:
                count+=helper(arr[1:])+arr[0]
            else:
                count+=helper(arr[:-1])+arr[-1]
            if count>0:
                return True
            else:
                return False
        return helper(piles)