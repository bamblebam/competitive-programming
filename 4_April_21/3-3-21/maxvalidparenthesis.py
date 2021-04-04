class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        answer = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                answer = max(answer, 2*right)
            elif right > left:
                right = left = 0
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                answer = max(answer, 2*left)
            elif left > right:
                left = right = 0
        return answer
