class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def clean_string(s, op, cl):
            balance = 0
            answer = ""
            for char in s:
                if char == op:
                    balance += 1
                    answer += char
                elif char == cl and balance > 0:
                    balance -= 1
                    answer += char
                elif char not in "()":
                    answer += char
            return answer
        return clean_string(clean_string(s, "(", ")")[::-1], ")", "(")[::-1]


sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
