class Solution:
    answers = list()

    def helper(self, path, index, digits):
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(path) == len(digits):
            self.answers.append("".join(path))
            return
        for letter in letters[digits[index]]:
            path.append(letter)
            self.helper(path, index+1, digits)
            path.pop()

    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        self.answers = list()
        self.helper([], 0, digits)
        return self.answers
