class Solution:
    def letterCasePermutation(self, S):
        answers = list()
        length = len(S)
        if length == 1:
            if S[0].isalpha():
                return [S[0].lower(), S[0].upper()]
            return [S[0]]
        for i in range(length):
            temp = list(S)
            if temp[i].isalpha():
                for j in range(length):
                    temp[i] = temp[i].lower()
                    if j == i:
                        answers.append("".join(temp))
                    else:
                        if temp[j].isalpha():
                            temp[j] = temp[j].lower()
                            answers.append("".join(temp))
                            temp[j] = temp[j].upper()
                            answers.append("".join(temp))
                        else:
                            answers.append("".join(temp))
                    if j == i:
                        answers.append("".join(temp))
                    else:
                        if temp[j].isalpha():
                            temp[j] = temp[j].upper()
                            answers.append("".join(temp))
                            temp[j] = temp[j].lower()
                            answers.append("".join(temp))
                        else:
                            answers.append("".join(temp))
                    temp[i] = temp[i].upper()
                    if j == i:
                        answers.append("".join(temp))
                    else:
                        if temp[j].isalpha():
                            temp[j] = temp[j].upper()
                            answers.append("".join(temp))
                            temp[j] = temp[j].lower()
                            answers.append("".join(temp))
                        else:
                            answers.append("".join(temp))
                    if j == i:
                        answers.append("".join(temp))
                    else:
                        if temp[j].isalpha():
                            temp[j] = temp[j].lower()
                            answers.append("".join(temp))
                            temp[j] = temp[j].upper()
                            answers.append("".join(temp))
                        else:
                            answers.append("".join(temp))
            else:
                answers.append("".join(temp))
        return set(answers)


sol = Solution()
print(sol.letterCasePermutation("RmR"))
