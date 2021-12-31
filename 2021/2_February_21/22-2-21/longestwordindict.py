class Solution:
    def findLongestWord(self, s, d):
        answer = ""
        for i, word in enumerate(d):
            j = 0
            for k in s:
                if j == len(word):
                    break
                if k == word[j]:
                    j += 1
            if j == len(word):
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer):
                    answer = min(word, answer)
        return answer


sol = Solution()
print(sol.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
