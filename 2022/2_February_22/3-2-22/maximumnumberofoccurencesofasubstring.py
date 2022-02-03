class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count=Counter(s[i:i+minSize] for i in range(len(s)-minSize+1))
        return max([v for k,v in count.items() if len(set(k))<=maxLetters]+[0])