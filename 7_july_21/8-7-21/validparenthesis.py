class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        for letter in s:
            if letter==')' and stack and stack[-1]=='(':
                stack.pop()
            elif letter==']' and stack and stack[-1]=='[':
                stack.pop()
            elif letter=='}' and stack and stack[-1]=='{':
                stack.pop()
            elif letter==')' and stack and stack[-1]!='(':
                return False
            elif letter==']' and stack and stack[-1]!='[':
                return False
            elif letter=='}' and stack and stack[-1]!='{':
                return False
            else:
                stack.append(letter)
        if stack:
            return False
        return True
       
    