class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:int(len(s)/2)], s[int(len(s)/2):]
        vowels = 'aeiouAEIOU'
        answer = [0, 0]
        for i, half in enumerate([a, b]):
            for char in half:
                if char in vowels:
                    answer[i] += 1
        if answer[0] == answer[1]:
            return True
        return False


sol = Solution()
print(sol.halvesAreAlike('textbook'))
