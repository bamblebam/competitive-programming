class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(Counter(s)[letter]*100/len(s))