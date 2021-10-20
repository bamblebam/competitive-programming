class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        ans=" ".join(s.split()[::-1])
        return ans