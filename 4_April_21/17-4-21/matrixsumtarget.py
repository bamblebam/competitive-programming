import itertools
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix, target) -> int:
        m, n = len(matrix), len(matrix[0])
        dp, answer = dict(), 0
        for k in range(m):
            t = [0]+list(itertools.accumulate(matrix[k]))
            for i, j in itertools.combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i, j, k-1), 0)+t[j]-t[i]
        for i, j in itertools.combinations(range(n+1), 2):
            count = collections.Counter([0])
            for k in range(m):
                answer += count[dp[i, j, k]-target]
                count[dp[i, j, k]] += 1
        return answer
