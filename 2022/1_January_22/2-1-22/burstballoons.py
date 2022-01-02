# This is quite difficult problem! Let us consider dp[i][j] the maximum number of coins we can get, popping balls from i to j, not including i and j. Why it is enough to keep these values? Let us look at the last popped balloon with number k. Then our balloons are separated into two groups: to the left of this balloon and the the right and we can write:

# dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) for k in (i+1,j),

# where k is the index of the last balloon burst in (i, j).

# Complexity: time complexity is O(n^3) and space complexity is O(n^2).

# You can see that code is very short, but it is in my opinion very diffucult to find this solution. How you can think in problems like this? First of all we are given, that n<500, which is quite small and we can try to understand what complexity we can expect. It is for sure not 2^500, so what is rest some polynomials and/or logarithms. So what we can expect is either O(n^2) or O(n^3), but no more than this. So at this moment we usually have 2 choises: either greedy or dp. It is not obvious how to do greedy for me, so the choise is dp. Now we can think that repeating subproblem is what is the answer on range (i, j). However the last step is something you can not invent quickly if you do not have experience in these type of problems. I can give you only intuition here: it is good idea to look at some extremal characteristic here: by this word I mean some object, which is either first/last, biggest/smallest and so on. Here our characteristic is last popped ballon on range, not the first we expect in simpler dp problems. Once you understand this logic, some other problems similar to this will be slightly simpler.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        
        for i in range(n-2,-1,-1):
            for j in range(i+2,n):
                dp[i][j]=max(nums[i]*nums[k]*nums[j]+dp[i][k]+dp[k][j] for k in range(i+1,j))
        
        return dp[0][n-1]