class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n, s = len(cardPoints), sum(cardPoints)
        answer = window = sum(cardPoints[:n-k])
        for i in range(n-k, n):
            window = window-cardPoints[i-n+k]+cardPoints[i]
            answer = min(window, answer)
        return s-answer
