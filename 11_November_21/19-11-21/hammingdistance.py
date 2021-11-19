class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x,y=bin(x)[2:],bin(y)[2:]
        x=(32-len(x))*'0'+x #add additional zeroes
        y=(32-len(y))*'0'+y
        count=0
        for bx,by in zip(x,y):
            if bx!=by:
                count+=1
        return count