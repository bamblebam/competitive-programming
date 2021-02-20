class Solution:
    def lengthOfLongestSubstring(self, s):
        answers = list()
        length = len(s)
        if length == 0:
            return 0
        for i in range(len(s)):
            chars = set()
            sum_ = 0
            for char in s[i:]:
                if char in chars:
                    break
                else:
                    sum_ += 1
                    chars.add(char)
            answers.append(sum_)
        return max(answers)


sol = Solution()
print(sol.lengthOfLongestSubstring(""))
