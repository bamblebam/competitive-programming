class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        def check(s):
            if s == s[::-1]:
                return True
            return False
        best = None
        for i in range(n):
            if palindrome[i] == 'a':
                x = palindrome[:i]+'b'+palindrome[i+1:]
                if not check(x):
                    if i != 0:
                        best = min(best, x)
                    if i == 0:
                        best = x
            else:
                x = palindrome[:i]+'a'+palindrome[i+1:]
                if not check(x):
                    if i != 0:
                        best = min(best, x)
                    if i == 0:
                        best = x
        return best
