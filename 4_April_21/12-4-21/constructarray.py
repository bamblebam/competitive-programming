class Solution:
    def constructArray(self, n, k):
        answer = list(range(n-k))
        for i in range(k+1):
            if not i % 2:
                answer.append(n-k+i//2)
            else:
                answer.append(n-i//2)
        return answer
