class Solution:
    def aux(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1

    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            length = max(self.aux(s, i, i), self.aux(s, i, i+1))
            if length > end-start:
                start = i-(length-1)//2
                end = i+length//2
        return s[start:end+1]


sol = Solution()
print(sol.longestPalindrome("babad"))
