class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        use a monotone stack of sorts
        go through each digit in num and if it is smaller than the the last element of stack and there are more k available remove them from stack
        final ans is just the ones that remain in stack
        '''
        attempts,stack=k,list()
        for digit in num:
            while stack and digit<stack[-1] and attempts>0:
                attempts-=1
                stack.pop()
            stack.append(digit)
        out="".join(stack[:len(num)-k]).lstrip("0")
        return "0" if out=="" else out
                