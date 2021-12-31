class Solution:
    def climbStairs(self, n: int) -> int:
        n = n+1
        phi = (1+math.sqrt(5))/2
        return round(pow(phi, n)/math.sqrt(5))
