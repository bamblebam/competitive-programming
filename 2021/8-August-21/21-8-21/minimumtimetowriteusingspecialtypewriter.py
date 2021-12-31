class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = 0
        for letter in word:
            curr = ord(letter)-ord('a')
            time += min(abs(curr-prev), (26-abs(curr-prev)))
            prev = curr
        time += len(word)
        return time
