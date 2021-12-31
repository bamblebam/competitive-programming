class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)/2
        candies = set(candyType)
        if n >= len(candies):
            return int(len(candies))
        return int(n)


sol = Solution()
print(sol.distributeCandies([]))
