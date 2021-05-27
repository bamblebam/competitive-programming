class Solution:
    def maxProduct(self, words) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if len(set(words[i]) & set(words[j])) == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
