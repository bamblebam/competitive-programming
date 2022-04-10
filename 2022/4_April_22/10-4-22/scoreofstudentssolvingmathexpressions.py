class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        """
        dp(i, j) will return all possible result for the substring from s[i] to s[j].
We enumerate the last operation s[m], which could be
s[m] = s[i+1], s[i+3] ,..., s[j-1]

Then we dfs-like find out the results for left part and right part.
We calculate the combine result of the whole substring with operation s[m].

One import optimization is that 0 <= answers[i] <= 1000,
so we will drop the result bigger than 1000.

use dp
select an op at idx i and calculate all the possible answers to its left and right
then just go over them all and create the list of final answers
if a answer is in that list it is correct
        """
        @lru_cache(None)
        def dp(i,j):
            if i==j:
                return {int(s[i])}
            res=dict()
            for m in range(i+1,j,2):
                for a in dp(i,m-1):
                    for b in dp(m+1,j):
                        curr=a*b if s[m]=='*' else a+b
                        if 0<=curr<=1000:
                            res[curr]=2
            return res
        
        res={**dp(0,len(s)-1),**{eval(s):5}}
        return sum(res.get(x,0) for x in answers)