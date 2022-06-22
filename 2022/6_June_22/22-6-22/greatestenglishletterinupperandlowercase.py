class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        for letter in "abcdefghijklmnopqrstuvwxyz"[::-1]:
            if letter.upper() in s and letter in s:
                return letter.upper()
        return ""