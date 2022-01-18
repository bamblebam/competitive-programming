class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        m=len(flowerbed)
        count=0
        for i in range(1,m-1):
            if flowerbed[i]==flowerbed[i-1]==flowerbed[i+1]==0:
                count+=1
                flowerbed[i]=1
        return count>n-1