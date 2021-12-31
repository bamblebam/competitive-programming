class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if k > 1:
            return ''.join(sorted(list(s)))
        ans = s
        for i in range(n):
            k_letters = list(s[:k])
            max_letter = max(k_letters)
            print(max_letter)
            k_letters.remove(max_letter)
            s = ''.join(k_letters)+s[k:]+max_letter
            if s < ans:
                ans = s
        return ans
