class Solution:
    def diffWaysToCompute(self, expression: str):
        ans=list()
        if '+' not in expression and '-' not in expression and '*' not in expression:
            ans.append(int(expression))
        for idx,num in enumerate(expression):
            if num in "+-*":
                left=self.diffWaysToCompute(expression[:idx])
                right=self.diffWaysToCompute(expression[idx+1:])
                for l,a in enumerate(left):
                    for r,b in enumerate(right):
                        if num=='+':
                            ans.append(a+b)
                        elif num=='-':
                            ans.append(a-b)
                        elif num=='*':
                            ans.append(a*b)
        return ans