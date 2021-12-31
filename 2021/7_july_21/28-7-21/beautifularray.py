class Solution:
    def beautifulArray(self, n: int):
        memo={1:[1]}
        def helper(n):
            if n not in memo:
                even=helper(n//2)
                odd=helper((n+1)//2)
                memo[n]=[2*x-1 for x in odd]+[2*x for x in even]
            return memo[n]
        return helper(n)