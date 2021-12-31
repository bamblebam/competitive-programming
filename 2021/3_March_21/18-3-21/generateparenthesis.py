class Solution:
    answer = list()

    def helper(self, string_, max_, left, right):
        if len(string_) == max_*2:
            self.answer.append(string_)
            return None
        if left < max_:
            self.helper(string_+"(", max_, left+1, right)
        if right < left:
            self.helper(string_+")", max_, left, right+1)

    def generateParenthesis(self, n: int):
        self.answer = list()
        self.helper("", n, 0, 0)
        return self.answer


sol = Solution()
print(sol.generateParenthesis(3))
