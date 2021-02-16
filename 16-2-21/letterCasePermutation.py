class Solution(object):
    ans = []

    def letterCasePermutationAux(self, S, i=0):

        if i >= len(S):
            self.ans.append(S)
            return

        if S[i].isalpha():
            temp = list(S)
            temp[i] = S[i].upper() if S[i].islower() else S[i].lower()
            self.letterCasePermutationAux("".join(temp), i+1)

        self.letterCasePermutationAux(S, i+1)

    def letterCasePermutation(self, S):
        self.ans = []
        self.letterCasePermutationAux(S)
        return self.ans


sol = Solution()
print(sol.letterCasePermutation("RmR"))
