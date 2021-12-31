class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        prev = 0
        n = len(shifts)
        for i in range(n):
            shifts[i] += prev
            prev = shifts[i]
        shifts.reverse()
        shifts = list(map(lambda x: x % 26, shifts))
        ans = ''
        for i, letter in enumerate(s):
            new_letter = chr((ord(letter)-ord('a')+shifts[i]) % 26+ord('a'))
            ans += new_letter
        return ans
