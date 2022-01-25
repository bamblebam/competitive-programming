class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3:
            return False
        inc=True
        for i in range(1,n):
            x=arr[i]-arr[i-1]
            if x==0:
                return False
            if x>0 and not inc:
                return False
            if x<0:
                inc=False
            if not inc and i==1:
                return False
            if inc and i==n-1:
                return False
        return True