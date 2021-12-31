class Solution:
    def helper(self, s, start, end):
        answer = 0
        while(start >= 0 and end < len(s)):
            if s[start] != s[end]:
                break
            answer += 1
            start -= 1
            end += 1
        return answer

    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            answer += self.helper(s, i, i)
            answer += self.helper(s, i, i+1)
        return answer


sol = Solution()
print(sol.countSubstrings("aaa"))
